# -*- coding: utf-8 -*-
"""
28BYJ-48 Stepper Motor with ULN2003 driver board

Credits
    http://www.scraptopower.co.uk/Raspberry-Pi/how-to-connect-stepper-motors-a-raspberry-pi
    https://github.com/custom-build-robots/Stepper-motor-28BYJ-48-Raspberry-Pi/commit/d8f6b5f3ee4d6b22d3fe40d81d0be09287c97c89

On the ULN2003A board, connect:
    IN1 to GPIO 6
    IN2 to GPIO 13
    IN3 to GPIO 19
    IN4 to GPIO 26

    "-" to a GND/Ground pin
    "+" to a 5V pin

Hint: run 'pinout' at the terminal to get a graphical representation of the
Pi's GPIO pin numbering layout.
"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

IN1 = 6  # IN1 connected to GPIO 6
IN2 = 13  # IN2 connected to GPIO 13
IN3 = 19  # IN3 connected to GPIO 19
IN4 = 26  # IN4 connected to GPIO 26


# Waiting time controls the speed at which the motor runs
time = 0.001

# Define the pins from the outputs
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# All pins are initially set to False
GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

# The stepper motor 28BYJ-48 is constructed in such a way that 8 steps are
# needed for the motor to turn. The 8 steps are controlled by step functions
# Step1() - Step8() that run in a sequence, on after the other.

# To turn 360° the step functions, Step1-8, must run 512 times
# To turn 180° the step functions must run 256 times.
# To turn 90°, 128 times etc.

# Definition of steps 1 - 8 via pins IN1 to IN4
# Between each movement, the motor briefly waits for the motor anchor to reach
# its position.


def Step1():
    GPIO.output(IN4, True)
    sleep(time)
    GPIO.output(IN4, False)


def Step2():
    GPIO.output(IN4, True)
    GPIO.output(IN3, True)
    sleep(time)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)


def Step3():
    GPIO.output(IN3, True)
    sleep(time)
    GPIO.output(IN3, False)


def Step4():
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    sleep(time)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)


def Step5():
    GPIO.output(IN2, True)
    sleep(time)
    GPIO.output(IN2, False)


def Step6():
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
    sleep(time)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)


def Step7():
    GPIO.output(IN1, True)
    sleep(time)
    GPIO.output(IN1, False)


def Step8():
    GPIO.output(IN4, True)
    GPIO.output(IN1, True)
    sleep(time)
    GPIO.output(IN4, False)
    GPIO.output(IN1, False)


def left(step):
    # Turn the motor left
    for i in range(step):
        # os.system('clear') # Slows down the movement of the engine too much
        Step1()
        Step2()
        Step3()
        Step4()
        Step5()
        Step6()
        Step7()
        Step8()
        # print("Step left: ",i)


def right(step):
    # Turn the motor right
    for i in range(step):
        # os.system('clear') # Slows down the movement of the engine too much
        Step8()
        Step7()
        Step6()
        Step5()
        Step4()
        Step3()
        Step2()
        Step1()
        # print("Step right: ",i)

# Test the motor


def test(move_right=512, move_left=512):
    right(move_right)  # Turns 360° to the right
    # sleep(5)
    left(move_left)  # Turns 360° to the left
    GPIO.cleanup()


if __name__ == "__main__":
    test()
