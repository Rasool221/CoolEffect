class Ball:
    def __init__(self, r, a, big_r):
        self.r = r
        self.x = random(0, 400)
        self.y = random(0, 400)
        self.rr = big_r + r
        
        self.xdir = random(-4, 4)
        self.ydir = random(-3, 3)
        
    def show(self):
        fill(0, 255, 0)
        ellipse(self.x, self.y, self.r*2, self.r*2)
        
        noFill()
        stroke(255, 255, 255)
        #ellipse(self.x, self.y, self.rr*2, self.rr*2)
    
    def move(self):
        self.x += self.xdir
        self.y += self.ydir        
        if (self.x > 410 or self.x < -10):
            self.xdir = -self.xdir
        elif (self.y > 410 or self.y < -10):
            self.ydir = -self.ydir
        
            
ball_list = []

def check_for_collision(ball_list):
    for i in range(len(ball_list)):
        for j in range(len(ball_list)):
            diff = sqrt(pow((ball_list[i].x - ball_list[j].x), 2) + pow(ball_list[i].y - ball_list[j].y, 2))
            if (diff < (ball_list[i].rr + ball_list[j].rr)):
                fill(0, 255, 255)
                line(ball_list[i].x, ball_list[i].y, ball_list[j].x, ball_list[j].y)
            
def setup():
    size(400, 400)
    
    # Change the number below to control the 
    # number of balls to draw
    BALLS_RENDERED = 15
    for i in range(BALLS_RENDERED):
        ball_list.append(Ball(5, 0, 40))
        
def draw():
    background(0)
    
    for i in range(len(ball_list)):
        ball_list[i].show()
        ball_list[i].move()
    
    check_for_collision(ball_list)
        
