# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:03:48 2021

@author: 瑛
"""
import time
def Format_LocalTime_ToFileName():
    rtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return rtime
#==============================================================================
#     localtime = time.localtime()
#     
#     year = localtime.tm_year
#     month = localtime.tm_mon
#     day = localtime.tm_mday
#     hour = localtime.tm_hour
#     minute = localtime.tm_min
#     sec = localtime.tm.sec
#     
#     fina_time = "{0}{1}{2}{3}{4}{5}".format(year,month,day,hour,minute,sec)
#     print(fina_time)
#     return fina_time
#==============================================================================



import calendar
def Calendar(year,mon):
    cal = calendar.month(year, mon)
    return cal
