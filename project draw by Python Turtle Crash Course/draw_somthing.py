import turtle

car_coordinates = [
    (-50, -25),  # Bottom left of car body
    (-50, 25),   # Top left of car body
    (50, 200),    # Top right of car body
    (50, -25),   # Bottom right of car body
    (-30, 25),   # Top left of car roof
    (70, 25),    # Top right of car roof
    (-30, 250),   # Front left of car roof
    (30, 50),    # Front right of car roof
    (-50, -25),  # Bottom left of front wheel
    (-100, -25),  # Bottom right of front wheel
    (25, -250),   # Bottom right of rear wheel
    (250, -25)    # Bottom left of rear wheel
      
]




turtle.hideturtle()
turtle.bgcolor("red")
turtle.setup(500,600)

start_play = (0,-25)
turtle.speed(1)

def draw_car(coredinate,start):
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for i in range(len(coredinate)):
        x = coredinate[i]
        turtle.goto(x)
    turtle.end_fill()    
draw_car(car_coordinates,start_play)

