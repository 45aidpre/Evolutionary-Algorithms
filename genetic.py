import random
# Gene class
class geneCode:
    def __init__(self,code):
        self.code = code
        #Single Point Mutation
    def spm(self): 
        sub = int(random.random()*12)
        if self.code[sub] == 0:
            self.code[sub] = 1
        else:
            self.code[sub] = 0
        #Double Point Mutation
    def dpm(self):
        en1 = int(random.random()*12)
        en2 = int(random.random()*12)
        while en2 == en1:
            en2 = int(random.random()*12)
        v1 = self.code[en1]
        v2 = self.code[en2]
        self.code[en1] = v2
        self.code[en2] = v1
    def pr(self):
        print(self.code)
# Crossover function
def crossover(c1,c2):
    en = int(random.random()*12)
    g1s = c1.code[:en]
    g1e = c1.code[en:]
    g2s = c2.code[:en]
    g2e = c2.code[en:]
    sub = []
    sub2 = []
    for i in range(len(g1s)):
        sub.append(g1s[i])
        sub2.append(g2s[i])
    for i in range(len(g2e)):
        sub.append(g2e[i])
        sub2.append(g1e[i])
    return [geneCode(sub),geneCode(sub2)]
#Desired Genetic Makeup
targetCode = [0,1,0,0,1,0,0,1,0,0,1,0]
# Initial population
pop = []
for i in range(8):
    sub = []
    for i in range(12):
        sub.append(int(random.random()*2))
    pop.append(geneCode(sub))
found = False
gen = 0
# Creates new generations until target is found
while not found:
    simDist = []
    for i in range(len(pop)):
        sim = 0
        for j in range(12):
            if pop[i].code[j] == targetCode[j]:
                sim += 1
        simDist.append([i,sim])
    simSort = []
    count = 0
    highest = simDist[0][1]
    highI = 0
    while len(simDist) > 0:
        highest = simDist[0][1]
        highI = 0
        for i in range(len(simDist)):
            if simDist[i][1] > highest:
                highest = simDist[i][1]
                highI = i
        simSort.append(simDist[highI])
        simDist[highI:highI+1] = []
    if simSort[0][1] == 12:
        found = True
    else:
        newPop = []
        for i in range(4):
            child = crossover(pop[simSort[i*2][0]],pop[simSort[i*2+1][0]])
            for j in range(2):
                newPop.append(child[j])
        gen += 1
        for i in range(len(newPop)):
            sub = random.random()
            if sub < 0.01:
                newPop[i].spm()
        pop = newPop
print("achieved in "+str(gen)+" generations")
# Useless roulette function lol roflcopter
def roulette(dist):
    seed = random.random()
    count = 0
    final = 0
    sumDist = []
    sub = 0
    for i in range(len(dist)):
        sumDist.append(sub)
        sub += dist[i]
    sumDist.append(sub)
    while count < len(dist):
        if seed*sub >= sumDist[count] and seed*sub < sumDist[count+1]:
            final = count
        count += 1
    return final
