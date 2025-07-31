import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT)  # or whatever pin

def fire_valve(seconds):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(11, GPIO.LOW)
