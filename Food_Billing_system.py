import tkinter  as tk
# from ttk import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import  * #Frame,Label,Tk,Checkbutton ,
#import *
import time
import random
root = Tk()


root.geometry("1350x750+0+0")
root.title("Food Destination")
Tops = Frame (root , width = 1350,height = 100,bd = 6,relief = "raise")
Tops.pack(side = TOP)
# must be flat, groove, raised, ridge, solid, or sunken
lblTitle = Label(Tops,font = ('arial',50,'bold'),text = "\tFood Destination\t\t    ")#.pack(side = TOP)
lblTitle.grid(row = 0, column = 0)

BottomMainFrame = Frame(root,width = 1350,height = 650,bd = 6,relief = 'raise')
BottomMainFrame.pack(side=  BOTTOM)

f1 = Frame(BottomMainFrame,width = 450,height = 650,bd = 2,relief = 'raise')
f1.pack(side=  LEFT)

f2 = Frame(BottomMainFrame,width = 450,height = 650,bd= 2 ,relief = "raise")
f2.pack(side = LEFT)

f2Top = Frame(f2,width = 450,height = 350,bd = 2,relief = 'raise')
f2Top.pack(side=  TOP)

f2Bottom = Frame(f2,width = 450,height = 300,bd = 1,relief = 'raise')
f2Bottom.pack(side=  BOTTOM)

f3 = Frame(BottomMainFrame,width = 450,height = 650,bd = 2,relief = 'raise')
f3.pack(side=  RIGHT)

var1 =  IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15  = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19  =  IntVar()
var20 =  IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var1.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)

varFries  = StringVar()
varSalad = StringVar()
varHamburger = StringVar()
varOnionRings = StringVar()
varChickenSalad = StringVar()
varChickenSandwich = StringVar()
varCheeseSandwich = StringVar()
varFishSandwich = StringVar()


varHashBrown = StringVar()
varToastedBage1= StringVar()
varPancakesSyrup = StringVar()
varPineappleStick  = StringVar()
varChocolateMuffin = StringVar()


varTea = StringVar()
varColdDrinks = StringVar()
varCoffee = StringVar()
varJuice = StringVar()
varWaterBottle = StringVar()

varVanillaCone = StringVar()
varVanillaShake = StringVar()
varStrawberryShake = StringVar()

varChange =  StringVar()
varSubTotal = StringVar()
varTotal = StringVar()
varTotal = StringVar()



varFries.set("0")
varSalad.set("0")
varHamburger.set("0")
varOnionRings.set("0")
varChickenSalad.set("0")
varChickenSandwich.set("0")
varCheeseSandwich.set("0")
varFishSandwich.set("0")
varTotal.set("0")


varHashBrown.set("0")
varToastedBage1.set("0")
varPancakesSyrup.set("0")
varPineappleStick.set("0")
varChocolateMuffin.set("0")


varTea.set("0")
varColdDrinks.set("0")
varCoffee.set("0")
varJuice.set("0")
varWaterBottle.set("0")
varVanillaCone.set("0")
varVanillaShake.set("0")
varStrawberryShake.set("0")

varChange.set("0")
varSubTotal.set("0")

