
kopce = [12, 9, 11, 8, 14, 13, 12, 13]
rychlost = 0
chůze = 0

for i in range(len(kopce)): # <0, 8)
    if i == len(kopce)-1:
        break
    tenhle_kopec = kopce[i]
    další_kopec = kopce[i+1]
    if rychlost + tenhle_kopec > další_kopec:
       rychlost += tenhle_kopec - další_kopec
    else:
        chůze += další_kopec - tenhle_kopec
        rychlost = 0

print(chůze)






