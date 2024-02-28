import wrap
import random
import clouds as cloud_mod



height=700
width=700
wrap.world.create_world(width, height)

fruits=[]
lifes=[]
clouds=[]
spicok_c=[]



platform = wrap.sprite.add("mario-items", 30, 600, "moving_platform1")
platform = wrap.sprite.add("mario-items", 30, 600, "moving_platform1")
platform = wrap.sprite.add("mario-items", 30, 600, "moving_platform1")



for life in range(0,96,32):
    platform_lives= wrap.sprite.add("mario-items", 650, 50+life, "moving_platform1")
    lifes.append(platform_lives)


@wrap.always(1000)
def fruits_spawn():
    straw=wrap.sprite.add("pacman",random.randint(100,600),-100,random.choice(["item_strawberry","item_apple","item_cherry"]))
    strawberry = {"speed": random.randint(10,50)}
    strawberry["id"]=straw
    fruits.append(strawberry)
    print(fruits)

@wrap.always(3000)
def cloud_spawn():
    chanse = random.randint(1, 100)
    if chanse >= 1 or chanse <= 100:
        cloud= cloud_mod.spawn()
        spicok_c.append(cloud)




def y_check(spicok,for_el):
    y = wrap.sprite.get_y(for_el["id"])
    if y >= 750:
        spicok.remove(for_el)
        wrap.sprite.remove(for_el["id"])


@wrap.always()
def cloud_move():
    for c_move in spicok_c.copy():
        cloud_mod.move(c_move)
        res = wrap.sprite.is_collide_sprite(c_move["id"], platform)
        if res:
            cloud_mod.remove(c_move)
            spicok_c.remove(c_move)
            wrap.sprite.remove(lifes[len(lifes) - 1])
            lifes.remove(lifes[len(lifes) - 1])
            continue
        y_check(spicok_c,c_move)




@wrap.always()
def fruits_move():
    for f_move in fruits.copy():
        wrap.sprite.move(f_move["id"],0,f_move["speed"])
        res = wrap.sprite.is_collide_sprite(f_move["id"], platform)
        if res:
            wrap.sprite.remove(f_move["id"])
            fruits.remove(f_move)
            continue
        y_check(fruits,f_move)





@wrap.on_mouse_move
def platform_move(pos_x):
    wrap.sprite.move_to(platform,pos_x,600)





import wrap_py
wrap_py.app.start()