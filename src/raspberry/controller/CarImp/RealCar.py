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
        print("set right speed to ", speed)
        cmd = ("R%d*" % speed).encode("ascii")
        print("My cmd is %s" % cmd)
        self.ser.write(cmd)
        print("return was {}".format(self.ser.readline()))

    def set_left_speed(self, speed):
        print("set left speed to ", speed)
        cmd = ("L%d*" % speed).encode("ascii")
        print("My cmd is %s" % cmd)
        self.ser.write(cmd)
        print("return was {}".format(self.ser.readline()))

    def stop(self):  # robot stop
        print("stop")