import turtle
def draw_flower():
    window = turtle.Screen()
    window.bgcolor('white')
   
    flower = turtle.Turtle()
    flower.shape('turtle')
    flower.fill(True)
    flower.color("blue")
    flower.fillcolor("magenta")
    flower.speed(0)
    
    i = 0
    while i < 50:
        flower.left(130)
        flower.forward(100)
        flower .right(60)
        flower.forward(100)
        flower.right(127)
        flower.forward(100)
        flower.right(60)
        flower.forward(100)
        i += 1
    flower.right(0)
    flower.forward(250)
    
    window.exitonclick()
draw_flower()  
