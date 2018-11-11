from tkinter import *
#button2 = Button(topframe,text = "VEIW", fg="black",bg="white").pack(side=LEFT)
def welcome():
    print("Welcome To Facebook")
def create():
    print("You Are Not Eligble TO New Account")
root =  Tk()

root.title("Facebook LogIn from")
#root.geometry("354x364")
#topframe = Frame(root).pack()
#bottomframe = Frame(root).pack()
topframe = Frame(root).pack()
#topframe.pack()
#button1 = Button(topframe,text = "FILE", fg="black",bg="white").pack(side=TOP)
#button1.pack(side=LEFT)
#button3 = Button(topframe,text = "EDIT", fg="black",bg="white").pack(side=LEFT)
#button4 = Button(topframe,text = "WWW.Tkinter.com", fg="black",bg="white").pack(side=LEFT)
#button5 = Button(topframe,text = "help", fg="black")#,bg="white").pack(side=LEFT)
root.minsize(width=700, height=600)
#root.maxsize(width=700, height=600)
label = Label(root, text="Facebook", fg="white", bg="medium blue", pady=10, font=("Facebook", 32)).pack(side=TOP,fill=X)
#label.config(fontsize = 50)
label2 = Label(root, text="Log in to Facebook", fg="black", bg="white",
               font=("Log in to Facebook", 20)).pack(side=TOP, fill =X, padx=150,pady=30)
label3 = Label(root, text= "Username",  font=("Password",15) ).pack(side=TOP, padx = 130, pady = 00)
entry = Entry(width=50).pack(ipady=4)
label4 = Label(root, text= "Password", font=("Password",15)).pack(side=TOP, padx = 130, pady = 10)

entry2 = Entry(width=50).pack(ipady=4)
check=Checkbutton(root, text="Save password as a remember").pack(pady=5)
button1=Button(root, text = "LOGIN",fg="white",bg="medium blue",
                 padx=120, command = welcome, font=("LOGIN", 15)).pack(ipady=10,pady=10)
button2=Button(root, text = "Create a New Account",fg="white",
               bg="medium blue", command=create, padx=55,font=("Create a New Account", 15)).pack(ipady=10,pady=10)
#entry3 = Entry(root)
#entry3.grid(row=0, column=1)
#button3=Button(root, text="Forget Password").grid(column=1)
#label4= Label(root, text= "Password")
#label4.grid(row=9, column = 3)



root.mainloop()