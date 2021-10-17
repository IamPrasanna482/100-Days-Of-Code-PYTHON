import colorgram

#extract 10 colors from an image
# colors=colorgram.extract('paint.jpg',30)


# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

max=t.Turtle()
t.colormode(255)
max.ht()
color_list=[(246, 244, 241), (237, 241, 247), (241, 246, 243), (247, 241, 243), (135, 164, 199), (222, 151, 106), (31, 43, 63), (199, 137, 148), (158, 62, 52), (235, 212, 93), (50, 100, 140), (137, 180, 162), (147, 64, 72), (158, 32, 28), (50, 40, 44), (58, 49, 46), (62, 114, 99), (169, 28, 33), (228, 165, 170), (234, 168, 159), (209, 84, 73), (34, 60, 54), (15, 96, 71), (194, 99, 107), (172, 189, 219), (35, 61, 104), (109, 126, 157), (17, 82, 105), (175, 201, 190), (39, 149, 205)]
max.speed(1000)
max.penup()
max.setheading(225)
max.forward(300)
max.setheading(0)
no_of_dots=100


for i in range(1,no_of_dots+1):
    max.dot(20,random.choice(color_list))
    max.forward(50)
    if i%10==0:
        max.setheading(90)
        max.forward(50)
        max.setheading(180)
        max.forward(500)
        max.setheading(0)


myscreen=t.Screen()
myscreen.exitonclick()
