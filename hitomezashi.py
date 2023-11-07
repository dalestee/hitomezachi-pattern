from random import *
from turtle import *
import pygame
"""creates a hitomezashi pattern from random 0's and 1's strings or inputs of 0's and 1's"""
def random01(): #returns an 10 characters string of 0's and 1's randoms
    a = ""
    for i in range(0,51):
        a += str(randint(0,1))
    return a

def A_to_0(v): #transforms str into 0 and 1
    st = ""
    for i in v:
        if i in ("A","E","I","O","U","a","e","i","o","u"):
            st += "0"
        else:
            st += "1"
    return st
  
def hitopatt(probL1 = 0.5 ,probL2 = 0.5): #defines hitomezashi pattern, rentre proba(entre 0.0 et 1) que soit 1
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    running = True
    
    v1 =""
    v2= ""
    
    pop = [0,1]
    weights1 = [1-probL1,probL2]
    weights2 = [1-probL1,probL2]
    for i in range(25):
        v1 += str(choices(pop,weights1))
        
    for i in range(25):
        v2 += str(choices(pop,weights2))
    
    def ligne_V_off(coordstart):
        vari = 0
        for i in range(25): #decine ligne vertial off
            pygame.draw.line(screen, (0,0,255), (coordstart,0+vari), (coordstart,10+vari))
            vari += 20
    
    def ligne_V_on(coordstart):
        vari = 0
        for i in range(25): #decine ligne vertial on
            pygame.draw.line(screen, (0,0,255), (coordstart,10+vari), (coordstart,20+vari))
            vari += 20
    
    def ligne_H_off(coordstart):
        vari = 0
        for i in range(25): #decine ligne horizontal off
            pygame.draw.line(screen, (0,0,255), (0+vari,coordstart), (10+vari,coordstart))
            vari += 20
    
    def ligne_H_on(coordstart):
        vari = 0
        for i in range(25): #decine ligne horizontal on
            pygame.draw.line(screen, (0,0,255), (10+vari,coordstart), (20+vari,coordstart))
            vari += 20
    
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        
        if isinstance(v1, str) == True:
            st1 = A_to_0(v1)
        elif isinstance(v2, str) == True:
            st2 = A_to_0(v2)
        esp = 0    
        for i in v1: #draws the v1 line
            esp += 10
            if i == "0":
                ligne_V_off(esp)
            else:
                ligne_V_on(esp)
                
        esp = 0 
        for i in v2: #draws the v2 line
            esp += 10
            if i == "0":
                ligne_H_off(esp)
            else:
                ligne_H_on(esp)
        
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    hitopatt() 