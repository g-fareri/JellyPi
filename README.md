# JellyPi
Turned a Raspberry Pi into a subnet router
# Jelly-Router 
Tailscale Subnet Router with OLED Status & Active Cooling
A hardware-monitored Raspberry Pi 4 Subnet Router designed to provide seamless access to a home Jellyfin server from a remote location. This project features a custom OLED interface, a capacitive touch "stealth" button, and temperature-controlled cooling.
# Features
Subnet Routing: Bridges two networks via Tailscale so remote devices (TVs, Tablets) see the Jellyfin server as if it were local.

Dynamic OLED Display: Features a "DVD Bounce" screensaver with a "Corner Hit" detector and counter.

Real-time Monitoring: Tap the touch sensor to view IP address, system uptime, CPU temperature, and disk usage.

Active Cooling: 5V fan triggered automatically via transistor when CPU exceeds 58°C.

# Hardware
Raspberry Pi 4 Model B (1GB+)

OLED Display - 0.96" I2C (SSD1306)

Touch Sensor - TTP223B Capacitive Switch

Cooling Fan - 5V DC (LD3007MS)

Transistor - 2N2222A (NPN)

Resistor - 330Ω

![image alt](https://github.com/g-fareri/JellyPi/blob/5053ac5a5f54830f51e90367856e3f92caff5f6f/jelly_pi_done.png)
