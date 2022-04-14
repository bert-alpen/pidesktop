#!/user/bin/env python

# pd-reboot.py - oneshot script so do your thing and exit
#
# We are in reboot processing because reboot is running. This cannot have been 
# initiated by the shutdown button.
#
import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Use physical board pin numbering
GPIO.setup(31,GPIO.OUT)  # Pi to Power MCU communication
GPIO.setup(33,GPIO.IN)   # Power MCU to Pi on power button

# In practice we should not be here because of a shutdown button press. 
# If this is case we want to log it. 
if GPIO.input(33):
	# Power Key was pressed
	print("pidesktop: reboot script unexpected power button detected")
else:
	# reboot initiated by other means (i.e. reboot command executed)
	print("pidesktop: reboot script active")

# we're done
print("pidesktop: reboot script completed")
