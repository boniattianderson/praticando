
# import library tkinter
from tkinter import*
from tkinter import ttk

# colors

colorOne ='#3b3b3b'
colorTwo ='#feffff' 
colorThree ='#38576b'
colorFour ='#ECEFF1'
colorFive ='#FFAB40' 

window = Tk()
window.title('calculadora')
window.geometry('235x310')
window.config(bg=colorOne)

# Frame creation
frame_display = Frame(window, width=235, height=50, bg=colorThree)
frame_display.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)

# variable all values

all_values = ''

# Creation from label 
value_text = StringVar()

# creation functions 

def input_Values(event):

    global all_values

    all_values = all_values + str(event)
    
    # passing in the display
    value_text.set(all_values)
    
# function to calculate

def calculate():
    global all_values
    result = eval(all_values)
    
    value_text.set(str(result))

# function clear Screen 

def clearScreen():
    global all_values
    all_values = ''
    value_text.set('')




app_label = Label(frame_display, textvariable=value_text, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=colorThree, fg=colorTwo)
app_label.place(x=0, y=0)

# buttons creation

buttonOne = Button(frame_body, command=clearScreen, text="C", width=11, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonOne.place(x=0, y=0)
buttonTwo = Button(frame_body, command=lambda:input_Values('%'), text="%", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonTwo.place(x=118, y=0)
buttonThree = Button(frame_body, command=lambda:input_Values('/'), text="/", width=5, height=2, bg=colorFive, fg=colorTwo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonThree.place(x=177, y=0)

buttonFour = Button(frame_body, command=lambda:input_Values('7'), text="7", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonFour.place(x=0, y=52)
buttonFive = Button(frame_body, command=lambda:input_Values('8'), text="8", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonFive.place(x=59, y=52)
buttonSix = Button(frame_body, command=lambda:input_Values('9'), text="9", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonSix.place(x=118, y=52)
buttonSeven = Button(frame_body, command=lambda:input_Values('*'), text="*", width=5, height=2, bg=colorFive, fg=colorTwo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonSeven.place(x=177, y=52)

buttonEight = Button(frame_body, command=lambda:input_Values('4'), text="4", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonEight.place(x=0, y=104)
buttonNine = Button(frame_body, command=lambda:input_Values('5'), text="5", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonNine.place(x=59, y=104)
buttonEleven = Button(frame_body, command=lambda:input_Values('6'), text="6", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonEleven.place(x=118, y=104)
buttonTwelve = Button(frame_body, command=lambda:input_Values('-'), text="-", width=5, height=2, bg=colorFive, fg=colorTwo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonTwelve.place(x=177, y=104)

buttonThirteen = Button(frame_body, command=lambda:input_Values('1'), text="1", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonThirteen.place(x=0, y=156)
buttonFourteen = Button(frame_body, command=lambda:input_Values('2'), text="2", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonFourteen.place(x=59, y=156)
buttonFifteen = Button(frame_body, command=lambda:input_Values('3'), text="3", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonFifteen.place(x=118, y=156)
buttonSeventeen = Button(frame_body, command=lambda:input_Values('+'), text="+", width=5, height=2, bg=colorFive, fg=colorTwo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonSeventeen.place(x=177, y=156)

buttonEighteen = Button(frame_body, command=lambda:input_Values('0'), text="0", width=11, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonEighteen.place(x=0, y=208)
buttonNineteen = Button(frame_body, command=lambda:input_Values('.'), text=".", width=5, height=2, bg=colorFour, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonNineteen.place(x=118, y=208)
buttonTwenty = Button(frame_body, command=calculate, text="=", width=5, height=2, bg=colorFive, fg=colorTwo, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonTwenty.place(x=177, y=208)

window.mainloop()