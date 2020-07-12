from tkinter import *

root = Tk()
root.title("simplecalculater")
root.geometry("227x275")

# entry

entry1= Entry(root, width=15 , font=('Digital-7',20) ,borderwidth=15 ,bg="grey" ,fg="darkblue")
entry1.grid(row=0,column=0,columnspan=4)


# logic
def click(number):
    
    num1 = entry1.get()
    entry1.delete(0, END) 
    entry1.insert(0,str(num1) + str(number))

def btn_clear():
    
    entry1.delete(0, END)
    
def btn_add():
    global fun
    global n1
    fun = "addition"
    n1 = entry1.get()
    entry1.delete(0,END)
    
def btn_sub(): 
    
    global fun
    global num3
    fun = ("subtraction")
    num3=entry1.get()
    entry1.delete(0,END)
    
    
def btn_divide(): 
    
    global fun
    global num4
    fun = ("divide")
    num4=entry1.get()
    entry1.delete(0,END)
    
    
def btn_multiple(): 
    
    global fun
    global num5
    fun = ("multiple")
    num5=entry1.get()
    entry1.delete(0,END)    
    
def btn_equal():
    
    num2=entry1.get()
    entry1.delete(0, END) 

    # if/Else statement
    if fun == "addition":
        if "." in num2:
            n2=float(num2)
            n3=float(n1)
            entry1.delete(0, END)
            entry1.insert(0,(n3) + (n2))
            
        elif "." in n1:
            n2=float(num2)
            n3=float(n1)
            entry1.delete(0, END)
            entry1.insert(0,(n3) + (n2))
        try:
            n2=int(num2)
            n3=int(n1)
        
        except:
            print("")
        
        else:
            n2=int(num2)
            n3=int(n1)
            entry1.delete(0, END)
            entry1.insert(0, (n3) + (n2))
            
    if fun == "subtraction":
        if "." in num2:
            n4=float(num2)
            n5=float(num3)
            entry1.delete(0, END)
            entry1.insert(0,(n5) - (n4))
            
        elif "." in num3:
            n4=float(num2)
            n5=float(num3)
            entry1.delete(0, END)
            entry1.insert(0,(n5) - (n4))
        
        try:
            n4=int(num2)
            n5=int(num3)
        
        except:
            print("")
            
        else:
            n4=int(num2)
            n5=int(num3)
            entry1.delete(0, END)
            entry1.insert(0, (n5) - (n4))
            
    
    if fun == "divide":
        if "." in num2:
            n6=float(num2)
            n7=float(num4)
            entry1.delete(0, END)
            entry1.insert(0,(n7) / (n6))
            
        elif "." in num4:
            n6=float(num2)
            n7=float(num4)
            entry1.delete(0, END)
            entry1.insert(0,(n7) / (n6))
            
        try:
            n6=int(num2)
            n7=int(num4)
        
        except:
            print("")
        
        else:
            n6=int(num2)
            n7=int(num4)
            entry1.delete(0, END)
            entry1.insert(0, (n7) / (n6))
           
    
    if fun == "multiple":
        if "." in num2:
            n8=float(num2)
            n9=float(num5)
            entry1.delete(0, END)
            entry1.insert(0,(n9) * (n8))
            
        
        elif "." in num5:
            n8=float(num2)
            n9=float(num5)
            entry1.delete(0, END)
            entry1.insert(0,(n9) * (n8))
         
        try:
            n8=int(num2)
            n9=int(num5)
        
        except:
            print("")
        
        else:
            n8=int(num2)
            n9=int(num5)
            entry1.delete(0, END)
            entry1.insert(0, (n9) * (n8))
        
#buttons

btn1 = Button(root, text="1", width=8,height=1 ,bg="green",fg="black",pady=5 ,padx=5,borderwidth=3,command=lambda:click(1))
btn1.grid(row=1, column=0 )

btn2 = Button(root, text="2", width=8,height=1 ,bg="green",fg="black",pady=5 ,padx=5,borderwidth=3,command=lambda:click(2))
btn2.grid(row=1, column=1 )

btn3 = Button(root, text="3", width=8,height=1 ,bg="green",fg="black",pady=5 ,padx=5,borderwidth=3,command=lambda:click(3))
btn3.grid(row=1, column=2 )

btn4 = Button(root, text="4", width=8,height=1 ,bg="green",fg="black",pady=5 ,padx=5,borderwidth=3,command=lambda:click(4))
btn4.grid(row=2, column=0 )

btn5 = Button(root, text="5", width=8, height=1 ,bg="green",fg="black",pady=5 ,padx=5,borderwidth=3,command=lambda:click(5))
btn5.grid(row=2, column=1 )

btn6 = Button(root, text="6", width=8,height=1 ,bg="green",fg="black",pady=5 ,padx=5,borderwidth=3,command=lambda:click(6))
btn6.grid(row=2, column=2 )

btn7 = Button(root, text="7", width=8,height=1 ,bg="green",fg="black",pady=5 ,padx=5,borderwidth=3,command=lambda:click(7))
btn7.grid(row=3, column=0 )

btn8 = Button(root, text="8", width=8, height=1 ,bg="green",fg="black",pady=5 ,padx=5,borderwidth=3,command=lambda:click(8))
btn8.grid(row=3, column=1 )

btn9 = Button(root, text="9", width=8,height=1 ,bg="green",fg="black",pady=5 ,padx=5,borderwidth=3,command=lambda:click(9))
btn9.grid(row=3, column=2 )

btn10 = Button(root, text="0", width=8,height=1 ,bg="green",fg="black",pady=5 ,padx=5,borderwidth=3,command=lambda:click(0))
btn10.grid(row=4, column=0 )

btnAdd = Button(root, text="+", width=8,height=1 ,bg="green",fg="white",pady=5 ,padx=5,borderwidth=3,command=btn_add)
btnAdd.grid(row=4, column=1 )

btnsub = Button(root, text="-", width=8,height=1 ,bg="green",fg="white",pady=5 ,padx=5,borderwidth=3,command=btn_sub)
btnsub.grid(row=4, column=2 )

btn_multiple = Button(root, text="*", width=8,height=1 ,bg="green",fg="white",pady=5 ,padx=5,borderwidth=3 ,command=btn_multiple )
btn_multiple.grid(row=5, column=0 )

btn_equal = Button(root, text="=", width=19,height=1 ,bg="lightgreen",fg="black",pady=5 ,padx=5,borderwidth=3 ,command=btn_equal)
btn_equal.grid(row=5, column=1 ,columnspan=25)

btnDivide = Button(root, text="/", width=8,height=1 ,bg="green",fg="white",pady=5 ,padx=5,borderwidth=3 ,command=btn_divide )
btnDivide.grid(row=6, column=0 )

btnDot = Button(root, text=".", width=8,height=1 ,bg="lightgreen",fg="black",pady=5 ,padx=5,borderwidth=3 ,command=lambda:click("."))
btnDot.grid(row=6, column=1)

btnclear = Button(root, text="CE", width=8,height=1 ,bg="lightgreen",fg="black",pady=5 ,padx=5 ,borderwidth=3 ,command=btn_clear)
btnclear.grid(row=6, column=2 )

root.mainloop()
