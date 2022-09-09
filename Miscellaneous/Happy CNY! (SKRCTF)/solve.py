import os
path = "C:/Users/User/Downloads/Angpows/Angpow"

for i in range(1,41):
    sum = 0
    for filename in os.listdir(path + str(i)):
        folder = "Angpow" + str(i) + "/"
        path2 = "C:/Users/User/Downloads/Angpows/" + folder + filename
        size = os.stat(path2).st_size
        
        if size == 121993:
            sum += 50
        elif size == 110306:
            sum += 20
        elif size == 114820:
            sum += 10
        elif size == 125945:
            sum += 5
        elif size == 132199:
            sum += 1
    print(sum)