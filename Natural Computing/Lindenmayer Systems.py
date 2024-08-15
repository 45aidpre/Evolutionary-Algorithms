#import pygame, math
#screen = pygame.display.set_mode((600,480))
#pygame.display.set_caption("fail")
#screen.fill((255,255,255))
#pygame.init()

#part 1
def step(s,n):
    final = ""
    for i in range(len(s)):
        if s[i] == "a":
            final += "c"
        elif s[i] == "b":
            final += "ac"
        else:
            final += "b"
    if n > 0:
        step(final,n-1)
    else:
        print(final)
print("p1")
step("c",9)

#part 2
def stepAC(s,n):
    final = ""
    for i in range(len(s)):
        if s[i] == "a":
            final += "bc"
        elif s[i] == "b":
            final += "da"
        elif s[i] == "c":
            final += "a"
        else:
            final += "b"
    print(final,"\n")
    if n > 0:
        stepAC(final,n-1)
print("p2")
#stepAC("a",10)










    