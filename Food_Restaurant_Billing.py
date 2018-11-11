from tkinter import *
import time
import random
root = Tk()

root.title("Food Destination")
root.geometry("1350x750+0+0")
Tops = Frame (root , width = 1350,height = 100,bd = 12,relief = "raise")
Tops.pack(side = TOP)
# must be flat, groove, raised, ridge, solid, or sunken
lblTitle = Label(Tops,font = ('arial',50,'bold'),text = "\tFood Destination\t\t    ")#.pack(side = TOP)
lblTitle.grid(row = 0, column = 0)

BottomMainFrame = Frame(root,width = 1350,height = 650,bd = 12,relief = 'raise')
BottomMainFrame.pack(side=  BOTTOM)

f1 = Frame(BottomMainFrame,width = 450,height = 650,bd = 12,relief = 'raise')
f1.pack(side=  LEFT)

f2 = Frame(BottomMainFrame,width = 450,height = 650,bd= 12 ,relief = "raise")
f2.pack(side = LEFT)

f2Top = Frame(f2,width = 450,height = 350,bd = 4,relief = 'raise')
f2Top.pack(side=  TOP)

f2Bottom = Frame(f2,width = 450,height = 300,bd = 4,relief = 'raise')
f2Bottom.pack(side=  BOTTOM)

f3 = Frame(BottomMainFrame,width = 450,height = 650,bd = 12,relief = 'raise')
f3.pack(side=  RIGHT)

var1 = root.Intvar()
# var2 = Tk. Intvar()
# var3 = Tk.Intvar()
# var4 = Tk.Intvar()
# var5 = Tk.Intvar()
# var6 = Tk.Intvar()
# var7 = Tk.Intvar()
# var8 = Tk.Intvar()
# var9 = Tk.Intvar()
# var10 = Tk.Intvar()
# var11 = Tk.Intvar()
# var12 = Tk.Intvar()
# var13 = Tk.Intvar()
# var14 = Tk.Intvar()
# var15  = Tk.Intvar()
# var16 = Tk.Intvar()
# var17 = Tk.Intvar()
# var18 = Tk.ntvar()
# var19  = Tk. Intvar()
# var20 = Tk.Intvar()
# var21 = Tk.Intvar()
# var22 = Tk.Intvar()
# var23 = Tk.Intvar()

var1.set(0)
# var2.set(0)
# var3.set(0)
# var4.set(0)
# var5.set(0)
# var6.set(0)
# var7.set(0)
# var8.set(0)
# var9.set(0)
# var10.set(0)
# var11.set(0)
# var12.set(0)
# var13.set(0)
# var14.set(0)
# var15.set(0)
# var16.set(0)
# var17.set(0)
# var1.set(0)
# var18.set(0)
# var19.set(0)
# var20.set(0)
# var21.set(0)
# var22.set(0)
# var23.set(0)

lblMeal = Label(f1,font = ('arial',18,'bold'),text = "\t Fast Food Meal and Vegetarian\t\t    ")#.pack(side = TOP)
lblMeal.grid(row = 0, column = 0)

Fries = Checkbutton(f1,text = 'Fries', variable = var1, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold')).grid(row = 1,column = 0,sticky  = W)





root.mainloop()
