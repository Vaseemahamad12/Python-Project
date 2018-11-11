from tkinter import *
from tkinter import ttk




root=Tk()
root.title("Student's Feedback Form")
topframe = Frame(root).pack()
root.minsize(width = 1200, height = 650)

root.maxsize(width = 1200, height = 650)
label = Label(root, text = "STUDENT's FEEDBACK",
              fg = "black",
              font=("STUDENT's FEEDBACK", 20)).pack()
labe2 = Label(root, text = "Student Name",
              fg = "black",
              font=("Student Name", 15)).pack(pady = 10)
entry = Entry(root, width = 40).pack(ipady = 4)
labe3 = Label(root, text = "Student E-mail",
              fg = "black",
              font=("Student E-mail", 15)).pack(pady = 10)
entry2 = Entry(root, width = 40).pack(ipady = 4)
#label4 = Label(topframe,
 #              text = "Subject Name",
  #             fg = "black", anchor = 'sw' ,
         #        font = ("Subject Name", 15)).pack(fill = 'both',                                             pady = 10,
          #                                       padx = 150)



label4 = Label(root,
               text = "Subject Name",
               fg = "black",
               font = ("Subject Name", 15)).place(
                                                 y = 220,
                                                 x = 150)


combo = ttk.Combobox(root, width = 40, value = ['Design Analysis $ Algorithm',
                                                'Manegirial Economics',
                                                'Cyber Security',
                                                'Software Testing $ Audit',
                                                'Principles of Programming Language',
                                                'Data Base Management System']).place(y= 250, x= 150)



label5 = Label(root,
               text = "Subject Code",
               fg = "black",
               font = ("Subject Code", 15)).place(
                                                 y = 220,
                                                 x = 650)

combo2 = ttk.Combobox(root, width = 40, value = ['RCS-501',
                                                 'RCS-502',
                                                 'RCS-503',
                                                 'RAS-501',
                                                 'RUC-501',
                                                 'RIT-E12']).place(y= 250, x= 650)


label5 = Label(root,
               text = "How Do You Rate The Faculty-- ",
               fg = "black",
               font = ("How Do You Rate The Faculty-- ", 12)).place(
                                                 y = 300,
                                                 x = 10)

check = Checkbutton(root, text = "Poor", font = ("Poor", 12) ).place(x = 250, y = 300)

check2 = Checkbutton(root, text = "Good", font = ("Good", 12) ).place(x = 350, y = 300)

check3 = Checkbutton(root, text = "Very Good", font = ("Very Good", 12) ).place(x = 450, y = 300)
check4 = Checkbutton(root, text = "Excellent", font = ("Excellent", 12) ).place(x = 600, y = 300)


label6 = Label(root,
               text = "Suggestion For The Betterment Of Faculty And Institute.",
               fg = "black",
               font = ("Suggestion For The Betterment Of Faculty And Institute", 15)).place(
                                                 y = 350,
                                                 x = 200)

#entry3 = Entry(root, width = 100,).place(x= 200, y =400)

from tkinter import scrolledtext
txt = scrolledtext.ScrolledText(root,width=100,height=6, fg = "black", bg = "white smoke").place(x = 200, y = 400)

button=Button(root,  text= "SUBMIT", padx = 40,  pady = 10, fg = "white", bg = "black", font = ("SUBMIT", 10)).place(x = 450, y = 540)

button2=Button(root,  text= "CANCEL", padx = 40,  pady = 10, fg = "white", bg = "black", font = ("CANCEL", 10)).place(x = 620, y = 540)

#txt = ScrolledText(root,width=40,height=10)

#combo['value'] = ('DAA', 'ME','DBMS', 'CS' , 'STA', 'PPL')
#entry = Entry(root, width = 40).pack(


#def InitUI(event ):
 #  event.combo = ttk.Combobox(event, width = 15)(AA,D"ME"","DBMS","CS"","STA","PPL" )
# #event.combo.place(y = 250, x = 150)
 #event.combo['values'] =

root.mainloop()