import turtle,random,math

s = turtle.Screen()
s.title("space invaders")
s.bgpic("op.gif") #1720x961
s.tracer(0)

turtle.register_shape("player.gif")
turtle.register_shape("zgoli.gif")
turtle.register_shape("enemy.gif")

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.setposition(570, -90)
scorestring = "%s" %score
score_pen.write(scorestring, False, align="left", font=("horta", 38, "bold"))
score_pen.hideturtle()

death = 0
death_pen = turtle.Turtle()
death_pen.speed(0)
death_pen.penup()
death_pen.setposition(590, 95)
deathstring = "%s" %death
death_pen.write(deathstring, False, align="left", font=("horta", 42, "bold"))
death_pen.hideturtle()


player = turtle.Turtle()
player.shape("player.gif") #100x90
player.penup()
player.speed(0)
player.setposition(0,-200)
playerspeed = 30

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -230:
        x = -230
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 230:
        x = 230  
    player.setx(x)

def move_up():
    y = player.ycor()
    y += playerspeed
    if y > -150:
        y = -150
    player.sety(y)     

def move_down():
    y = player.ycor()
    y -= playerspeed 
    if y < -200:
       y = -200     
    player.sety(y)

no_of_enemies = 10
enemies = []
for i in range(no_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-220,220)
    y = random.randint(0,220)
    enemy.setposition(x,y)
enemyspeed = 0.09

bullet = turtle.Turtle()
bullet.shape("zgoli.gif")
bullet.penup()
bullet.speed(0)
bulletspeed = 3
bulletstate = "r"
bullet.hideturtle()

def fire_bullet():
    global bulletstate

    if bulletstate == "r":
        bulletstate = "f"
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 35: 
        xo = t2.xcor()
        yo = t2.ycor() - 10
        return True
    else: return False

turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(move_up,"Up")
turtle.onkeypress(move_down,"Down")
turtle.onkeypress(fire_bullet, "space")

while True:
    s.update()

    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 230:
                for e in enemies:
                    y = e.ycor()
                    y -= 20
                    e.sety(y)
                enemyspeed *= -1

        if enemy.xcor() < -230:
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemyspeed *= -1
        
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "r"
            bullet.setposition(0, -400)
            # enemy.hideturtle()
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x, y)

            death += 1
            deathstring = "%s" %death
            death_pen.clear()
            death_pen.write(deathstring, False, align="left", font=("horta", 42, "normal"))

            score += 5
            scorestring = "%s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("horta", 38, "normal"))

        
        if isCollision(player, enemy):
            player.hideturtle()
            for e in enemies:
                e.hideturtle()
    
    if bulletstate == "f":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletstate = "r"


turtle.mainloop()