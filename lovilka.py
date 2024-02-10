import wrap
import random

height=700
width=700
wrap.world.create_world(width, height)

fruits=[]

platform = wrap.sprite.add("mario-items", 30, 600, "moving_platform1")

@wrap.always(1000)
def fruits_spawn():
    fruit= wrap.sprite.add("pacman",random.randint(100,600),-100,random.choice(["item_apple","item_cherry","item_strawberry"]))
    fruits.append(fruit)

@wrap.always()
def fruits_move():
    for f_move in fruits:
        wrap.sprite.move(f_move,0,50)

@wrap.on_mouse_move
def platform_move(pos_x):
    wrap.sprite.move_to(platform,pos_x,600)

@wrap.always()
def fruits_click():
    for f_col in fruits:
        res= wrap.sprite.is_collide_sprite(f_col,platform)
        if res:
            wrap.sprite.remove(f_col)
            fruits.remove(f_col)



import wrap_py
wrap_py.app.start()