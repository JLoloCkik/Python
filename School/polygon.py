import turtle
import math

n = int(input("Add meg a szögek számát: "))
t = int(input("Add meg a lépéseket: "))
r = 80
m =(n*(n-3)/2) / 2
angle = (n - 2) * 180 / n

def draw(n, t):
    tur = turtle.Turtle()
    tur.speed(1)
    
    points = []
    
  
    for i in range(n): 
        tur.forward(r)
        tur.right(360 / n)
        points.append(tur.position()) 
    # end

    tur.penup()
    tur.goto(points[0])
    tur.pendown()
    
    next_index = 0
    
    for i in range(n): 
        next_index = (next_index + t) % n
        tur.goto(points[next_index])
        
    turtle.done()
    # end       
# end           
            
print(m)
draw(n, t)
