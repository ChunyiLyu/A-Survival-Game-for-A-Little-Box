#Conference Project from Chunyi Lyu
# import library
import Games
from Graphics import *
import random
import math

# set up global variables that i need to refer in my program
count = 0
currentLevel = []
allLevels = []
deathnote = Text((250, 20), "your box just died, type key r to restart the game")

def game():
    global count,currentLevel,allLevels, deathnote
    # create the window
    wid = 500
    len = 500
    win = Window("Survival Game for a Little Box", wid, len)
    win.mode = "physics"
    # draw the little box
    r = Rectangle(Point((wid/2 - 15), (len-60)),Point((wid/2 + 15),(len-30)))
    r.color = Color("salmon")
    r.draw(win)
    r.mass = .4
    r.friction = 2.0
    r.wrap = True


    # draw the frame of the window (base, wall1, wall2)
    base = Rectangle((0, (len-30)), (wid, (len-20)))
    base.bodyType = "static"
    base.color = Color("blue")
    base.draw(win)

    wall1 = Rectangle((0, 0), (5, (len-30)))
    wall1.bodyType = "static"
    wall1.color = Color("blue")
    wall1.draw(win)

    wall2 = Rectangle(((wid-5), 0), (wid, (len-30)))
    wall2.bodyType = "static"
    wall2.color = Color("blue")
    wall2.draw(win)

    # set up blocks for level 1
    floorL1 = Rectangle(Point(0, 380), Point(170, 390))
    floorL1.color = Color("blue")
    floorL1.bodyType = "static"
    level1 = [floorL1]

    # set up blocks for level 2
    level2 = []
    l = 200
    for i in range(2):
        y = 250 + i * 130
        b = Rectangle(Point(0, y), Point(l, (y + 10)))
        b.color = Color("gray")
        b.bodyType = "static"
        level2.append(b)
    l = 200
    for i in range(1):
        y = 330 + i * 90
        b = Rectangle(Point((wid - l), y), Point(wid, (y + 10)))
        b.color = Color("gray")
        b.bodyType = "static"
        level2.append(b)

    # set up blocks for level 3
    level3 = []
    l = 200
    for i in range(3):
        y = 150 + i * 130
        f = Rectangle(Point(0, y), Point(l, (y + 10)))
        f.color = Color("green")
        f.bodyType = "static"
        level3.append(f)
    l = 200
    for i in range(2):
        y = 200 + i * 130
        f = Rectangle(Point((wid - l), y), Point(wid, (y + 10)))
        f.color = Color("green")
        f.bodyType = "static"
        level3.append(f)

   # write the function for going to the next level of the game
    def gotoNextLevel(newlevel):
        global count, currentLevel
        for b in currentLevel:
            win.undraw(b)
        for b in newlevel:
            win.draw(b)
        count = 0
        currentLevel = newlevel
        r.moveTo(250, 455)

    gotoNextLevel(level1)

    # show the instruction of the game inside the window
    instruction = SpeechBubble((10, 10), (300, 240), "In this little game, you will need to use keys to control your box: Space(go up), Right, and Left. The goal is to move the box to the top floor. The game has 3 levels. You can only press space key 20 times at each level, or the box will die. Press key, n, after you complete one level. Click your mouse to start the game", (r.center.x, r.center.y))
    instruction.draw(win)

    allLevels = [level2, level3]


    # how the program reacts differently according to different pressed keys
    def keypressed(obj, event):
        global count, allLevels
        print("count is", count)
        if count < 21:

        # first, set different vectors applying on the box, when pressing Space, right, and left
            if event.key == "space" and count <=20:
                count = count + 1
                v = Vector(0, 100)
                r.body.ApplyForce(-v)
            elif event.key == "Right" and count <= 20:
                v = Vector(200, 50)
                r.body.ApplyForce(v)
            elif event.key == "Left" and count <= 20:
                v = Vector(-200, 50)
                r.body.ApplyForce(v)


            # press e to quit the game
            elif event.key == 'e':
                win.close()

            # press n to go to the next level, when the user complete all of the levels, a message shows in the window
            elif event.key == 'n':
                if allLevels == []:
                    box = Rectangle(Point(120, 400/3), Point(380, 400/3*2))
                    box.fill = makeColor(50, 50, 50)
                    box.bodyType = "static"
                    box.draw(win)
                    cong = Text((250, 205), "Congraduations! Press E to exit")
                    cong.bodyType = "static"
                    cong.fill = Color("red")
                    cong.draw(win)
                else:
                    nextlevel = allLevels[0]
                    allLevels = allLevels[1:]
                    gotoNextLevel(nextlevel)

        # when user has already pressed Space for 20 times, displays a message in the window
        else:

            if count == 21 and event.key in ["space", "Right", "Left"]:
                deathnote.fill = Color("blue")
                deathnote.draw(win)
            elif event.key == "r":
                deathnote.undraw()
                count = 0
                r.moveTo(250, 455)

    win.getMouse()
    instruction.undraw()
    win.onKeyPress(keypressed)
    win.run()


