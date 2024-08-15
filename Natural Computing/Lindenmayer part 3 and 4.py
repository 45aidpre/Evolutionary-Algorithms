import pygame, math
screen = pygame.display.set_mode((600,480))
pygame.display.set_caption("fail")
screen.fill((255,255,255))
pygame.init()

#parts 3 and 4 are uploaded separately, ignore below
class turtle:
    def __init__(self,nf,ng,d,ac):
        self.x = 300
        self.y = 240
        self.a = 0
        self.nf = nf
        self.ng = ng
        self.stack = ""
        self.d = d
        self.ac = ac
        self.pStack = []
    def genStack(self,s,n):
        final = ""
        for i in range(len(s)):
            if s[i] == "F":
                final += self.nf
            elif s[i] == "G":
                final += self.ng
            else:
                final += s[i]
        if n > 0:
            self.genStack(final,n-1)
        else:
            self.stack = final
    def draw(self):
        for i in range(len(self.stack)):
            if self.stack[i] == "F" or self.stack[i] == "G":
                stp = [self.x,self.y]
                self.x += self.d*math.cos(self.a/180*math.pi)
                self.y += self.d*math.sin(self.a/180*math.pi)
                enp = [self.x,self.y]
                pygame.draw.line(screen, (0,0,0), stp, enp)
            elif self.stack[i] == "+":
                self.a += self.ac
            elif self.stack[i] == "-":
                self.a -= self.ac
            elif self.stack[i] == "[":
                self.pStack.append([self.x,self.y,self.a])
            elif self.stack[i] == "]":
                self.x = self.pStack[-1][0]
                self.y = self.pStack[-1][1]
                self.a = self.pStack[-1][2]
                self.pStack[-1:] = []
            pygame.display.update()
a = turtle("FF","F+[[G]−G]−F[−FG]+G",4,22.5)
a.genStack("G",4)
a.draw()

a = turtle("F−−F−−F−−GG","GG",1,60)
a.genStack("F",3)
a.draw()