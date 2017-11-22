import turtle
import math
alex = turtle.Turtle()
bob = turtle.Turtle()
alice = turtle.Turtle()
may= turtle.Turtle()
juice = turtle.Turtle()
black = turtle.Turtle()
fish = turtle.Turtle()

bob.shape("circle")
bob.color("yellow")
bob.pu()
bob.goto(50,0)
bob.pd()

t = [alex,alice,may,juice,black,fish]
colors= ['red','blue','green','black','grey','orange']
ax = [90,120,200,230,300,400]
bx = [70,100,170,200,220,300]

for f in range(0,len(t)):
    t[f].shape("circle")
    t[f].color(colors[f])
    t[f].pu()
    t[f].goto(ax[f],0)
    t[f].pd()
    

for u in range(1000):
    for x in range(100000):
        for i in range(0,len(t)):
            currx = ax[i]*math.cos(x/(100*(i+1)))
            y = bx[i]*math.sin(x/(100*(i+1)))
            t[i].goto(currx,y)
    for m in range(100000):
        for n in range(0,len(t)):
            currm = math.cos(m/(100*(m+1)))*ax[n]
            ym = -(bx[n]*math.sin(m/(100*(m+1))))
            t[n].goto(-currm,ym)
        

turtle.mainloop()
   
