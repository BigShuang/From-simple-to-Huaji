import pygame
import sys
from plane import Plane
from huaji import HuajiManager

COLORS={
    "bg":(0, 0, 0) # 背景颜色
}

FPS=60 # 游戏帧率
WINWIDTH = 600  # 窗口宽度
WINHEIGHT = 900  # 窗口高度
MOVESTEP=5  # 移动速度

pygame.init() # pygame初始化，必须有，且必须在开头
# 创建主窗体
clock=pygame.time.Clock() # 用于控制循环刷新频率的对象
win=pygame.display.set_mode((WINWIDTH,WINHEIGHT))

plane=Plane(win,200,600)
hm=HuajiManager(win)
mx,my=0,0 # 记录移动方向
while True:
    win.fill(COLORS["bg"])

    # 获取所有事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 判断当前事件是否为点击右上角退出键
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT or event.key == ord('a'):
                mx=-1
            if event.key==pygame.K_RIGHT or event.key == ord('d'):
                mx=1
            if event.key==pygame.K_UP  or event.key == ord('w'):
                my=-1
            if event.key==pygame.K_DOWN  or event.key == ord('s'):
                my=1

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key == ord('a'):
                if mx==-1:
                    mx=0
            if event.key==pygame.K_RIGHT or event.key == ord('d'):
                if mx==1:
                    mx=0
            if event.key==pygame.K_UP  or event.key == ord('w'):
                if my==-1:
                    my=0
            if event.key==pygame.K_DOWN  or event.key == ord('s'):
                if my==1:
                    my=0

    plane.check_all_hit(hm.huajilist)
    plane.check_crash(hm.huajilist)

    if plane.lives<=0:
        break

    hm.generate()
    hm.update()
    hm.draw()

    plane.move(mx*MOVESTEP,my*MOVESTEP)
    plane.draw()

    plane.fire()
    plane.update_bullets()
    plane.draw_bullets()

    clock.tick(FPS) # 控制循环刷新频率,每秒刷新FPS对应的值的次数
    pygame.display.update()