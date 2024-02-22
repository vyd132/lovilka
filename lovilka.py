import wrap
import random

height=700
width=700
wrap.world.create_world(width, height)

fruits=[]
lifes=[]

platform = wrap.sprite.add("mario-items", 30, 600, "moving_platform1")
platform = wrap.sprite.add("mario-items", 30, 600, "moving_platform1")
platform = wrap.sprite.add("mario-items", 30, 600, "moving_platform1")

for life in range(0,96,32):
    platform_lives= wrap.sprite.add("mario-items", 650, 50+life, "moving_platform1")
    lifes.append(platform_lives)


@wrap.always(1000)
def fruits_spawn():
    fruit= wrap.sprite.add("pacman",random.randint(100,600),-100,random.choice(["item_apple","item_cherry","item_strawberry"]))
    fruits.append(fruit)


@wrap.always()
def fruits_move():
    for f_move in fruits.copy():
        wrap.sprite.move(f_move,0,50)
        res = wrap.sprite.is_collide_sprite(f_move, platform)
        if res:
            wrap.sprite.remove(f_move)
            fruits.remove(f_move)
            continue
        y = wrap.sprite.get_y(f_move)
        if y >= 750:
            fruits.remove(f_move)
            wrap.sprite.remove(f_move)
            if len(lifes)==0:
                continue
            wrap.sprite.remove(lifes[len(lifes)-1])
            lifes.remove(lifes[len(lifes)-1])



@wrap.on_mouse_move
def platform_move(pos_x):
    wrap.sprite.move_to(platform,pos_x,600)





import wrap_py
wrap_py.app.start()