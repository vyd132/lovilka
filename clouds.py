import random
import wrap
import time



def spawn():
    diaposon = random.randint(20, 480)
    x=random.randint(0, 190)
    cloud = wrap.sprite.add("mario-enemies", diaposon + x, -100, "cloud")
    clouds = {"speed": random.randint(2, 3), "id": cloud, "end": diaposon,"attack_time":random.randint(1,4),"start":time.time()}
    timer=wrap.sprite.add_text(str(clouds["attack_time"]),diaposon + x,-120,text_color=[255,255,255])
    clouds["text"]=timer
    return clouds

def move(cloud:dict):
    wrap.sprite.move(cloud["id"], cloud["speed"], 2)
    wrap.sprite.move(cloud["text"], cloud["speed"], 2)
    x = wrap.sprite.get_x(cloud['id'])
    if x >= cloud["end"] + 200 or x <= cloud["end"]:
        cloud["speed"] = -cloud["speed"]
    b = time.time()
    c = b - cloud["start"]
    cloud["start"]=time.time()
    cloud["attack_time"] -= c
    wrap.sprite_text.set_text(cloud["text"],str(int(cloud["attack_time"])))
    print("work")

def remove(cloud):
    wrap.sprite.remove(cloud["id"])
    wrap.sprite.remove(cloud["text"])

