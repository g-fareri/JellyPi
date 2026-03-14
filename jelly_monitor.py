import os
import time
import socket
import psutil
import datetime
import RPi.GPIO as GPIO
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import Image, ImageDraw

# --- CONFIGURATION ---
TOUCH_PIN = 17
FAN_PIN = 14
TEMP_THRESHOLD = 58.0
SHUTDOWN_HOLD_TIME = 8

# --- HARDWARE SETUP ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_PIN, GPIO.IN)
GPIO.setup(FAN_PIN, GPIO.OUT)
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

# --- CREATE DRAWN LOGO ---
logo_w, logo_h = 35, 20
logo_img = Image.new("1", (logo_w, logo_h))
draw_logo = ImageDraw.Draw(logo_img)
draw_logo.ellipse([0, 0, logo_w-1, logo_h-1], outline="white")
draw_logo.text((6, 5), "DVD", fill="white")

# Variables
x, y, dx, dy = 10, 10, 2, 2
corner_timer = 0
corner_count = 0

def get_stats():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except: ip = "No Network"
    
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = float(f.read()) / 1000
    
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    up = f"{(datetime.datetime.now() - boot_time).days}d"
    return ip, up, temp

try:
    while True:
        ip, uptime, current_temp = get_stats()
        GPIO.output(FAN_PIN, current_temp > TEMP_THRESHOLD)

        # --- SENSOR LOGIC (Touch, Stats, or Shutdown) ---
        if GPIO.input(TOUCH_PIN):
            touch_start = time.time()
            is_shutdown = False
            
            # While the sensor is being held
            while GPIO.input(TOUCH_PIN):
                hold_duration = time.time() - touch_start
                
                with canvas(device) as draw:
                    if hold_duration < 3:
                        # Normal Stats
                        draw.text((0, 0),  f"IP: {ip}", fill="white")
                        draw.text((0, 16), f"UP: {uptime} | CPU: {current_temp:.1f}C", fill="white")
                        draw.text((0, 32), f"DSK: {psutil.disk_usage('/').percent}%", fill="white")
                        draw.text((0, 48), "Hold for Shutdown...", fill="white")
                    elif hold_duration < SHUTDOWN_HOLD_TIME:
                        # Shutdown Warning
                        countdown = int(SHUTDOWN_HOLD_TIME - hold_duration)
                        draw.rectangle(device.bounding_box, outline="white", fill="black")
                        draw.text((10, 20), f"SHUTTING DOWN IN {countdown}...", fill="white")
                    else:
                        # Trigger Shutdown
                        draw.rectangle(device.bounding_box, outline="white", fill="white")
                        draw.text((20, 25), "SYSTEM HALTING", fill="black")
                        is_shutdown = True
                        break
                time.sleep(0.1)

            if is_shutdown:
                time.sleep(2)
                os.system("sudo shutdown -h now")
                break # Exit the script
        
        # --- DVD BOUNCE MODE ---
        else:
            hit_x, hit_y = False, False
            x += dx
            y += dy

            if x <= 0 or x + logo_w >= device.width:
                dx = -dx
                hit_x = True
            if y <= 0 or y + logo_h >= device.height:
                dy = -dy
                hit_y = True

            if hit_x and hit_y:
                corner_timer = 35 
                corner_count += 1

            with canvas(device) as draw:
                draw.bitmap((x, y), logo_img, fill="white")
                if corner_timer > 0:
                    draw.rectangle([15, 15, 113, 45], outline="white", fill="black")
                    draw.text((25, 20), "CORNER HIT!", fill="white")
                    draw.text((45, 32), f"Total: {corner_count}", fill="white")
                    corner_timer -= 1
            
            time.sleep(0.02)

except KeyboardInterrupt:
    GPIO.cleanup()
