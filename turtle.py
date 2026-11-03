from turtle import *

# Create and set up Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(0)
tommy.color("forestgreen")

# Point Tommy upwards and move to bottom of screen:
tommy.left(90)
tommy.penup()
tommy.goto(0, -150)
tommy.pendown()

def draw_tree(branch_length):
  y = 2  
  if branch_length < 15:
        return
  tommy.forward(branch_length)
  tommy.left(30)
  draw_tree(branch_length * 0.86)
  tommy.forward(branch_length / y)
  tommy.backward(branch_length / y)
  tommy.right(60)
  draw_tree(branch_length * 0.86)
  tommy.forward(branch_length / y)
  tommy.backward(branch_length / y)
  tommy.left(30)
  tommy.backward(branch_length)

# Start drawing the tree with an initial branch length of 70:
draw_tree(60)

# Write a finish message:
tommy.penup()
tommy.goto(0, -200)
tommy.color("black")
tommy.write("Finish the tree code!", None, "center", "16pt bold")
tommy.goto(0, -230)
