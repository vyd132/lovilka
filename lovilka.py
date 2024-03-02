import wrap
import random
import clouds as cloud_mod, fruits as fruit_mod, lifes as life_mod




height=700
width=700
wrap.world.create_world(width, height)

fruits=[]
clouds=[]
spicok_c=[]



platform = wrap.sprite.add("mario-items", 30, 600, "moving_platform1")
platform = wrap.sprite.add("mario-items", 30, 600, "moving_platform1")
platform = wrap.sprite.add("mario-items", 30, 600, "moving_platform1")



life=life_mod.spawn()




@wrap.always(1000)
def fruits_spawn():
    straw=fruit_mod.spawn()
    fruits.append(straw)
    print(fruits)

@wrap.always(3000)
def cloud_spawn():
    chanse = random.randint(1, 100)
    if chanse >= 1 or chanse <= 100:
        cloud= cloud_mod.spawn()
        spicok_c.append(cloud)




def y_check(spicok,for_el,comand):
    y = wrap.sprite.get_y(for_el["id"])
    if y >= 600:
        spicok.remove(for_el)
        comand.remove(for_el)



@wrap.always()
def cloud_move():
    for c_move in spicok_c.copy():
        cloud_mod.move(c_move)
        res = wrap.sprite.is_collide_sprite(c_move["id"], platform)
        if res:
            cloud_mod.remove(c_move)
            spicok_c.remove(c_move)
            life_mod.remove()
            continue
        y_check(spicok_c,c_move,cloud_mod)




@wrap.always()
def fruits_move():
    for f_move in fruits.copy():
        fruit_mod.move(f_move)
        res = wrap.sprite.is_collide_sprite(f_move["id"], platform)
        if res:
            fruit_mod.remove(f_move)
            fruits.remove(f_move)
            continue
        y_check(fruits,f_move,fruit_mod)



@wrap.on_mouse_move
def platform_move(pos_x):
    wrap.sprite.move_to(platform,pos_x,600)





import wrap_py
wrap_py.app.start()