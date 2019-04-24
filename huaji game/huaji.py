#usr/bin/env python
#-*- coding:utf-8- -*-
import pygame
import random

SMALLSIZE=50

# 敌机 - 滑稽
class Huaji():
    imgpath="img/smallhuaji.png"
    speed=2

    def __init__(self,master,x,y=0):
        self._master=master # 父控件
        self.image=pygame.image.load(self.imgpath)
        self.x=x
        self.y=y
        self.lives=1

    # 移动敌机，更新敌机位置
    def update(self):
        self.y+=self.speed

    def draw(self):
        self._master.blit(self.image,(self.x,self.y))

    def inWindow(self):
        if self.y<0 or self.y>self._master.get_height():
            return False
        return True

    def get_center_XY(self):
        # 获取圆心坐标
        return (self.x+SMALLSIZE/2,self.y+SMALLSIZE/2)

    def get_radius(self):
        # 获取半径
        return SMALLSIZE/2


class HuajiManager():
    cd=15 # 生成滑稽的时间间隔

    def __init__(self,master):
        self._master=master
        self.t=0
        self.huajilist=[]

    def generate(self):
        self.t+=1
        if self.t%self.cd==0:
            x=random.randint(0,self._master.get_width()-SMALLSIZE)
            ji=Huaji(self._master,x,0)
            self.huajilist.append(ji)

    def update(self):
        survive=[]
        for huaji in self.huajilist:
            huaji.update()
            if huaji.inWindow() and huaji.lives>0:
                survive.append(huaji)
        self.huajilist=survive

    def draw(self):
        for huaji in self.huajilist:
            huaji.draw()
