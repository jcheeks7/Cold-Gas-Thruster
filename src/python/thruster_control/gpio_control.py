import lgpio
import time

VALVE_PIN = 17

h = lgpio.gpiochip_open(0)

lgpio.gpio_claim_output(h, VALVE_PIN)

def fire_valve(duration):
    lgpio.gpio_write(h, VALVE_PIN, 1)
    time.sleep(duration)
    lgpio.gpio_write(h, VALVE_PIN, 0)
