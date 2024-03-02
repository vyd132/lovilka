import wrap
import random

def spawn():
    x= random.randint(100, 600)
    straw=wrap.sprite.add("pacman",x,-100,random.choice(["item_strawberry","item_apple","item_cherry"]))
    strawberry = {"speed": random.randint(10,50),"id":straw}
    number=wrap.sprite.add_text(str(strawberry["speed"]),x,-110,text_color=[255,255,255])
    strawberry["text"]=number
    return strawberry

def move(for_el):
    wrap.sprite.move(for_el["id"], 0, for_el["speed"])
    wrap.sprite.move(for_el["text"], 0, for_el["speed"])

def remove(for_el):
    wrap.sprite.remove(for_el["id"])
    wrap.sprite.remove(for_el["text"])