def iExit():
    qExit = messagebox.askyesno("Fast Food", "Do You Want To Quit")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    varFries.set("0")
    varSalad.set("0")
    varHamburger.set("0")
    varOnionRings.set("0")
    varChickenSalad.set("0")
    varChickenSandwich.set("0")
    varCheeseSandwich.set("0")
    varFishSandwich.set("0")
    varTotal.set("0")

    varHashBrown.set("0")
    varToastedBage1.set("0")
    varPancakesSyrup.set("0")
    varPineappleStick.set("0")
    varChocolateMuffin.set("0")

    varTea.set("0")
    varColdDrinks.set("0")
    varCoffee.set("0")
    varJuice.set("0")
    varWaterBottle.set("0")
    varVanillaCone.set("0")
    varVanillaShake.set("0")
    varStrawberryShake.set("0")

    varChange.set("0")
    varSubTotal.set("0")

    txtFries.configure(state = DISABLED)
    txtSalad.configure(state= DISABLED)
    txtHamburger.configure(state = DISABLED)
    txtOnionRings.configure(state = DISABLED)
    txtChickenSalad.configure(state =DISABLED)
    txtChickenSandwich.configure(state = DISABLED)
    txtCheeseSandwich.configure(state = DISABLED)
    txtFishSandwich.configure(state = DISABLED)
    txtHashBrown.configure(state = DISABLED)
    txtToastedBage1.configure(state = DISABLED)
    txtPancakesSyrup.configure(state= DISABLED)
    txtPineappleStick.configure(state = DISABLED)
    txtChocolateMuffin.configure(state = DISABLED)
    txtTea.configure(state = DISABLED)
    txtColdDrinks.configure(state= DISABLED)
    txtCoffee.configure(state= DISABLED)
    txtJuice.configure(state = DISABLED)
    txtWaterBottle.configure(state= DISABLED)
    txtVanillaCone.configure(state = DISABLED)
    txtVanillaShake.configure(state = DISABLED)
    txtStrawberryShake.configure(state = DISABLED)
    txtChange.configure(state= DISABLED)
    txtPayment.configure(state = DISABLED)
    txtSubTotal.configure(state= DISABLED)
    txtTotal.configure(state = DISABLED)
    txtTax.configure(state= DISABLED)

def chkFries():
    if(var1.get() == 1):
        txtFries.configure(state = NORMAL)
        varFries.set("")
    elif(var1.get() == 0):
        txtFries.configure(state = DISABLED)
        varFries.set("0")


def chkSalad():
    if(var2.get() == 1):
        txtSalad.configure(state = NORMAL)
        varSalad.set("")
    elif(var2.get() == 0):
        txtSalad.configure(state = DISABLED)
        varSalad.set("0")


def chkHamburger():
    if(var3.get() == 1):
        txtHamburger.configure(state = NORMAL)
        varHamburger.set("")
    elif(var3.get() == 0):
        txtHamburger.configure(state = DISABLED)
        varHamburger.set("0")


def chkOnionRings ():
    if(var4.get() == 1):
        txtOnionRings.configure(state = NORMAL)
        varOnionRings.set("")
    elif(var4.get() == 0):
        txtOnionRings.configure(state = DISABLED)
        varOnionRings.set("0")


def chkChickenSalad ():
    if(var5.get() == 1):
        txtChickenSalad.configure(state = NORMAL)
        varChickenSalad.set("")
    elif(var5.get() == 0):
        txtChickenSalad.configure(state = DISABLED)
        varChickenSalad.set("0")


def chkChickenSandwich():
    if(var6.get() == 1):
        txtChickenSandwich .configure(state = NORMAL)
        varChickenSandwich .set("")
    elif(var6.get() == 0):
        txtChickenSandwich.configure(state = DISABLED)
        varChickenSandwich .set("0")



def chkCheeseSandwich():
    if(var7.get() == 1):
        txtCheeseSandwich .configure(state = NORMAL)
        varCheeseSandwich .set("")
    elif(var7.get() == 0):
        txtCheeseSandwich.configure(state = DISABLED)
        varCheeseSandwich .set("0")


def chkFishSandwich():
    if(var8.get() == 1):
        txtFishSandwich .configure(state = NORMAL)
        varFishSandwich .set("")
    elif(var8.get() == 0):
        txtFishSandwich.configure(state = DISABLED)
        varFishSandwich .set("0")


def chkHashBrown():
    if(var9.get() == 1):
        txtHashBrown.configure(state = NORMAL)
        varFishSandwich .set("")
    elif(var9.get() == 0):
        txtHashBrown.configure(state = DISABLED)
        varHashBrown.set("0")

def chkToastedBage1():
    if(var10.get() == 1):
        txtToastedBage1.configure(state = NORMAL)
        varToastedBage1.set("")
    elif(var10.get() == 0):
        txtToastedBage1.configure(state = DISABLED)
        varToastedBage1.set("0")


def chkPancakesSyrup():
    if(var11.get() == 1):
        txtPancakesSyrup.configure(state = NORMAL)
        varPancakesSyrup.set("")
    elif(var11.get() == 0):
        txtPancakesSyrup.configure(state = DISABLED)
        varPancakesSyrup.set("0")

