#https://core-electronics.com.au/tutorials/ir-controlled-lights-with-circuitpython-adafruit-circuit-playground-express-tutorial.html
from adafruit_circuitplayground.express import cpx
import board
import random
import time
import pulseio
import array

# Creates IR output pulse
pwm = pulseio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulse = pulseio.PulseOut(pwm)


pulse_A = array.array('H', [1000, 3800, 65000, 950, 300, 200, 300, 1000, 350, 175,
    275, 215, 275, 250, 275, 215, 275, 225, 275, 215, 275, 1000, 300, 225, 275,
    950, 300, 950, 300, 1000, 300, 950, 300, 250, 275, 700, 300, 950, 300, 450,
    300, 475, 300, 215, 275, 725, 300, 950, 300, 200, 300, 715, 325, 900, 315,
    425, 315, 1000, 65000])
pulse_B = array.array('H', [1000, 3800, 65000, 960, 300, 200, 300, 950, 350, 190,
    215, 245, 300, 225, 275, 225, 275, 215, 275, 200, 300, 700, 300, 200, 300,
    700, 300, 1000, 315, 675, 300, 1000, 300, 200, 300, 700, 300, 950, 300,
    950, 300, 700, 300, 700, 300, 450, 300, 475, 275, 715, 300, 225, 275, 450,
    300, 450, 300, 1000, 65000])


while True:
# when button is pressed, send IR pulse
# detection is paused then cleared and resumed after a short pause
# this prevents reflected detection of own IR
    while cpx.button_a:
        pulse.send(pulse_A)  # sends IR pulse
        time.sleep(.2)  # wait so pulses dont run together

    while cpx.button_b:
        pulse.send(pulse_B)
        time.sleep(.2)
        
