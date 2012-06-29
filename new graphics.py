##from graphics import *
##
##win = GraphWin('My Circle',150,150)
##c=Circle(Point(50,50),10)
##c.setFill('red')
##c.draw(win)
##
##win.mainloop()
from graphics import *
class Wheel(object):

    def __init__(self,center,wheel_radius,tire_radius):
        self.tire_circle=Circle(centre, tire_radius)
        self.wheel_circle=Circle(centre, wheel_radius)
    def draw(self,win):
        self.tire_circle.draw(win)
        self.wheel_circle.draw(win)
    def move(self,dx,dy):
        self.tire_circle.move(dx,dy)
        self.wheel_circle.move(dx,dy)
    def set_color(self,wheel_color,tire_color):
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)
    def undraw(self):
        self.tire_circle.undraw()
        self.wheel_circle.undraw()
    def get_size(self):
        return self.tire_circle.getRadius()
    def get_centre(self):
        return tire_circle.getCenter()
    
win=GraphWin('big wheel', 320,240)
w=Wheel(Point(100,100),50,70)
w.draw(win)
w.set_color('red','blue')
w.undraw()
win.mainloop()
        
    
