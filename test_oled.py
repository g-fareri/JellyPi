from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
import time

# Initialize the I2C interface
serial = i2c(port=1, address=0x3C)

# Initialize the device
device = ssd1306(serial)

print("Displaying 'Hello Pi!'... Press Ctrl+C to stop.")

try:
    with canvas(device) as draw:
        # Draw a white border
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        # Write text (coordinates are x, y)
        draw.text((30, 25), "Hello Pi!", fill="white")
    
    # Keep the script alive so the image stays on the screen
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nCleaning up and shutting down.")
