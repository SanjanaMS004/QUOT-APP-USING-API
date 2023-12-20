from tkinter import*
from customtkinter import*
import requests
import random
import PIL.ImageTk as imtk 

# quote-api
response = requests.get("https://type.fit/api/quotes")
print(response.status_code)

# print(response.json())

#displays a quote
num=random.randint(0, 15)
quote=response.json()[num]['text']
author= response.json()[num]['author']
a=author.split(',')

win= Tk()
win.geometry('550x370')
win.title("QUOTES")
win.configure(bg="red")
win.resizable(width=False, height=False)

bg= imtk.PhotoImage(file="bubble_03.jpg")
r_arrow=imtk.PhotoImage(file="r22.png")
l_arrow=imtk.PhotoImage(file="r33.png")


my_canvas= Canvas(win)
my_canvas.place(relwidth=1,relheight=1)

my_canvas.create_image(0,0,image=bg,anchor='nw')

Q=my_canvas.create_text(270,150,text=quote,width=260)
A=my_canvas.create_text(270,200,text="- "+author,width=260)

frame1 =Frame(win,bg="red") 
frame1.place(x=500,y=170)

frame2 =Frame(my_canvas) 
frame2.place(x=20,y=170)

def next():
    global num, quote,Q,A
    l=len(response.json())-1
    if num==l:
        num=0
    else:
        num=num+1
    quote=response.json()[num]['text']
    author= response.json()[num]['author']    
    my_canvas.itemconfig(Q, text=quote)
    my_canvas.itemconfig(A, text="- "+ author)
    # my_canvas.create_image(0,0,image=new_bg,anchor='nw')

def prev():
    global num, quote,Q,A
    l=len(response.json())-1
    if num==0:
        num=l
    else:
        num=num-1
    quote=response.json()[num]['text']
    author= response.json()[num]['author']    
    my_canvas.itemconfig(Q, text=quote)
    my_canvas.itemconfig(A, text="- "+ author)

n_btn=Button(frame1,image=r_arrow,bg="#72D5EA",borderwidth=0,relief=RIDGE,command=next)
n_btn.pack()

p_btn=Button(frame2,image=l_arrow,bg="#72D5EA",borderwidth=0,relief=RIDGE,command=prev)
p_btn.pack()

win.mainloop()