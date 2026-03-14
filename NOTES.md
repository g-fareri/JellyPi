## Service Management Cheat Sheet
If I need to edit the code for the case assembly:

# 1. Stop the background service
sudo systemctl stop jelly-oled.service

# 2. Make changes to jelly_monitor.py
nano jelly_monitor.py

# 3. Test manually
source ~/jellypi-env/bin/activate
python3 jelly_monitor.py

# 4. Restart the background service
sudo systemctl start jelly-oled.service

# 5. Check if it's running okay
sudo systemctl status jelly-oled.service
