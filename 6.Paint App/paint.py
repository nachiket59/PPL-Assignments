from tkinter import *
from tkinter.ttk import *
import tkinter.font
from tkinter.colorchooser import *
class PaintApp:
	color = '#000000'
	drawing_tool = "line"
	left_btn = "up"
	x_pos, y_pos = None, None
	x1,y1,x2,y2 = None,None,None,None
	def __init__(self,root):
		menu = Frame(root)  
		sel_line = Button(menu, text= "line", command = self.select_line)
		sel_pencil = Button(menu, text= "pencil", command = self.select_pencil)
		sel_rect = Button(menu, text= "rectangle", command = self.select_rect)
		sel_oval = Button(menu, text= "oval", command = self.select_oval)
		sel_arc = Button(menu, text= "arc", command = self.select_arc)
		sel_eraser = Button(menu, text= "eraser", command = self.select_eraser)
		pick_color = Button(menu, text= "select color", command = self.select_color)
		drawing_area = Canvas(root,bg="white")
		#drawing_area.pack()
		drawing_area.bind("<Motion>",self.motion)
		drawing_area.bind("<ButtonPress-1>", self.left_btn_down)
		drawing_area.bind("<ButtonRelease-1>",self.left_btn_up)
		
		menu.pack(fill = BOTH, expand = True, side=RIGHT)
		pick_color.pack(side = TOP)
		sel_line.pack(side = TOP) 
		sel_pencil.pack(side = TOP)
		sel_rect.pack(side = TOP)
		sel_oval.pack(side = TOP)
		sel_arc.pack(side = TOP)
		sel_eraser.pack(side = TOP)
		drawing_area.pack(side = RIGHT)	
	
	def select_line(self,event = None):
		self.drawing_tool = "line"
	
	def select_pencil(self,event = None):
		self.drawing_tool = "pencil"

	def select_arc(self,event = None):
		self.drawing_tool = "arc"
	
	def select_rect(self,event = None):
		self.drawing_tool = "rectangle"	

	def select_oval(self,event = None):
		self.drawing_tool = "oval"

	def select_eraser(self,event = None):
		self.drawing_tool = "eraser"		
			
	def select_color(self,event = None):
		x = askcolor()[1]
		if x is not None:
			self.color = x
		print(self.color)

	#left btn press(down)
	def left_btn_down(self,event=None):
		self.left_btn="down"
		self.x1 = event.x
		self.y1 = event.y
	
	#left btn press(down)
	def left_btn_up(self,event=None):
		self.left_btn="up"
		self.x_pos = None
		self.y_pos = None
		self.x2 = event.x
		self.y2 = event.y
		#print(self.x1,self.y1,self.x2,self.y2)
		if self.drawing_tool == "line":
			self.draw_line(event)
		elif self.drawing_tool == "rectangle":
			self.rectangle_draw(event)
		elif self.drawing_tool == "oval":
			self.ovel_draw(event)
		elif self.drawing_tool == "arc":
			self.arc_draw(event)			
	
	#track mouse motion
	def motion(self,event=None):
		if self.drawing_tool == "pencil":
			self.pencil_draw(event)
		elif self.drawing_tool == "eraser":
			self.eraser_draw(event)	

	#drawing logic by pencil tool
	def pencil_draw(self,event =None):
		if self.left_btn == "down":
			if self.x_pos is not None and self.y_pos is not None:
				event.widget.create_line(self.x_pos,self.y_pos,event.x,event.y,smooth = TRUE,fill = self.color)
			self.x_pos = event.x
			self.y_pos = event.y

	def eraser_draw(self,event =None):
		if self.left_btn == "down":
			if self.x_pos is not None and self.y_pos is not None:
				event.widget.create_line(self.x_pos,self.y_pos,event.x,event.y,smooth = TRUE,fill = "white", width = 20)
			self.x_pos = event.x
			self.y_pos = event.y		

	#draw line from point a to b		
	def draw_line(self,event =None):
		if None not in (self.x1, self.y1, self.x2, self.y2):
			event.widget.create_line(self.x1,self.y1,self.x2,self.y2,smooth = TRUE, fill = self.color)
	
	def arc_draw(self, event=None):
		if None not in (self.x1, self.y1, self.x2,self.y2):
			coords = self.x1, self.y1, self.x2,self.y2
			event.widget.create_arc(coords, start=0, extent=150,style=ARC)

	def ovel_draw(self,event= None):
		if None not in (self.x1, self.y1, self.x2,self.y2):
			event.widget.create_oval(self.x1, self.y1,self.x2, self.y2,fill=self.color,outline=self.color,width=2)

	def rectangle_draw(self,event =None):
		if None not in (self.x1, self.y1, self.x2,self.y2):
			event.widget.create_rectangle(self.x1, self.y1,self.x2, self.y2,fill=self.color,outline=self.color,width=2)
root = Tk()
paint = PaintApp(root)
root.mainloop()