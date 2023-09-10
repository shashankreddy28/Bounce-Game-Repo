from tkinter import *
import random
import time
tk=Tk()
tk.title("Bounce")
tk.resizable(0,0)       #makes sure window size is fixed
tk.wm_attributes("-topmost",1)  #this window becomes the topmos window
canvas=Canvas(tk,width=450,height=350,bd=0, highlightthickness=0)
canvas.pack()
tk.update()
current_label = None

#need to work on score
class Ball:

    def __init__(self, canvas, paddle, color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        start=[-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
        self.score=IntVar()
        self.score.set(0)
        global score_label
        score_label=Label(tk,text="Score:{}".format(self.score.get()))
        score_label.pack()
        


    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0] <=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                self.score.set(self.score.get()+1)
                print(self.score.get())
                
                score_label.config(text="Score: {}".format(ball.score.get()))

                return True
            return False
       
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos =self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=2
        if pos[3]>=self.canvas_height:
            self.hit_bottom= True
            canvas.create_text(220,100,text="Game Over!")
            #possibly create a pop-up window for retry option
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-9
        if self.hit_paddle(pos)==True:
            self.y=-9


class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,65,10,fill=color)
        self.canvas.move(self.id,190,270)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyRelease-Left>",self.stay)#new

        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
        self.canvas.bind_all("<KeyRelease-Right>",self.stay)#new
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=-2
            
        
    def stay(self,evt):#new
        self.x=0#new
    def turn_left(self,evt):
        self.x=-3
    def turn_right(self,evt):
        self.x=3



paddle = Paddle(canvas,'blue')
ball = Ball(canvas, paddle,'red')



while 1:
    
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)





