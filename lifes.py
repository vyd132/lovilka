import wrap

lifes=[]

def spawn():
    for life in range(0,96,32):
        platform_lives= wrap.sprite.add("mario-items", 650, 50+life, "moving_platform1")
        lifes.append(platform_lives)

def remove():
    wrap.sprite.remove(lifes[len(lifes) - 1])
    lifes.remove(lifes[len(lifes) - 1])