import random
import wrap
import time

a=time.time()

def spawn():
    global a
    diaposon = random.randint(20, 480)
    x=random.randint(0, 190)
    cloud = wrap.sprite.add("mario-enemies", diaposon + x, -100, "cloud")
    clouds = {"speed": random.randint(30, 40), "id": cloud, "end": diaposon,"attack_time":random.randint(1,3)}
    return clouds

def move(cloud:dict):
    global a
    wrap.sprite.move(cloud["id"], cloud["speed"], 10)
    x = wrap.sprite.get_x(cloud['id'])
    y = wrap.sprite.get_y(cloud['id'])

    b = time.time()
    c = b - a
    if c >= cloud["attack_time"]:
        ball = wrap.sprite.add("mario-enemies",x, y, 'armadillo_go')
        cloud["attack"] = ball
        a = time.time()

    if 'attack' in cloud.keys():
        wrap.sprite.move(cloud["attack"], 0, 30)

    if x >= cloud["end"] + 200 or x <= cloud["end"]:
        cloud["speed"] = -cloud["speed"]

def remove(cloud):
    wrap.sprite.remove(cloud["id"])
    if 'attack' in cloud.keys():
        wrap.sprite.remove(cloud["attack"])

