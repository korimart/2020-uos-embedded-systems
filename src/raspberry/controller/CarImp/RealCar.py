# Copyright(c) Reserved 2020.
# Donghee Lee, University of Soul
#
__author__ = "will"

import serial

from ..Car import Car


class RealCar(Car):
    def __init__(self, carCamera):
        super().__init__(carCamera)

        self.left_wheel = 0
        self.right_wheel = 0
        self.ser = serial.Serial("/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_75830333438351710240-if00", 9600)

    def finish_iteration(self):
        print("finish iteration")

    def set_right_speed(self, speed):
        cmd = ("R%d\n" % speed).encode("ascii")
        self.ser.write(cmd)
        print(self.left_wheel, self.right_wheel)

    def set_left_speed(self, speed):
        cmd = ("L%d\n" % speed).encode("ascii")
        self.ser.write(cmd)
        print(self.left_wheel, self.right_wheel)

    def stop(self):  # robot stop
        print("stop")