# hc_sr04_activated_28byj_48
Activates 2BYJ-48 stepper motor with ULN2003 module using an HR-S04 ultrasonic distance sensor.

## Connecting HC-SR04 to the Raspberry Pi
1. Plug four of your male to female jumper wires into the pins on the HC-SR04 as follows:
- Red -> Vcc
- Blue -> Trig
- Yellow -> Echo
- Black -> Gnd
2. Plug **Vcc** into the positive rail of your breadboard, and plug GND into your negative rail.
3. Plug GPIO 5V [Pin 2] into the positive rail, and GPIO GND [Pin 6] into the negative rail.
    See [here](https://github.com/frankenwino/hc_sr04_activated_28byj_48/raw/master/hc_sr04_activated_28byj_48/images/3.%20hc-sr04-tut-4_1024x1024.jpg).
4. Plug **Trig** into a blank rail, and plug that rail into GPIO 23 [Pin 16]. (You can plug **Trig** directly into GPIO 23 if you want).
    See [here](https://github.com/frankenwino/hc_sr04_activated_28byj_48/raw/master/hc_sr04_activated_28byj_48/images/4.%20hc-sr04-tut-5_1024x1024.jpg).
5. Plug **Echo** into a blank rail, link another blank rail using a 1kΩ resistor (R1)
6. Link your R1 rail with the **Gnd** rail using a 2kΩ resistor (R2). Leave a space between the two resistors.
    See [here](https://github.com/frankenwino/hc_sr04_activated_28byj_48/raw/master/hc_sr04_activated_28byj_48/images/6.%20hc-sr04-tut-6_1024x1024.jpg).
7. Add GPIO 24 [Pin 18] to the rail with your R1 (1kΩ resistor). This GPIO pin needs to sit between R1 and R2

That's it! The HC-SR04 sensor is connected to our Raspberry Pi!
    See [here](https://github.com/frankenwino/hc_sr04_activated_28byj_48/raw/master/hc_sr04_activated_28byj_48/images/8.%20hc-sr04-tut-8_1024x1024.jpg).
