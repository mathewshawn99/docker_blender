# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:11:34 2020

@author: mathesn
"""

import bpy, _cycles
import time
import math
import os

import datetime

x = datetime.datetime.now()
LOG_FILE_NAME = x.strftime("%Y-%m-%d %H-%M-%S") + ".txt"
LOG_FILE= open("logs/" + LOG_FILE_NAME,"w+")

#start time
LOG_FILE.write("Began at:" + str(datetime.datetime.now()))



print("Running")

bpy.context.scene.render.filepath = "test.png"
bpy.ops.render.render(write_still = True)

LOG_FILE.write("\nDone rendering at:" + str(datetime.datetime.now()))
  
LOG_FILE.close()