#
def chkPineappleStick():
    if(var12.get() == 1):
        txtPineappleStick.configure(state = NORMAL)
        varPineappleStick.set("")
    elif(var12.get() == 0):
        txtPineappleStick.configure(state = DISABLED)
        varPineappleStick.set("0")


def chkChocolateMuffin():
    if(var13.get() == 1):
        txtChocolateMuffin.configure(state = NORMAL)
        varChocolateMuffin.set("")
    elif(var13.get() == 0):
        txtChocolateMuffin.configure(state = DISABLED)
        varChocolateMuffin.set("0")


def chkTea():
    if(var14.get() == 1):
        txtTea.configure(state = NORMAL)
        varTea.set("")
    elif(var14.get() == 0):
        txtTea.configure(state = DISABLED)
        varTea.set("0")


def chkColdDrinks ():
    if(var15.get() == 1):
        txtColdDrinks .configure(state = NORMAL)
        varColdDrinks .set("")
    elif(var15.get() == 0):
        txtColdDrinks .configure(state = DISABLED)
        varColdDrinks .set("0")


def chkCoffee():
    if (var16.get() == 1):
        txtCoffee.configure(state=NORMAL)
        varCoffee.set("")
    elif (var16.get() == 0):
        txtCoffee.configure(state=DISABLED)
        varCoffee.set("0")

def chkJuice():
    if (var17.get() == 1):
        txtJuice.configure(state=NORMAL)
        varJuice.set("")
    elif (var17.get() == 0):
        txtJuice.configure(state=DISABLED)
        varJuice.set("0")


def chkWaterBottle():
    if (var18.get() == 1):
        txtWaterBottle.configure(state=NORMAL)
        varWaterBottle.set("")
    elif (var18.get() == 0):
        txtWaterBottle.configure(state=DISABLED)
        varWaterBottle.set("0")


def chkVanillaCone ():
    if (var19.get() == 1):
        txtVanillaCone .configure(state=NORMAL)
        varVanillaCone .set("")
    elif (var19.get() == 0):
        txtVanillaCone .configure(state=DISABLED)
        varVanillaCone .set("0")


def chkVanillaShake  ():
    if (var20.get() == 1):
        txtVanillaShake  .configure(state=NORMAL)
        varVanillaShake  .set("")
    elif (var20.get() == 0):
        txtVanillaShake  .configure(state=DISABLED)
        varVanillaShake  .set("0")


def chkStrawberryShake():
    if (var21.get() == 1):
        txtStrawberryShake.configure(state=NORMAL)
        varStrawberryShake.set("")
    elif (var21.get() == 0):
        txtStrawberryShake.configure(state=DISABLED)
        varStrawberryShake.set("0")


def costofmeal():
    meal1 = float(varFries.get())
    meal2 = float(varSalad.get())
    meal3 = float(varHamburger.get())
    meal4 = float(varOnionRings.get())
    meal5 = float(varChickenSalad.get())
    meal6 = float(varFishSandwich.get())
    meal7 = float(varCheeseSandwich.get())
    meal8 = float(varChickenSandwich.get())
    meal9 = float(varHashBrown.get())
    meal10 = float(varToastedBage1.get())
    meal11 = float(varPancakesSyrup.get())
    meal12 = float(varPineappleStick.get())
    meal13 = float(varChocolateMuffin.get())
    meal14 = float(varTea.get())
    meal15 = float(varColdDrinks.get())
    meal16 = float(varCoffee.get())
    meal17 = float(varJuice.get())
    meal18 = float(varWaterBottle.get())
    meal19 = float(varVanillaCone.get())
    meal20 = float(varVanillaShake.get())
    meal21 = float(varStrawberryShake.get())

    varTotal.set(meal1 + meal2)


# -------------------------------------FRAME ONE----------------------------------------------------------

lblMeal = Label(f1,font = ('arial',20,'bold'),text = "Fast Meal & Vegetarian\t\n    ")#.pack(side = TOP)
lblMeal.grid(row = 0, column = 0)

