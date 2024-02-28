import random
import wrap

def spawn():
    diaposon = random.randint(20, 480)
    cloud = wrap.sprite.add("mario-enemies", diaposon + random.randint(0, 190), -100, "cloud")
    clouds = {"speed": random.randint(30, 40), "id": cloud, "end": diaposon}
    return clouds

def move(cloud):
    wrap.sprite.move(cloud["id"], cloud["speed"], 10)
    x = wrap.sprite.get_x(cloud['id'])
    if x >= cloud["end"] + 200 or x <= cloud["end"]:
        cloud["speed"] = -cloud["speed"]

def remove(cloud):
    wrap.sprite.remove(cloud["id"])

