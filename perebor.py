chisla=[1,1,8,3,6,2,2]
copys= chisla.copy()
for dellete in copys:
    if dellete<4:
        chisla.remove(dellete)

print(chisla)