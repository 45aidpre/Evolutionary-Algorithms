from math import cos, sin, radians
import random

def fl(a, b, c, d):
    # Function to simulate drawing a Bezier curve
    pass

sig = 0  # angle variance
mig = 0  # length variance

class Turtle:
    def __init__(self, nf, ng, d, ac, start, it):
        self.x = 0
        self.y = 0
        self.a = 90
        self.nf = nf
        self.ng = ng
        self.stack = ""
        self.d = d
        self.ac = ac
        self.pStack = []
        self.start = start
        self.it = it
    
    def genStack(self, s, n):
        final = ""
        for i in range(len(s)):
            if s[i] == "F":
                final += self.nf
            elif s[i] == "G":
                final += self.ng
            else:
                final += s[i]
        if n == 0:
            self.stack = final
        else:
            self.genStack(final, n - 1)
    
    def path(self, c=0):
        self.x = 0
        self.y = 0
        for i in range(len(self.stack)):
            if self.stack[i] == "F" or self.stack[i] == "G":
                stp = [self.x, self.y]
                self.x += (self.d) * cos(radians(self.a))
                self.y += (self.d) * sin(radians(self.a))
                enp = [self.x, self.y]
                fl(stp[0], stp[1], enp[0], enp[1])
            elif self.stack[i] == "+":
                self.a += self.ac
            elif self.stack[i] == "-":
                self.a -= self.ac
            elif self.stack[i] == "[":
                self.pStack.append([self.x, self.y, self.a])
            elif self.stack[i] == "]":
                self.x = self.pStack[-1][0]
                self.y = self.pStack[-1][1]
                self.a = self.pStack[-1][2]
                self.pStack.pop()

class WindTurtle(Turtle):
    def __init__(self, nf, ng, d, ac, start, it):
        super().__init__(nf, ng, d, ac, start, it)
        self.al = [[], []]
        self.af = 0
        self.ag = 0

    def genStack(self, s, n):
        final = ""
        for i in range(len(s)):
            if s[i] == "F":
                final += self.nf
                self.al[0].append(random.uniform(-1, 1))
            elif s[i] == "G":
                final += self.ng
                self.al[1].append(random.uniform(-1, 1))
            else:
                final += s[i]
        if n == 0:
            self.stack = final
        else:
            self.genStack(final, n - 1)

    def path(self, c):
        self.x = 0
        self.y = 0
        self.a = 90
        self.af = 0
        self.ag = 0
        for i in range(len(self.stack)):
            if self.stack[i] == "F" or self.stack[i] == "G":
                stp = [self.x, self.y]
                if self.stack[i] == "F":
                    self.x += (self.d) * cos(radians(self.a + self.al[0][self.af] * 0))
                    self.y += (self.d) * sin(radians(self.a + self.al[0][self.af] * 0))
                    self.af += 1
                elif self.stack[i] == "G":
                    self.x += (self.d) * cos(radians(self.a + self.al[1][self.ag] * 0))
                    self.y += (self.d) * sin(radians(self.a + self.al[1][self.ag] * 0))
                    self.ag += 1
                enp = [self.x, self.y]
                fl(stp[0], stp[1], enp[0], enp[1])
            elif self.stack[i] == "+":
                self.a += self.ac + self.al[0][self.af] * c
            elif self.stack[i] == "-":
                self.a -= self.ac + self.al[0][self.af] * c
            elif self.stack[i] == "[":
                self.pStack.append([self.x, self.y, self.a])
            elif self.stack[i] == "]":
                self.x = self.pStack[-1][0]
                self.y = self.pStack[-1][1]
                self.a = self.pStack[-1][2]
                self.pStack.pop()

class DecayTurtle(WindTurtle):
    pass

class VaryTurtle(Turtle):
    pass

def draw():
    pass

