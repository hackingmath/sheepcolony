'''Sheep World with Curtis
April 15, 2017
Peter Farrell'''

from random import choice

WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)

colorList = [WHITE,RED,YELLOW,PURPLE]

grassList = []

class Sheep:
    def __init__(self,x,y,sList,col):
        self.x = x #x-position
        self.y = y #y-position
        self.col = col #color
        self.age = 0
        self.sz = 10 #size
        self.energy = 20 #energy level
        #add it to the sheep list
        sList.append(self)
        
    def update(self):
        #make sheep walk randomly
        move = 10
        if self.col == PURPLE:
            move = 12
        self.x += random(-move, move)
        self.y += random(-move, move)
        self.energy -= 1
        self.age += 1
        
        if self.energy > 50:
            Sheep(self.x,self.y,
                  sheepList,self.col)
            self.energy -= 30
        
        #draw sheep
        fill(self.col)
        ellipse(self.x,
                self.y,
                self.sz, self.sz)
                                
class Patch:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.energy = 2 #energy from eating this patch
        self.eaten = False #hasn't been eaten yet
        self.sz = 10
        
    def update(self):
        if self.eaten:
            if random(100)<5:
                self.eaten = False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x, self.y, self.sz,self.sz)
               
                            
def setup():
    global sheepList,colorList
    size(800,800)
    rectMode(CENTER)
    noStroke()
    patchsize = 10
    sheepList = []
    #rows:
    '''for y in range(int(height/patchsize)):
        sheepList.append([])
        #columns filled with 0's
        for x in range(int(width/patchsize)):
            sheepList[y].append(0)'''
        
    for i in range(10):
        Sheep(random(width),random(height),sheepList,
              choice(colorList))
    for x in range(int(width/patchsize)):
        for y in range(int(height/patchsize)):
            grassList.append(Patch(patchsize*x,
                                   patchsize*y))
    
def draw():
    background(WHITE)
    for g in grassList:
        for s in sheepList:
            #check if there's a sheep on this patch
            if not g.eaten and dist(g.x,
                    g.y,
                    s.x,
                    s.y)<10:
                g.eaten = True
                s.energy += g.energy
        g.update()
    for s in sheepList:
        s.update()
        if s.energy <= 0 or s.age > 100: 
            sheepList.remove(s)
    