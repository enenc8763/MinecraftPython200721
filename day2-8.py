# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:51:05 2020

@author: us我愛minecraft,也愛python er
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,"我愛minecraft","也愛python")
 