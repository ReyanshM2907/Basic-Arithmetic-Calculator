from tkinter import *
root=Tk()
root.geometry("400x600")
root.title("Basic Arithmetic calculator")
root.configure(bg="silver")

def Add():
    num1=int(AddEnter11.get())
    num2=int(AddEnter12.get())
    ans=num1+num2
    Label1['text']=str(ans)
    
def Subtract():
    num1=int(SubtractEnter21.get())
    num2=int(SubtractEnter22.get())
    ans=num1-num2
    Label2['text']=str(ans)

    
def Multiply():
    num1=int(MultiplyyEnter31.get())
    num2=int(MultiplyEnter32.get())
    ans=num1*num2
    Label3['text']=str(ans)
    
def Divide():
    num1=int(DivideEnter41.get())
    num2=int(DivideEnter42.get())
    ans=num1/num2
    Label4['text']=str(ans)

Btn1=Button(root, text="Addition", font=('courier', 10, 'bold'), command=Add)
Btn1.place(relx=0.5, rely=0.05, anchor=CENTER)
AddEnter11=Entry(root)
AddEnter11.place(relx=0.7, rely=0.1, anchor=CENTER)
AddEnter12=Entry(root)
AddEnter12.place(relx=0.7, rely=0.15, anchor=CENTER)
Label11=Label(root, text="No 1 :")
Label11.place(relx=0.3, rely=0.1, anchor=CENTER)
Label12=Label(root, text="No 2 :")
Label12.place(relx=0.3, rely=0.15, anchor=CENTER)
Label1=Label(root, text="", font=('courier', 9, 'bold'), width=20)
Label1.place(relx=0.5, rely=0.2, anchor=CENTER)

Btn2=Button(root, text="Subtraction", font=('courier', 10, 'bold'), command=Subtract)
Btn2.place(relx=0.5, rely=0.3, anchor=CENTER)
SubtractEnter21=Entry(root)
SubtractEnter21.place(relx=0.7, rely=0.35, anchor=CENTER)
SubtractEnter22=Entry(root)
SubtractEnter22.place(relx=0.7, rely=0.4, anchor=CENTER)
Label21=Label(root, text="No 1 :")
Label21.place(relx=0.3, rely=0.35, anchor=CENTER)
Label22=Label(root, text="No 2 :")
Label22.place(relx=0.3, rely=0.4, anchor=CENTER)
Label2=Label(root, text="", font=('courier', 9, 'bold'), width=20)
Label2.place(relx=0.5, rely=0.45, anchor=CENTER)

Btn3=Button(root, text="Multiplication", font=('courier', 10, 'bold'), command=Multiply)
Btn3.place(relx=0.5, rely=0.55, anchor=CENTER)
MultiplicationEnter31=Entry(root)
MultiplicationEnter31.place(relx=0.7, rely=0.6, anchor=CENTER)
MultiplicationEnter32=Entry(root)
MultiplicationEnter32.place(relx=0.7, rely=0.65, anchor=CENTER)
Label31=Label(root, text="No 1 :")
Label31.place(relx=0.3, rely=0.6, anchor=CENTER)
Label32=Label(root, text="No 2 :")
Label32.place(relx=0.3, rely=0.65, anchor=CENTER)
Label3=Label(root, text="", font=('courier', 9, 'bold'), width=20)
Label3.place(relx=0.5, rely=0.7, anchor=CENTER)

Btn4=Button(root, text="Division", font=('courier', 10, 'bold'), command=Divide)
Btn4.place(relx=0.5, rely=0.8, anchor=CENTER)
DivideEnter41=Entry(root)
DivideEnter41.place(relx=0.7, rely=0.85, anchor=CENTER)
DivideEnter42=Entry(root)
DivideEnter42.place(relx=0.7, rely=0.9, anchor=CENTER)
Label41=Label(root, text="No 1 :")
Label41.place(relx=0.3, rely=0.85, anchor=CENTER)
Label42=Label(root, text="No 2 :")
Label42.place(relx=0.3, rely=0.9, anchor=CENTER)
Label4=Label(root, text="", font=('courier', 9, 'bold'), width=20)
Label4.place(relx=0.5, rely=0.95, anchor=CENTER)

root.mainloop()
