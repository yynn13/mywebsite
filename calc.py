import tkinter as tk

root=tk.Tk()
root.geometry('800x600')
root.resizable(False, False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
def end():
    root.destroy()
def showframe(frame):
    frame.tkraise()



start = tk.Frame(root, bg='#2B2A29')
wip = tk.Frame(root, bg='#2B2A29')
cat = tk.Frame(root, bg='#2B2A29')
#algebra categories

algcat=tk.Frame(root, bg='#2B2A29')
variations=tk.Frame(root, bg='#2B2A29')
direct=tk.Frame(root, bg='#2B2A29')
xsolve=tk.Frame(root, bg='#2B2A29')
ysolve = tk.Frame(root, bg='#2B2A29')
xanswer=tk.Frame(root, bg='#2B2A29')
yanswer=tk.Frame(root, bg='#2B2A29')
#geometry frames
geocate= tk.Frame(root, bg='#2B2A29')
area= tk.Frame(root, bg='#2B2A29')
triangle = tk.Frame(root, bg='#2B2A29')
triangleans=tk.Frame(root, bg='#2B2A29')
square = tk.Frame(root, bg='#2B2A29')
squareans = tk.Frame(root, bg='#2B2A29')
rectangle = tk.Frame(root, bg='#2B2A29')
rectangleans = tk.Frame(root, bg='#2B2A29')
circle=tk.Frame(root, bg='#2B2A29')
circleans=tk.Frame(root, bg='#2B2A29')

for frame in (start,cat,algcat,variations,xanswer, direct,xsolve, geocate,area,circle,circleans, wip,triangle, triangleans, square, squareans, rectangleans,rectangle):
    frame.grid(row=0,column=0,sticky="nsew")


#code for the beginning

start_title = tk.Label(start,text='CALCOOLATOR',fg='white', bg='#2B2A29', font=('Uni Sans Heavy',40))
start_title.place(x=200,y=0)
startbut = tk.Button(start, text='start',height=3, width=10,command=lambda:showframe(cat))
startbut.place(x=350, y=300)

#code for work in progess stuff
texturmom = tk.Label(wip, text='That is a work in progress', bg="#2B2A29", fg='white', font=('Uni Sans Heavy',20))
texturmom.place(x=200,y=0)
goback = tk.Button(wip, text='GO BACK',height=3, width=10,command=lambda:showframe(cat))
goback.place(x=350, y=300)
#code for category picking

text2 = tk.Label(cat, text='Choose The Category', bg="#2B2A29", fg='white', font=('Uni Sans Heavy',30))
text2.place(x=200, y=0)
GEO = tk.Button(cat, text='Geometry', command=lambda:showframe(geocate))
ALG = tk.Button(cat, text='Algebra', command=lambda:showframe(algcat))
quit1= tk.Button(cat, width=10, height=3, text='Quit', command=end)
quit1.place(x=700,y=500)
GEO.grid(row=1, column=1,padx=200, pady=300,)
ALG.grid(row=1, column=2,padx=90, pady=300)

#code for geometry formula category picking

text3 = tk.Label(geocate, text='Choose The Category', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
text3.place(x=200, y=0)
back = tk.Button(geocate, text='back', command=lambda:showframe(cat))
back.place(x=700, y=500)
jo=tk.Button(geocate, text='Area of polygons', command=lambda:showframe(area))
Volume3d=tk.Button(geocate, text='Volume of 3D objects', command=lambda:showframe(wip))
jo.grid(row=1, column=1, padx=200, pady=300)
Volume3d.grid(row=1, column=2, padx=0, pady=300)

#code for algebra category picking

text3 = tk.Label(algcat, text='Choose The Category', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
text3.place(x=200, y=0)
back = tk.Button(algcat, text='back', command=lambda:showframe(cat))
back.place(x=700, y=500)
lin=tk.Button(algcat, text='linear equations', command=lambda:showframe(wip))
var=tk.Button(algcat, text='Variations', command=lambda:showframe(variations))
lin.grid(row=1, column=1, padx=200, pady=300)
var.grid(row=1, column=2, padx=0, pady=300)

#code for variations

vtext = tk.Label(variations, text='Choose the variation', bg='#2B2A29', fg='white', font=('Uni Sans Heavy',30))
v1 = tk.Button(variations, text='Direct',command=lambda:showframe(direct))
v2 = tk.Button(variations, text='Inverse')
vtext.place(x=200,y=0)
v1.place(x=200,y=300)
v2.place(x=500,y=300)

#command for solving x
def solvex():
    k = int(kval.get(1.0, 'end-1c'))
    y = int(yval.get(1.0, 'end-1c'))
    ans = k*y
    showframe(xanswer)
    text8 = tk.Label(xanswer, text='The value of x is', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
    text9 = tk.Label(xanswer, text=ans, bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
    but1 = tk.Button(xanswer, text='Categories', command=lambda: showframe(cat))
    but2 = tk.Button(xanswer, text='Use again', command=lambda: showframe(xsolve))
    but3 = tk.Button(xanswer, text='Pick another variation', command=lambda: showframe(variations))
    but1.place(x=300, y=500)
    but2.place(x=400, y=500)
    but3.place(x=500, y=500)
    text8.place(x=200, y=0)
    text9.place(x=200, y=50)
    kval.delete(1.0, 'end')
    yval.delete(1.0, 'end')


text = tk.Label(xsolve, text='To solve for x, we do k*y', bg='#2B2A29', fg='white', font=('Uni Sans Heavy',30))
kval = tk.Text(xsolve,height=1, width=1)
yval = tk.Text(xsolve,height=1, width=1)
text2 = tk.Label(xsolve, text='K:', bg='#2B2A29', fg='white', font=('Uni Sans Heavy',10))
text3 = tk.Label(xsolve, text='Y:', bg='#2B2A29', fg='white', font=('Uni Sans Heavy',10))
getans = tk.Button(xsolve, text='Solve',command=solvex)
getans.place(x=500,y=300)
text2.place(x=170,y=300)
text3.place(x=370,y=300)
text.place(x=200,y=0)
kval.place(x=200,y=300)
yval.place(x=400,y=300)

#code for direct variation

dtext1 = tk.Label(direct, text='Direct variations are x=ky',bg='#2B2A29',fg='white', font=('Uni Sans Heavy',30))
dbut1=tk.Button(direct,text='Find x', command=lambda:showframe(xsolve))
dbut2=tk.Button(direct,text='Find k')
dbut3=tk.Button(direct, text='Find y', command=lambda:showframe(ysolve))
dtext1.place(x=180,y=0)
dbut1.place(x=200,y=300)
dbut2.place(x=500,y=300)
dbut3.place(x=350,y=400)

#code for shape picking in area

back2 = tk.Button(area, text='back',command=lambda:showframe(geocate))
back2.place(x=700, y=500)
text4 = tk.Label(area, text='Choose The Shape', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
text4.place(x=200, y=0)
Circle = tk.Button(area, text='Circle',command=lambda:showframe(circle))
Rectangle = tk.Button(area,text='Rectangle',command=lambda:showframe(rectangle))
Triangle = tk.Button(area, text= 'Triangle',command=lambda:showframe(triangle))
Square = tk.Button(area, text='Square', command=lambda:showframe(square))
Square.place(x=200,y=400)
Circle.place(x=200, y=300)
Triangle.place(x=400, y=400)
Rectangle.place(x=400, y=300)

#code for the formula for circle
def answercircle():
    try:
        int(textbox.get(1.0))
        x=int(textbox.get(1.0))
        ans = 3.1415926535897932384626433832795028841*(x**2)
        f_ans = round(ans, 2)
        showframe(circleans)
        text8 = tk.Label(circleans, text='The area of the circle is', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        text9 = tk.Label(circleans, text=f_ans, bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        but1 = tk.Button(circleans, text='Categories', command=lambda: showframe(cat))
        but2 = tk.Button(circleans, text='Use again', command=lambda: showframe(circle))
        but3 = tk.Button(circleans, text='Pick another shape', command=lambda: showframe(area))
        but1.place(x=300, y=500)
        but2.place(x=400, y=500)
        but3.place(x=500, y=500)
        text8.place(x=200, y=0)
        text9.place(x=200, y=50)
        textbox.delete(1.0, 'end')
    except ValueError:
        urmom = tk.Label(circle, text='That is not a number', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        urmom2 = tk.Label(circle, text='Try again', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        urmom.place(x=200, y=300)
        urmom2.place(x=200, y=400)
back = tk.Button(circle, text='back', command=lambda:showframe(area))
back.place(x=700, y=500)
text1 = tk.Label(circle, text='The formula for the area', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
text2 = tk.Label(circle, text='of a circle is πr^2', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
text3 = tk.Label(circle, text='enter the value of r below', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
answer = tk.Button(circle, text='Get answer',command=answercircle)
textbox = tk.Text(circle, height=2, width=2)
text1.place(x=200, y=0)
text2.place(x=200, y=50)
text3.place(x=200, y=150)
textbox.place(x=200, y=500)
answer.place(x=250, y=500)

#code for triangle
def triangleanswer():
    try:
        int(ttextbox.get(1.0))
        int(ttextbox2.get(1.0))
        b = int(ttextbox.get(1.0, "end-1c"))
        h = int(ttextbox2.get(1.0, 'end-1c'))
        showframe(triangleans)
        finalanswer = (b * h) / 2
        text8 = tk.Label(triangleans, text='The area of the triangle is', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        text9 = tk.Label(triangleans, text=finalanswer, bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        text8.place(x=200, y=0)
        text9.place(x=200, y=50)
        but1 = tk.Button(triangleans, text='Categories', command=lambda: showframe(cat))
        but2 = tk.Button(triangleans, text='Use again', command=lambda: showframe(triangle))
        but3 = tk.Button(triangleans, text='Pick another shape', command=lambda: showframe(area))
        but1.place(x=300, y=500)
        but2.place(x=400, y=500)
        but3.place(x=500, y=500)
        text8.place(x=200, y=0)
        text9.place(x=200, y=50)
        ttextbox.delete(1.0, 'end')
        ttextbox2.delete(1.0, 'end')
    except ValueError:
        global urmom7
        global urmom8
        urmom7 = tk.Label(triangle, text='That is not a number', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        urmom8 = tk.Label(triangle, text='Try again', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        urmom7.place(x=200,y=300)
        urmom8.place(x=200,y=150)



tback = tk.Button(triangle, text='back', command=lambda:showframe(area))
tback.place(x=700, y=500)
ttext1 = tk.Label(triangle, text='The formula for the area', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
ttext2 = tk.Label(triangle, text='of a triangle is (b*h)/2', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
ttext3 = tk.Label(triangle, text='enter the value of b below', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 10))
ttext4 = tk.Label(triangle, text='enter the value of h below', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 10))
tanswer = tk.Button(triangle, text='Get answer', command=triangleanswer)
ttextbox = tk.Text(triangle, height=2, width=2)
ttextbox2 = tk.Text(triangle, height=2, width=2)
ttext1.place(x=200, y=0)
ttext2.place(x=200, y=50)
ttext3.place(x=150, y=450)
ttext4.place(x=350, y=450)
ttextbox.place(x=200, y=500)
ttextbox2.place(x=400, y=500)
tanswer.place(x=600, y=500)


#code for square
def answercircle():
    try:
        int(stextbox.get(1.0))
        x=int(stextbox.get(1.0))
        ans = x**2
        f_ans = round(ans, 2)
        showframe(squareans)
        text8 = tk.Label(squareans, text='The area of the circle is', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        text9 = tk.Label(squareans, text=f_ans, bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        but1 = tk.Button(squareans, text='Categories', command=lambda: showframe(cat))
        but2 = tk.Button(squareans, text='Use again', command=lambda: showframe(square))
        but3 = tk.Button(squareans, text='Pick another shape', command=lambda: showframe(area))
        but1.place(x=300, y=500)
        but2.place(x=400, y=500)
        but3.place(x=500, y=500)
        text8.place(x=200, y=0)
        text9.place(x=200, y=50)
        stextbox.delete(1.0, 'end')
    except ValueError:
        urmom = tk.Label(square, text='That is not a number', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        urmom2 = tk.Label(square, text='Try again', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        urmom.place(x=200, y=300)
        urmom2.place(x=200, y=400)
sback = tk.Button(square, text='back', command=lambda:showframe(area))
sback.place(x=700, y=500)
text5 = tk.Label(square, text='The formula for the area', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
text6 = tk.Label(square, text='of a square is s^2', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
text7 = tk.Label(square, text='enter the value of s below', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
answer= tk.Button(square,text='Get answer', command=answercircle)
stextbox = tk.Text(square,height=2, width=2)
text5.place(x=200,y=0)
text6.place(x=200,y=50)
text7.place(x=200,y=150)
stextbox.place(x=200,y=500)
answer.place(x=250,y=500)

#code for rectangle
def answerrectangle():
    try:
        x= int(recttextbox.get(1.0))
        y= int(recttextbox2.get(1.0))
        ans = x*y
        showframe(rectangleans)
        text8 = tk.Label(rectangleans, text='The area of the circle is', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        text9 = tk.Label(rectangleans, text=ans, bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        but1 = tk.Button(rectangleans, text='Categories', command=lambda: showframe(cat))
        but2 = tk.Button(rectangleans, text='Use again', command=lambda: showframe(rectangle))
        but3 = tk.Button(rectangleans, text='Pick another shape', command=lambda: showframe(area))
        but1.place(x=300, y=500)
        but2.place(x=400, y=500)
        but3.place(x=500, y=500)
        text8.place(x=200, y=0)
        text9.place(x=200, y=50)
        recttextbox.delete(1.0, 'end')
        recttextbox2.delete(1.0, 'end')
    except ValueError:
        global urmom3
        global urmom4
        urmom3 = tk.Label(rectangle, text='That is not a number', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        urmom4 = tk.Label(rectangle, text='Try again', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
        urmom4.place(x=200,y=300)
        urmom3.place(x=200,y=150)
back3 = tk.Button(rectangle, text='back', command=lambda:showframe(area))
back3.place(x=700, y=500)
recttext5 = tk.Label(rectangle, text='The formula for the area', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
recttext6 = tk.Label(rectangle, text='of a rectangle is l x w', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 30))
recttext7 = tk.Label(rectangle, text='enter the value of l below', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 10))
recttext8 = tk.Label(rectangle, text='enter the value of w below', bg="#2B2A29", fg='white', font=('Uni Sans Heavy', 10))
rectanswer = tk.Button(rectangle, text='Get answer',command=answerrectangle)
recttextbox=tk.Text(rectangle,height=2, width=2)
recttextbox2 = tk.Text(rectangle, height=2, width=2)
recttext5.place(x=200, y=0)
recttext6.place(x=200, y=50)
recttext7.place(x=150, y=450)
recttext8.place (x=350, y=450)
recttextbox.place(x=200, y=500)
recttextbox2.place(x=400, y=500)
rectanswer.place(x=600, y=500)

showframe(start)


root.mainloop()
