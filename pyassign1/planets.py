Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
alex = turtle.Turtle()
bob = turtle.Turtle()
alice = turtle.Turtle()
may= turtle.Turtle()
juice = turtle.Turtle()
black = turtle.Turtle()
fish = turtle.Turtle()

bob.shape("circle")
bob.color("yellow")
bob.goto(50,0)

t = [alex,alice,may,juice,black,fish]
colors= ['red','blue','green','black','grey','orange']
ax = [100,180,300,230,200,400]
bx = [100,150,350,200,120,300]

for f in range(0,len(t)):
    t[f].shape("circle")
    t[f].color(colors[f])
    t[f].pu()
    t[f].goto(-ax[f],0)
    t[f].pd()
    


for u in range(1000):
    for x in range(-100,101):
        for i in range(0,len(t)):
            currx = x/100*ax[i]
            y = (bx[i]**2-bx[i]**2/ax[i]**2*currx**2)**(1/2)
            t[i].goto(currx,y)
    for m in range(-100,101):
        for n in range(0,len(t)):
            currm = m/100*ax[n]
            ym = -(bx[n]**2-bx[n]**2/ax[n]**2*currm**2)**(1/2)
            t[n].goto(-currm,ym)
        

turtle.mainloop()
   