Fries = Checkbutton(f1,text = 'Fries\t\t\t?50', variable = var1, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'), command = chkFries).grid(row = 1,column = 0,sticky  = W)
txtFries = Entry(f1,font = ('arial',18,'bold'),textvariable =  varFries,width = 6,justify = 'right', state = DISABLED)
txtFries.grid(row = 1, column = 1)

Salad = Checkbutton(f1,text = 'Salad\t\t\t?30', variable = var2, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command = chkSalad).grid(row = 2,column = 0,sticky  = W)
txtSalad = Entry(f1,font = ('arial',18,'bold'),textvariable =  varSalad,width = 6,justify = 'right' ,state = DISABLED)
txtSalad.grid(row = 2, column = 1)

Hamburger = Checkbutton(f1,text = 'Burger\t\t\t?55', variable = var3, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command = chkHamburger).grid(row = 3,column = 0,sticky  = W)
txtHamburger = Entry(f1,font = ('arial',18,'bold'),textvariable =  varHamburger,width = 6, justify = 'right',state = DISABLED)
txtHamburger.grid(row = 3, column = 1)


OnionRings = Checkbutton(f1,text = 'OnionRings\t\t?35', variable = var4, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command = chkOnionRings).grid(row = 4,column = 0,sticky  = W)
txtOnionRings = Entry(f1,font = ('arial',18,'bold'),textvariable =  varOnionRings,width = 6, justify = 'right', state = DISABLED)
txtOnionRings.grid(row = 4, column = 1)

ChickenSalad = Checkbutton(f1,text = 'ChickenSalad\t\t?100', variable = var5, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command = chkChickenSalad).grid(row = 5,column = 0,sticky  = W)
txtChickenSalad = Entry(f1,font = ('arial',18,'bold'),textvariable =  varChickenSalad ,width = 6, justify = 'right', state = DISABLED)
txtChickenSalad.grid(row = 5, column = 1)

lblSandwich = Label(f1,font = ('arial',20,'bold'),text = "\nSandwich\n    ")#.pack(side = TOP)
lblSandwich.grid(row = 6 , column = 0)


ChickenSandwich = Checkbutton(f1,text = 'ChickenSandwich\t\t?70', variable = var6, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command = chkChickenSandwich).grid(row = 7,column = 0,sticky  = W)
txtChickenSandwich = Entry(f1,font = ('arial',18,'bold'),textvariable =  varChickenSandwich,width = 6, justify = 'right',state = DISABLED)
txtChickenSandwich.grid(row = 7, column = 1)

CheeseSandwich = Checkbutton(f1,text = 'CheeseSandwich\t\t?60', variable = var7, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command = chkCheeseSandwich).grid(row = 8,column = 0,sticky  = W)
txtCheeseSandwich = Entry(f1,font = ('arial',18,'bold'),textvariable =  varCheeseSandwich,width = 6, justify = 'right', state = DISABLED)
txtCheeseSandwich.grid(row = 8, column = 1)

FishSandwich = Checkbutton(f1,text = 'FishSandwich\t\t?90', variable = var8, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command = chkFishSandwich).grid(row = 9,column = 0,sticky  = W)
txtFishSandwich = Entry(f1,font = ('arial',18,'bold'),textvariable =  varFishSandwich,width = 6, justify = 'right',state = DISABLED)
txtFishSandwich.grid(row = 9, column = 1)

lblSpace = Label(f1,text = "\n\n\n\n\n\n\n\n\n")
lblSpace.grid(row = 10 , column = 0)

#--------------------------------------------FRAME 2 Top--------------------------------------------------------

lblMeal = Label(f2Top,font = ('arial',18 ,'bold'),text = "Desserts\n ")#.pack(side = TOP)
lblMeal.grid(row = 0, column = 0)

HashBrown = Checkbutton(f2Top,text = 'Hash Brown\t\t?3', variable = var9, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'), command = chkHashBrown).grid(row = 1,column = 0,sticky  = W)
txtHashBrown = Entry(f2Top,font = ('arial',18,'bold'),textvariable =  varHashBrown,width = 6,justify = "right", state = DISABLED)
txtHashBrown.grid(row = 1, column = 1)

ToastedBage1 =  Checkbutton(f2Top,text = 'ToastedBage1', variable = var10, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command = chkToastedBage1).grid(row = 2,column = 0,sticky  = W)
txtToastedBage1 = Entry(f2Top,font = ('arial',18,'bold'),textvariable =  varToastedBage1,width = 6,justify = 'right',state = DISABLED)
txtToastedBage1.grid(row = 2, column = 1)

PancakesSyrup= Checkbutton(f2Top,text = 'PancakeSyrup', variable = var11, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command = chkPancakesSyrup).grid(row = 3,column = 0,sticky  = W)
txtPancakesSyrup = Entry(f2Top,font = ('arial',18,'bold'),textvariable =  varPineappleStick,width = 6, justify = 'right', state = DISABLED)
txtPancakesSyrup.grid(row = 3, column = 1)
#
PineappleStick = Checkbutton(f2Top,text = 'PineappleStick', variable = var12, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command = chkPineappleStick).grid(row = 4,column = 0,sticky  = W)
txtPineappleStick = Entry(f2Top,font = ('arial',18,'bold'),textvariable =  varPineappleStick,width = 6, justify = 'right', state = DISABLED)
txtPineappleStick.grid(row = 4, column = 1)

ChocolateMuffin = Checkbutton(f2Top,text = 'ChocolateMuffin', variable = var13, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'), command= chkChocolateMuffin).grid(row = 5,column = 0,sticky  = W)
txtChocolateMuffin = Entry(f2Top,font = ('arial',18,'bold'),textvariable =  varChocolateMuffin,width = 6, justify = 'right',state = DISABLED)
txtChocolateMuffin.grid(row = 5, column = 1)

#------------------------------------------FRAME THIRD---------------------------------------------------------------


lblMeal = Label(f3,font = ('arial',18 ,'bold'),text = "Drinks\n ")#.pack(side = TOP)
lblMeal.grid(row = 0, column = 0)

Tea = Checkbutton(f3,text = 'Tea\t\t?40', variable = var14, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'), command= chkTea).grid(row = 1,column = 0,sticky  = W)
txtTea= Entry(f3,font = ('arial',18,'bold'),textvariable =  varTea,width = 6,justify = "left", state = DISABLED)
txtTea.grid(row = 1, column = 1)

ColdDrinks =  Checkbutton(f3,text = 'ColdDrinks\t?35', variable = var15, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'), command= chkColdDrinks).grid(row = 2,column = 0,sticky  = W)
txtColdDrinks = Entry(f3,font = ('arial',18,'bold'),textvariable =  varColdDrinks,width = 6,justify = 'left',state = DISABLED)
txtColdDrinks.grid(row = 2, column = 1)

Coffee = Checkbutton(f3,text = 'Coffee\t\t?45', variable = var16, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'), command = chkCoffee).grid(row = 3,column = 0,sticky  = W)
txtCoffee = Entry(f3,font = ('arial',18,'bold'),textvariable = varCoffee ,width = 6, justify = 'left', state = DISABLED)
txtCoffee.grid(row = 3, column = 1)

Juice = Checkbutton(f3,text = 'Juice\t\t?40', variable = var17, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'),command= chkJuice).grid(row = 4,column = 0,sticky  = W)
txtJuice = Entry(f3,font = ('arial',18,'bold'),textvariable =  varJuice,width = 6, justify = 'left', state = DISABLED)
txtJuice.grid(row = 4, column = 1)

WaterBottle = Checkbutton(f3,text = 'WaterBottle\t?30', variable = var18, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'), command = chkWaterBottle).grid(row = 5,column = 0,sticky  = W)
txtWaterBottle = Entry(f3,font = ('arial',18,'bold'),textvariable =  varWaterBottle,width = 6, justify = 'left',state = DISABLED)
txtWaterBottle.grid(row = 5, column = 1)

lblShakes = Label(f3,font = ('arial',20,'bold'),text = "\nShakes\n")
lblShakes.grid(row= 6,column = 0)

VanillaCone = Checkbutton(f3,text = 'Vanilla Cone\t?40', variable = var19, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'), command = chkVanillaCone).grid(row = 7,column = 0,sticky  = W)
txtVanillaCone = Entry(f3,font = ('arial',18,'bold'),textvariable =  varVanillaCone,width = 6, justify = 'left',state = DISABLED)
txtVanillaCone.grid(row = 7, column = 1)


VanillaShake = Checkbutton(f3,text = 'Vanilla Shakes\t?70', variable = var20, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'), command = chkVanillaShake).grid(row = 8,column = 0,sticky  = W)
txtVanillaShake = Entry(f3,font = ('arial',18,'bold'),textvariable =  varVanillaShake,width = 6, justify = 'left',state = DISABLED)
txtVanillaShake.grid(row = 8, column = 1)


StrawberryShake = Checkbutton(f3,text = 'Strawberry Shake  ?90', variable = var21, onvalue = 1, offvalue = 0,
                    font = ('arial',18,'bold'), command = chkStrawberryShake).grid(row = 9,column = 0,sticky  = W)
txtStrawberryShake = Entry(f3,font = ('arial',18,'bold'),textvariable =  varStrawberryShake,width = 6, justify = 'left',state = DISABLED)
txtStrawberryShake.grid(row = 9, column = 1)

lblSpace = Label(f3,text = "\n\n\n\n\n\n\n\n\n")
lblSpace.grid(row= 10 , column = 0)

#==================================================FRAME 2 BOTTOM ===========================================================

lblPaymentMethod = Label(f2Bottom,font = ('arial',14,'bold'),text = "Payment Method", bd= 10,width = 16, anchor= 'w')
lblPaymentMethod.grid(row = 0,column = 0)

lblChange = Label(f2Bottom,font = ('arial',18,'bold'),text = "Change",bd = 10,anchor = 'w')
lblChange.grid(row = 0,column = 1)
txtChange = Entry(f2Bottom,font = ('arial',18,'bold'),textvariable = varChange, width = 6, justify = 'right',state = DISABLED)
txtChange.grid(row = 0,column = 2)

cmbPaymentMethod = ttk.Combobox(f2Bottom,textvariable = var22,state = 'readonly',font = ('arial',10,'bold'),width = 20)
cmbPaymentMethod['value'] = ('Cash','Master Card','Visa Card','Debit Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row = 1, column = 0)

lblTax = Label(f2Bottom,font = ('arial',14,'bold'),text = "Tax  ", bd = 10,anchor  = 'w')
lblTax.grid(row = 1,column = 1)
txtTax = Entry(f2Bottom,font = ('arial',18,'bold'),textvariable = varSubTotal,width = 6, justify = 'right',state = DISABLED)
txtTax.grid(row = 1,column = 2)

txtPayment = Entry(f2Bottom,font = ('arial',18,'bold'),textvariable = varChange,width = 6, justify = 'right',state = DISABLED)
txtPayment.grid(row = 2,column = 0)
lblSubTotal = Label(f2Bottom,font = ('arial',14,'bold'),text = "Sub Total", bd = 10, width = 8 ,anchor = 'w')
lblSubTotal.grid(row = 2,column =1 )
txtSubTotal = Entry(f2Bottom,font = ('arial',18, 'bold'),textvariable = varSubTotal,width = 6,justify = 'right',state =DISABLED)
txtSubTotal.grid(row = 2, column = 2)

lblTotal = Label(f2Bottom,font = ('arial',14,'bold'),text = "Total", bd = 10, width = 6 ,anchor = 'w')
lblTotal.grid(row = 3,column =1 )
txtTotal = Entry(f2Bottom,font = ('arial',14,'bold'),text = 'Total' ,bd= 10,width = 6,justify = 'right',state = DISABLED)
txtTotal.grid(row= 3 ,column = 2)

# ================================================= FRAME 2 BUTTON==================================================

btnTotal = Button(f2Bottom,padx = 16,pady = 1,bd= 4,fg = "black",font = ('arial',16,'bold'),width =5,
                  text = "Total ", command =  costofmeal).grid(row = 4,column =0)

btnReset = Button(f2Bottom,padx = 16,pady = 1,bd= 4,fg = "black",font = ('arial',16,'bold'),width =5,
                  text = "Reset ", command = Reset).grid(row = 4,column =1)

btnExit = Button(f2Bottom,padx = 16,pady = 1,bd= 4,fg = "black",font = ('arial',16,'bold'),width =5,
                  text = "Exit ",command = lambda: iExit()).grid(row = 4,column =  2)
labSpace = Label(f2Bottom,text = "\n\n\n\n\n\n\n")
labSpace.grid(row = 5,column = 0)



root.mainloop()