import turtle
from random import randrange
import time

f_name = lambda f_name: os.path.realpath(os.path.join(os.getcwd(), f_name)).replace('\\', '/')



# reverse string
def str_rev(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + str_rev(string[:len(string) - 1])

def palindromVerif(string):
    return string.replace(" ", "").lower() == str_rev(string).replace(" ", "").lower()




#Koch snowflake

def kochSide(turtle, length, depth):
    if (depth == 0):
        turtle.forward(length)
    else:
        kochSide(turtle, length/3.0, depth-1)
        turtle.right(60)
        kochSide(turtle, length/3.0, depth-1)
        turtle.left(120)
        kochSide(turtle, length/3.0, depth-1)
        turtle.right(60)
        kochSide(turtle, length/3.0, depth-1)

def kochSnowflake(turtle, length, recursionDepth):
    for step in range(3):
        kochSide(turtle, length,recursionDepth)
        turtle.left(120)

def kochSnowMain():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myTurtle.penup()
    myTurtle.goto(-200, -100)
    myTurtle.setheading(0)
    myTurtle.pendown()
    turtle.delay(0)
    myTurtle.speed(10)

    kochSnowflake(myTurtle, 400, 5)
    myWin.exitonclick()




#1Factorial
def factor(num):
    if num < 1:
        return 1
    return num * factor(num-1)



#2List reverse
def lst_rev(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + lst_rev(lst[0:-1])



#3Maze
def mainMaze(path):
    location = []  # list to hold the location we are at in the maze
    hasNoEnd = True

    with open(path, 'r') as infile:
        maze = [list(row) for row in infile.read().splitlines()]

    for y in range(0, len(maze)):
        for x in range(0, len(maze[y])):
            if maze[y][x] == 'S':
                location = [y, x]
            elif maze[y][x] == 'E':
                hasNoEnd = False
    if len(location) == 0:
        raise Exception("No start cell")
    if hasNoEnd:
        raise Exception("Maze has no end")

    tick(maze, location[0], location[1])
    print("\n\n")
    print('\n'.join(''.join(row) for row in maze))

#Recursive method which solves the maze.
def tick(maze, y, x):
    if maze[y][x] in (' ', 'S'):
        maze[y][x] = 'x'
        # check right, down, left, up
        if (tick(maze, y, x + 1) or tick(maze, y - 1, x) or tick(maze, y, x - 1) or tick(maze, y + 1, x)):
            maze[y][x] = '.'
            return True
    elif maze[y][x] == 'E':
        return True
    return False





def hilbert(turt, level, angle, case, size = 5):
    if level == 0:
        return
    turt.color("Blue")
    turt.speed(15)

    if case == 0:
        turt.left(angle)
        hilbert(turt, level - 1, angle, 1)
        turt.forward(size)
        turt.right(angle)
        hilbert(turt, level - 1, angle, 0)
        turt.forward(size)
        hilbert(turt, level - 1, angle, 0)
        turt.right(angle)
        turt.forward(size)
        hilbert(turt, level - 1, angle, 1)
        turt.left(angle)

    elif case == 1:
        turt.right(angle)
        hilbert(turt, level - 1, angle, 0)
        turt.forward(size)
        turt.left(angle)
        hilbert(turt, level - 1, angle, 1)
        turt.forward(size)
        hilbert(turt, level - 1, angle, 1)
        turt.left(angle)
        turt.forward(size)
        hilbert(turt, level - 1, angle, 0)
        turt.right(angle)







#Fibonachi
fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1

def fib_1(n):
    if n <= 2:
        return 1
    else:
        return fib_1(n-1) + fib_1(n-2)

def fib_2(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

def time_estimator(fib_method, num):
    start = time.time()
    for i in range(num):
        print(fib_method(i))
    end = time.time()
    print("Time elapsed: ", end - start)





#PASCAL TRIANGLE
def pascal_triangle(n, lst=None):
    if lst == None:
        lst = [1]
    if n > 1:
        new = [1] + [sum(i) for i in zip(lst[:-1], lst[1:])] +[1]
        print str(new)[1:-1]
        pascal_triangle(n-1, new)





if __name__ == "__main__":
    print("check palindrom")
    print(palindromVerif("Wassamassaw  a town in South Dakota"))
    print(palindromVerif("Able was I ere I saw Elba"))
    print("\n")

    print("draw koch snow")
    kochSnowMain()
    print("\n")

    print("factorial")
    print(factor(5))
    print("\n")

    print("list reverse")
    print(lst_rev([1, 2, 3]))
    print("\n")

    print("MAZE")
    mainMaze(f_name("maze.txt"))
    print("\n")

    print("draw hilbert curve")
    myWin = turtle.Screen()
    t = turtle.Turtle()
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    hilbert(t, 5, 90, 0)
    myWin.exitonclick()
    print("\n")


    print("fibonachi")
    print(fib(10))
    print(fib_1(10))
    print(fib_2(10))
    print("\n")

    #time_estimator(fib, 200)
    #time_estimator(fib_1, 200)
    #time_estimator(fib_2, 200)

    print("pascale triangle")
    pascal_triangle(7)

