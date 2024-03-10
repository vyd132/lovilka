import wrap
import random
import time

a=time.time()

def spawn(x,y):
    global a
    b = time.time()
    c = b - a
    if c >= random.randint(1,4):
        ball = wrap.sprite.add("mario-enemies", x, y, 'armadillo_go')
        armadillo={"id":ball,"speed":random.randint(30,40)}
        a = time.time()
        return armadillo

def move(for_el):
    wrap.sprite.move(for_el["id"], 0,for_el["speed"])


def remove(for_el):
    wrap.sprite.remove(for_el["id"])