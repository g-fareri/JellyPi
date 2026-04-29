# JellyPi
Raspberry Pi Gateway for Remote Access to Jellyfin Server

JellyPi is a Raspberry Pi–based network gateway designed to securely and reliably provide remote access to a self-hosted Jellyfin media server located on a separate network. Originally built as a Tailscale subnet router, the system has been upgraded into an NGINX reverse-proxy gateway for improved control and reliability.
# Overview

This project transforms a Raspberry Pi 4 into an intelligent network access point that bridges a remote location (family network) with a private home media server. Instead of relying solely on subnet routing, JellyPi now uses NGINX reverse proxying over Tailscale to securely forward traffic to the Jellyfin server.

This setup allows devices on the remote network to access the media server as if it were local.

# Key Features
#Network Gateway
Migrated from Tailscale subnet routing to NGINX reverse proxy architecture
Securely forwards traffic to Jellyfin server via Tailscale IP
Simplifies access to media services across networks
#Remote Media Access
Enables seamless Jellyfin streaming from a remote location
Maintains private network isolation using Tailscale VPN
#System Monitoring (Hardware-Based)
OLED display shows system status and animations (“DVD bounce” screensaver)
Touch sensor provides real-time system info:
IP address
CPU temperature
System uptime
Disk usage
#Active Cooling System
Temperature-controlled 5V fan system
Automatically activates via transistor circuit when CPU exceeds 58°C
#Technology Stack
Raspberry Pi OS (Linux)
Tailscale VPN
NGINX reverse proxy
Jellyfin media server (remote host)
Python (hardware control scripts)

#Hardware
Raspberry Pi 4 Model B
0.96” I2C OLED Display (SSD1306)
TTP223B Capacitive Touch Sensor
5V DC Cooling Fan
2N2222A NPN Transistor
330Ω Resistor

#Evolution of Project
Started as a Tailscale subnet router
Upgraded to NGINX reverse proxy gateway
Added hardware monitoring + cooling system
Optimized for stability and real-world usability

![image alt](https://github.com/g-fareri/JellyPi/blob/5053ac5a5f54830f51e90367856e3f92caff5f6f/jelly_pi_done.png)
