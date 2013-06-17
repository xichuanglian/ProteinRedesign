import random

# rotamer library
fout = open('rotamerLibrary', 'w')

num = 10
fout.write("%d\n" % num)

rotamerLib = []
for x in range(0, 10):
    numRot = random.randrange(2,5,1)
    rotamerLib.append(numRot)
    fout.write("%d " % numRot)

fout.close()

# print rotamerLib

# energy table
fout = open('energyTable', 'w')
length = num * (num-1)
fout.write("%d\n" % num)


for x in range(0, num):
    for y in range(0, num):
        if x >= y: continue

        # output (x, y)
        fout.write("%d %d " %(x, y))

        energyTab = [[0 for i in range(rotamerLib[y])] for i in range (rotamerLib[x])]
        for i in range (0, rotamerLib[x]):
            for j in range (0, rotamerLib[y]):
                energy = -random.random()*100
                energyTab[i][j] = energy
                fout. write("%f " % energy)

        fout.write("\n")

        # output (y, x)
        fout.write("%d %d " %(y, x))

        for i in range (0, rotamerLib[y]):
            for j in range (0, rotamerLib[x]):
                fout. write("%f " % energyTab[j][i])

        fout.write("\n")

fout.close()


