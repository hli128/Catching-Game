'''
Move the Paddle using mouse
Catching object worth for 5 points
Missing the object will result in -1 point
'''
ballPosX = []
ballPosY = []

# create object list with len of 3
for i in range(5):
    ballPosX.append(random(0,300))
    ballPosY.append(random(0,150))

ballSpeed = 3

screenWidth = 560
screenHeight = 560

# paddle config
paddlePosX = 0
paddlePosY = 500
paddleWidth = 70
paddleHeight = 50

scoreCount = 0 # actual score
scoreDisplay = 0 # score showing to player

def setup():
    global pad, assets, bg, scoreBoard
    size(screenWidth, screenHeight)
    
    #load image
    bg = loadImage("assets/bg.png") 
    scoreBoard = loadImage("assets/score.png") 
    pad = loadImage("assets/pad.png")
    diamond = loadImage("assets/diamond.png")
    diamond1 = loadImage("assets/diamond1.png")
    diamond2 = loadImage("assets/diamond2.png")
    diamond3 = loadImage("assets/diamond3.png")
    diamond4 = loadImage("assets/diamond4.png")
    assets = [diamond, diamond1, diamond2, diamond3, diamond4]
    
    background(bg)
    noStroke()
    rectMode(CENTER)
    
def draw():
    global ballPosX, ballPosY, ballSpeed, paddlePosX, scoreCount, scoreDisplay, assets, pad, bg, scoreBoard
    
    paddlePosX = mouseX
    
    # drop   
    for i in range(len(ballPosX)):
        ballPosX[i] += random(-2, 2) # random X
        if i < len(ballPosY):
            ballPosY[i] += (ballSpeed + random(0,1))
        # off-screen
        if ballPosY[i] > screenHeight + 20:
            ballPosX[i] = random(0, screenWidth)
            ballPosY[i] = random(-20, 20)
            scoreCount -= 1 # miss the catch

        # catch
        if ballPosX[i] > paddlePosX - paddleWidth/2:
            if ballPosX[i] < paddlePosX + paddleWidth/2:    
                if ballPosY[i] > paddlePosY - paddleHeight/2 - 15/2:
                    ballPosX[i] = random(30, screenWidth)
                    ballPosY[i] = random(-20, 20)
                    scoreCount += 5  # catch diamond to win 5 points
                
    # draw
    background(bg)
    for i in range(len(ballPosX)):
        image(assets[i],ballPosX[i], ballPosY[i],44, 44)
    image(pad, paddlePosX, paddlePosY, paddleWidth, paddleHeight)         
    
    # hysteresis on score display
    if scoreDisplay < scoreCount:         
        scoreDisplay += 1
        fill(255,215,235)
        textSize(35)
        text("CATCH!", mouseX, mouseY)
    if scoreDisplay > scoreCount:         
        scoreDisplay -= 1
        
    image(scoreBoard, 10, 15)
    fill(255, 0, 0)
    textSize(22)
    text(str(scoreDisplay), 70, 50)

    fill(255,215,235)
    textSize(33)
    text("Catch Diamond!", 300, 50)
    
