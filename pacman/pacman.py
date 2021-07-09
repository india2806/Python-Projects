import turtle
import random
import time

lives = 3
score = 0

window = turtle.Screen()
window.tracer(0)
window.title("Pac-man")
window.bgcolor('black')
window.setup(600,600)

pacman = turtle.Turtle()
pacman.speed(0)
pacman.penup()
pacman.color('yellow')
pacman.shape('circle')
#pacman movement
pacman.direction = 'stop'

enemies = []
for x in range(10):
    enemy = turtle.Turtle()
    enemy.color('red')
    enemy.penup()
    enemy.shape('turtle')
    enemy.speed = 0.5
    x = random.randint(-280,280)
    y = random.randint(-280,280)
    enemy.setposition(x,y)
    enemies.append(enemy)


pen = turtle.Turtle()
pen.speed(0)
pen.color('blue')
pen.penup()
pen.goto(0,245)
pen.pendown()
pen.write("Score : {} Lives : {}".format(score,lives), align='center', font=('Courier',36))
pen.hideturtle()

foods = []
for _ in range(40):
    food = turtle.Turtle()
    food.speed(0)
    food.penup()
    food.color("orange")
    food.shape("circle")
    food.shapesize(stretch_wid=0.4, stretch_len=0.4)
    x = random.randint(-280,280)
    y = random.randint(-280,280)
    food.setposition(x,y)
    foods.append(food)

def movement():
    if pacman.direction == 'up':
        y = pacman.ycor()
        y += 5
        pacman.sety(y)

    if pacman.direction == 'down':
        y = pacman.ycor()
        y -= 5
        pacman.sety(y)   

    if pacman.direction == 'left':
        x = pacman.xcor()
        x -= 5
        pacman.setx(x)

    if pacman.direction == 'right':
        x = pacman.xcor()
        x += 5
        pacman.setx(x)

#enemy movement
def enemyMovement():
    #make the enemies move
    for enemy in enemies:
        y = enemy.ycor()
        x = enemy.xcor()
        y += enemy.speed
        x += enemy.speed
        enemy.sety(y)
        enemy.setx(x)          

#window binding function
def moveUp():
    pacman.direction = 'up'
def moveDown():
    pacman.direction = 'down'
def moveLeft():
    pacman.direction = 'left'
def moveRight():
    pacman.direction = 'right'

# set window binding
window.listen()
window.onkeypress(moveUp, "Up")
window.onkeypress(moveDown, "Down")
window.onkeypress(moveLeft, "Left")
window.onkeypress(moveRight, "Right")                            


#main game loop
while True:
    window.update()

    #border collision
    if pacman.xcor > 300 or pacman.xcor < -300 or pacman.ycor > 300 or pacman.ycor < -300:
        lives -= 1
        pen.clear()
        pen.write("Score : {} Lives : {}".format(score,lives), align='center', font=('Courier',36))
        time.sleep(1)
        pen.goto(0,0)
    #check lives
    if lives == 0:
        score = 0
        lives = 3
        pen.clear()
        pen.write("Score : {} Lives : {}".format(score,lives), align='center', font=('Courier',36))
        time.sleep(1)
        pen.goto(0,0)


 
    #food and pacman collision
    for food in foods:
        if pacman.distance(food) < 10:
            score += 1
            pen.clear()
            pen.write("Score : {} Lives : {}".format(score,lives), align='center', font=('Courier',36))
            x = random.randint(-280,280)
            y = random.randint(-280,280)
            food.goto(x,y)
    
    #enemy and border
    for enemy in enemies:
        if enemy.xcor > 300 or enemy.xcor < -300 or enemy.ycor > 300 or enemy.ycor < -300:
            x = random.randint(-280,280)
            y = random.randint(-280,280)
            enemy.goto(x,y)
            enemyMovement()

    #enemy and pacman collision
    for enemy in enemies:
        if pacman.distance(enemy) < 10:
            lives -= 1
            pen.clear()
            pen.write("Score : {} Lives : {}".format(score,lives), align='center', font=('Courier',36))
            x = random.randint(-280,280)
            y = random.randint(-280,280)
            time.sleep(1)
            pacman.goto(x,y)


    movement()
    enemyMovement()