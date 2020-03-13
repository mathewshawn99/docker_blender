# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:11:34 2020

@author: mathesn
"""

import bpy, _cycles
import time
import math
import os

for card in bpy.context.user_preferences.addons['cycles'].preferences.devices:
    print(card.name)

prefs = bpy.context.user_preferences.addons['cycles'].preferences
prefs.compute_device_type = 'CUDA'
prefs.devices[0].use = True

bpy.ops.wm.save_userpref()




print("Running")

bpy.data.scenes['Scene'].render.filepath = os.path.join("test.png")
bpy.ops.render.render()
