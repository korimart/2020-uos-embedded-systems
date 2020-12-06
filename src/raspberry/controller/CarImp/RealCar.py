# Copyright(c) Reserved 2020.
# Donghee Lee, University of Soul
#
__author__ = "will"

import serial
import numpy as np

from ..Car import Car


class RealCar(Car):
    def __init__(self, carCamera):
        super().__init__(carCamera)

        self.left_wheel = 0
        self.right_wheel = 0
        self.ser = serial.Serial("/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_75830333438351710240-if00", 9600)
        self.memory = []

    def finish_iteration(self):
        print("finish iteration")

    def set_right_speed(self, speed):
        ''' Speed is ignored
        '''

        self.right_wheel = speed
        rcmd = ("R%d\n" % speed).encode("ascii")

        self.ser.write(rcmd)
        self.ser.write(rcmd)
        self.ser.write(rcmd)
        self.ser.write(rcmd)
        self.ser.write(rcmd)
        self.ser.write(rcmd)
        
        print(self.left_wheel, self.right_wheel)

    def set_left_speed(self, speed):
        ''' Speed is ignored
        '''

        self.left_wheel = speed
        cmd = ("L%d\n" % speed).encode("ascii")
        
        self.ser.write(cmd)
        self.ser.write(cmd)
        self.ser.write(cmd)
        self.ser.write(cmd)
        self.ser.write(cmd)
        self.ser.write(cmd)
        
        print(self.left_wheel, self.right_wheel)

    def stop(self):  # robot stop
        print("stop")

    def get_image_from_camera(self):
        image = self.carCamera.getImage()
        self.memory.append([self.left_wheel, self.right_wheel, image])
        return image

    def save(self, path):
        toSave = np.array(self.memory)
        np.save(path, toSave)