from tkinter import *

root = Tk()
root.title("Calculator")

box1 = Entry(root, width = 37)
box1.grid(row = 6, column = 0, columnspan = 4)

box = Entry(root, width = 37, borderwidth = 5)
box.grid(row = 0, column = 0, columnspan = 4, ipady = 3)



# variables to be used in the program
operation = ""
number1 = 0
display = ""
given_output = False



# to change the display if = sign is pressed
def out():
    global display
    global given_output
    if(given_output):
        display = box.get()
        given_output = False


# to chnage the value of number1
def change_number1():
    global operation
    global number1
    if box.get() != "":
        if operation == "":
            number1 = float(box.get())
            box.delete(0, END)
        elif operation == "+":
            number1 += float(box.get())
            box.delete(0, END)
        elif operation == "-":
            number1 -= float(box.get())
            box.delete(0, END)
        elif operation == "/":
            number1 /= float(box.get())
            box.delete(0, END)
        elif operation == "*":
            number1 *= float(box.get())
            box.delete(0, END)


# to change the number in the box
def number_change(a):
    global display
    out()
    box.insert(END, a)
    display += str(a)
    box1.delete(0, END)
    box1.insert(0, display)


#************************************
#*******function declarations********
#************************************



def add():
    global operation
    global display
    out()

    if(given_output):
        display = box.get()
    
    if (len(display) >= 3 and display[-2] == operation and display[-2] != "+"):
        display = display[ :-3] + " + "
    elif(len(display) > 3 and display[-2] != operation):
        display += " + "
    else:
        display += " + "

    box1.delete(0, END)
    box1.insert(0, display)
    change_number1()
    operation = "+"
    

def subtract():
    global operation
    global display
    out()
    
    if (len(display) >= 3 and display[-2] == operation and display[-2] != "-"):
        display = display[ :-3] + " - "
    elif(len(display) > 3 and display[-2] != operation):
        display += " - "
    else:
        display += " - "

    box1.delete(0, END)
    box1.insert(0, display)
    change_number1()
    operation = "-"


def divide():
    global operation
    global display
    out()

    if (len(display) >= 3 and display[-2] == operation and display[-2] != "/"):
        display = display[ :-3] + " / "
    elif(len(display) > 3 and display[-2] != operation):
        display += " / "
    else:
        display += " / "

    box1.delete(0, END)
    box1.insert(0, display)
    change_number1()
    operation = "/"


def multiply():
    global operation
    global display
    out()
    
    if (len(display) >= 3 and display[-2] == operation and display[-2] != "*"):
        display = display[ : -3] + " * "
    elif(len(display) > 3 and display[-2] != operation):
        display += " * "
    else:
        display += " * "

    box1.delete(0, END)
    box1.insert(0, display)
    change_number1()
    operation = "*"


def output():
    global operation
    global display

    if(box.get() == ""):
        box.insert(0, "Wrong statement")
    change_number1()

    box.delete(0, END)
    box.insert(0,number1)
    operation = ""

    display = display + " = " + str(number1)
    box1.delete(0, END)
    box1.insert(0, display)
    
    global given_output
    given_output = True


def clear():
    global number1
    global operation
    global display
    display = ""
    number1 = 0
    operation = ""
    box.delete(0, END)
    box1.delete(0, END)


def backspace():
    global display
    index = len(box.get())
    box.delete(index - 1)
    if(len(display) > 0 and display[-1] != " " ):
        display = display[0:len(display) - 1]
        box1.delete(0, END)
        box1.insert(0, display)


def change_sign():
    global display
    if(box.get() != ""):
        for i in range(len(display) - 1 , -1 , -1):
            if (display[i] == "("):
                display = display[0 : i ] + display[i+ 2  : -1]
                box1.delete(0, END)
                box1.insert(0, display)
                break

            if (display[i] == " "):
                display = display[0 : i + 1] + "(-" + display[i + 1 : ] + ")"
                box1.delete(0, END)
                box1.insert(0, display)
                break

        a = float(box.get())
        box.delete(0, END)
        box.insert(0,-a)

#*************************************



#buttons declaration

#number keys
b1            = Button(root, width = 7, text = "1"   , height = 3, command = lambda: number_change(1)  ).grid(row = 4, column = 0)
b2            = Button(root, width = 7, text = "2"   , height = 3, command = lambda: number_change(2)  ).grid(row = 4, column = 1)
b3            = Button(root, width = 7, text = "3"   , height = 3, command = lambda: number_change(3)  ).grid(row = 4, column = 2)
b4            = Button(root, width = 7, text = "4"   , height = 3, command = lambda: number_change(4)  ).grid(row = 3, column = 0)
b5            = Button(root, width = 7, text = "5"   , height = 3, command = lambda: number_change(5)  ).grid(row = 3, column = 1)
b6            = Button(root, width = 7, text = "6"   , height = 3, command = lambda: number_change(6)  ).grid(row = 3, column = 2)
b7            = Button(root, width = 7, text = "7"   , height = 3, command = lambda: number_change(7)  ).grid(row = 2, column = 0)
b8            = Button(root, width = 7, text = "8"   , height = 3, command = lambda: number_change(8)  ).grid(row = 2, column = 1)
b9            = Button(root, width = 7, text = "9"   , height = 3, command = lambda: number_change(9)  ).grid(row = 2, column = 2)
b0            = Button(root, width = 7, text = "0"   , height = 3, command = lambda: number_change(0)  ).grid(row = 5, column = 1)

#operational keys
b_clear       = Button(root, width = 16, text = "C"   , height = 3, command = clear                     ).grid(row = 1, column = 0, columnspan = 2)
b_back        = Button(root, width = 7, text = "Back", height = 3, command = backspace                 ).grid(row = 1, column = 2)
b_divide      = Button(root, width = 7, text = "/"   , height = 3, command = divide                    ).grid(row = 1, column = 3)
b_multiply    = Button(root, width = 7, text = "*"   , height = 3, command = multiply                  ).grid(row = 2, column = 3)
b_subtract    = Button(root, width = 7, text = "-"   , height = 3, command = subtract                  ).grid(row = 3, column = 3)
b_add         = Button(root, width = 7, text = "+"   , height = 3, command = add                       ).grid(row = 4, column = 3)
b_change_sign = Button(root, width = 7, text = "+/-" , height = 3, command = change_sign               ).grid(row = 5, column = 0)
b_decimal     = Button(root, width = 7, text = "."   , height = 3, command = lambda: number_change(".")).grid(row = 5, column = 2)
b_output      = Button(root, width = 7, text = "="   , height = 3, command = output                    ).grid(row = 5, column = 3)



# main loop of the program
root.mainloop()