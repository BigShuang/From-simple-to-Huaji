#usr/bin/env python
#-*- coding:utf-8- -*-
import pygame
import math
PLANEIMG="img/huaplane.png"
PLANESIZE=90 # 飞机对象直径（近似圆形）

class Plane():
    firedelay=15 # 发射子弹时间间隔

    def __init__(self,master,x,y,img_path=PLANEIMG):
        self._master=master # 父控件
        self.image=pygame.image.load(img_path) # 飞机图像
        # 飞机位置-坐标
        self.x=x
        self.y=y
        self.lives=1
        self.t=0
        self.bullets=[] # 发射的子弹

    # 移动飞机
    def move(self,x,y):
        if 0<=self.x+PLANESIZE/2+x<=self._master.get_width():
            self.x+=x
        if 0<=self.y+PLANESIZE/2+y<=self._master.get_height():
            self.y+=y

    # 绘制飞机
    def draw(self):
        self._master.blit(self.image,(self.x,self.y))

    # 发射子弹
    def fire(self):
        self.t+=1
        if self.t>=self.firedelay:
            self.t=0
            # 子弹初始坐标
            bx=self.x+int(self.image.get_width()/2)
            by=self.y
            bullet=Bullet(self._master,bx,by)
            self.bullets.append(bullet)

    # 更新子弹位置，清除失效的子弹
    def update_bullets(self):
        survive=[]
        for b in self.bullets:
            b.update()
            if b.on:
                survive.append(b)
        self.bullets=survive

    # 绘制子弹
    def draw_bullets(self):
        for b in self.bullets:
            b.draw()

    def check_all_hit(self,huajilist):
        survive=[]
        for b in self.bullets:
            b.check_hit(huajilist)
            if b.on:
                survive.append(b)
        self.bullets=survive

    def get_distance(self,xy):
        x,y=xy
        cx=self.x+PLANESIZE/2
        cy=self.y+PLANESIZE/2
        return math.sqrt(math.pow(cx-x,2)+math.pow(cy-y,2))

    def check_crash(self,huajilist):
        for huaji in huajilist:
            if huaji.lives>0 and huaji.inWindow():
                d=self.get_distance(huaji.get_center_XY())
                if d<=PLANESIZE/2+huaji.get_radius():
                    # hit
                    self.lives-=1
                    huaji.lives-=1

class Bullet():
    speed=2 # 速度
    color=(255,0,0) # 颜色
    radius=5 # 半径

    def __init__(self,master,x,y):
        self._master=master # 父控件
        self.x=x
        self.y=y
        self.on=True # 记录子弹状态，初始为True，子弹失效（超出边界或者碰到敌机）时为False

    # 更新子弹位置，移动子弹
    def update(self):
        self.y-=self.speed

        if self.y<=0:
            self.on=False

    # 绘制飞机
    def draw(self):
        pygame.draw.circle(self._master, self.color, (self.x,self.y), self.radius,2)

    def get_distance(self,xy):
        x,y=xy
        return math.sqrt(math.pow(self.x-x,2)+math.pow(self.y-y,2))

    def check_hit(self,huajilist):
        if not self.on:
            return
        for huaji in huajilist:
            if huaji.lives>0 and huaji.inWindow():
                d=self.get_distance(huaji.get_center_XY())
                if d<=huaji.get_radius():
                    # hit
                    self.on=False
                    huaji.lives-=1


