import turtle
import math
def defineTurtle(speed: float):
  turtle.colormode(255)
  T=turtle.Turtle()
  T.speed(speed)
  return T
def DrawCircle(radius: float, centered: bool, filled: bool, pen: turtle.Turtle):
  if centered:
    pen.penup()
    pen.goto(0,0)
    pen.right(90)
    pen.forward(radius)
    pen.left(90)
    pen.backward(radius)
    pen.pendown()
  if filled:
    pen.begin_fill()
  pen.circle(radius)
  if filled:
    pen.end_fill()
def DrawRegularPolygon(sides: int, SideLength: float, centered: bool, filled: bool, pen: turtle.Turtle):
  a=SideLength/(2*math.tan(math.pi/sides))
  h=a*2
  print(a,h)
  if centered:
    pen.penup()
    pen.goto(0,0)
    pen.right(90)
    pen.forward(a)
    pen.left(90)
    pen.backward(SideLength/2)
    pen.pendown()
  if filled:
    pen.begin_fill()
  for i in range(sides):
    pen.forward(SideLength)
    pen.left(360/sides)
  if filled:
    pen.end_fill()
def HexToNum(number: str):
  number=number.lower()
  numList=[]
  for i in number:
    numList.append(i)
  n=0
  for i in numList:
    if i == "a":
      numList[n]=10
    elif i == "b":
      numList[n]=11
    elif i == "c":
      numList[n]=12
    elif i == "d":
      numList[n]=13
    elif i == "e":
      numList[n]=14
    elif i == "f":
      numList[n]=15
    else:
      numList[n]=int(i)
    n+=1
  n=0
  for i in range(len(numList)):
    numList[n]=numList[n]*16**(len(numList)-1-i)
    n+=1
  r=0
  for i in numList:
    r+=i
  return r
def Advance(distance: float, pen: turtle.Turtle):
  pen.penup()
  pen.forward(distance)
  pen.pendown()
