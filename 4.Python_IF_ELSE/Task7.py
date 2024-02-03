import math
type=str(input())

if type=="square":
    squareside=float(input())
    squares=squareside*squareside
    print(squares)
elif type=="rectangle":
    rectanglesidea=float(input())
    rectanglesideb=float(input())
    rectangles=rectanglesidea*rectanglesideb
    print(rectangles)
elif type=="circle":
    circler=float(input())
    circles=circler*circler*math.pi
    print(circles)
elif type=="triangle":
    trianglea=float(input())
    triangleh=float(input())
    triangles=0.5*trianglea*triangleh
    print(triangles)
