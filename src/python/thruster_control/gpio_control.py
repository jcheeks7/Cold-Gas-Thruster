import RPi.GPIO as GPIO
import time

VALVE_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(VALVE_PIN, GPIO.OUT)
GPIO.output(VALVE_PIN, GPIO.LOW)

def fire_valve(duration):
    GPIO.output(VALVE_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(VALVE_PIN, GPIO.LOW)
