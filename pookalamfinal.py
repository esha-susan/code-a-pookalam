
import turtle

screen = turtle.Screen()

screen.bgcolor("white")  

t = turtle.Turtle()

t.speed(0)  
t.penup()
t.goto(0,-225)
t.pendown()
t.fillcolor(" brown")
t.begin_fill()
t.circle(254)
t.end_fill()



t.penup()

t.goto(115, -54)  

t.pendown()

#To draw the star

def draw_star(turtle, size):

    turtle.begin_fill()  

    for _ in range(16):  

        turtle.forward(size)

        turtle.left(135)  
        turtle.forward(size)

        turtle.right(135)  

        turtle.left(22.5) 

    turtle.end_fill() 
t.penup()
t.goto(145,-70)
t.pendown()
t.fillcolor('red')
draw_star(t,90)
t.penup()
t.goto(125,-60)
t.pendown()
t.fillcolor('dark orange')
draw_star(t,80)

t.penup()
t.goto(110,-50)
t.pendown()
t.fillcolor('gold')
draw_star(t,70)
t.penup()
t.goto(95,-40)
t.pendown()
t.fillcolor("white")
draw_star(t,60)
t.fillcolor("dark green")
t.penup()
t.goto(80,-30)
t.pendown()
draw_star(t,50)  

t.penup()

t.goto(0,-70)

t.pendown()

t.fillcolor('gold')

t.begin_fill()

t.circle(90)

t.end_fill()

t.penup()

t.goto(0,20)

t.pendown()

# To draw the petals
def draw_petal(size, color):

    t.fillcolor(color)

    t.begin_fill()
    t.circle(size, 60)  
    t.left(120) 
    t.circle(size, 60)
    t.left(120) 
    t.end_fill()


for _ in range(18):
    draw_petal(80, 'red') 
    t.left(20)


for _ in range(12): 
    draw_petal(70, ' dark orange')
    t.left(30)


for _ in range(18): 
    draw_petal(60, "gold")  
    t.left(20) 



for _ in range(12): 
    draw_petal(50, "white")  
    t.left(30)  

t.hideturtle()

turtle.done()