# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:24:30 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
number = 1
x,y,z = mc.player.getTilePos()
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
    number = number*2
    mc.postToChat("現在生成了"+str(number)+"隻蠹魚")