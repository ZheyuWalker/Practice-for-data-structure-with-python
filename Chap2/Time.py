#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Time(object):
    @staticmethod
    def num_check(a, b, c):
        if (isinstance(a, int) and 
            isinstance(b, int) and
            isinstance(c, int)):
            if ((a<0 or a>=24) or 
                (b<0 or b>=60) or
                (c<0 or c>=60)):
                raise ValueError
            else:
                pass
        else:
            raise TypeError

    def __init__(self, hours, minutes, seconds):
        Time.num_check(hours, minutes, seconds)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._time = hours * 3600 + minutes * 60 + seconds

    def __eq__(self, another):
        return self._time == another._time

    def __lt__(self, another):
        return self._time < another._time

    def __add__(self, another):
        total_sec = (self._time + another._time) % 86400
        new_h = total_sec // 3600
        new_m = (total_sec - 3600*new_h) // 60
        new_s = total_sec % 60
        return Time(new_h, new_m, new_s)

    def __sub__(self, another):
        total_sec = (self._time - another._time + 86400) % 86400
        new_h = total_sec // 3600
        new_m = (total_sec - 3600*new_h) // 60
        new_s = total_sec % 60
        return Time(new_h, new_m, new_s)

    def get_time(self):
        print('{:02}:{:02}:{:02}'.format(self.hours, self.minutes, self.seconds))


a = Time(12, 24, 12)
b = Time(13, 45, 34)
(a+b).get_time()
(a-b).get_time()
