from gpiozero import RotaryEncoder, PWMLED
from signal import pause

rotor = RotaryEncoder(22, 19, wrap=True, max_steps=180)
led = PWMLED(pin=18, initial_value=0.0)

STEP = 0.05

def increase_brightness():
    led.value = min(1.0, led.value + STEP)
def decrease_brightness():
    led.value = max(0.0, led.value - STEP)

rotor.when_rotated_clockwise = increase_brightness
rotor.when_rotated_counter_clockwise = decrease_brightness

pause()
