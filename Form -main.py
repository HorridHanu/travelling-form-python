#CODE LANGUAGE IS PYTHON!
#CODE BY HANU!
#EDUCATIONAL PURPOSE ONLY!
#PROGRAME DATE : 29/JUNE/2021
#CODE FOR TRAVELLING FORM USING TKINTER!
#FORM ARE STORED IN  RECORD.TXT FILE!


from tkinter import *
root = Tk()


def submit():                                                                      #define function for submit!
    print(f"Name is : {nameval.get()}"
          f"\nGender is : {genderval.get()}"
          f"\nPhone number is : {phoneval.get()}"
          f"\nEmergency contact is:  {emergenceval.get()}"
          f"\nPayment mode is : {paymentmodeval.get()}"
          f"\nfood service if (yes-1) or (no-0): {foodserviceval.get()} \n")



    with open("record.txt", "a") as f:                                              #open and save file as record.txt!
        f.write(f"\nName is : {nameval.get()}"
          f"\nGender is : {genderval.get()}"
          f"\nPhone number is : {phoneval.get()}"
          f"\nEmergency contact is:  {emergenceval.get()}"
          f"\nPayment mode is : {paymentmodeval.get()}"
          f"\nfood service if (yes-1) or (no-0): {foodserviceval.get()}\n")



root.geometry("500x300")                                                           #geometery size
root.resizable(0, 0)                                                                #form can't resizeable
root.config(bg="white")                                                            #background color


Label(text="Welcome To Hanu Travellers!").grid(row=0, column=3)                     #welcome lable


#labels!
name = Label(root, text="Name: ", bg="white", fg="black").grid(row=1, column=2)
gender = Label(root, text="Gender: ", bg="white", fg="black").grid(row=2, column=2)
phone = Label(root, text="Phone: ", bg="white", fg="black").grid(row=3, column=2)
emergence = Label(root, text="Emergence contact: ", bg="white", fg="black").grid(row=4, column=2)
paymentmode = Label(root, text="Paymentmode: ", bg="white", fg="black").grid(row=5, column=2)


#variables for talking input!
nameval = StringVar()                                                              #storing the name in nameval!
genderval = StringVar()                                                            #storing the gender in genderval!
phoneval = StringVar()                                                             #storing the contact in contactval!
emergenceval = StringVar()                                                         #storing the emergency no. in emergencyval!
paymentmodeval = StringVar()                                                       #storing the paymentmode in paymentmodeval!
foodserviceval = IntVar()                                                          #storing the foodservice in foodservicevalval!


#enteries from Stringvar()!
namentry = Entry(root, textvariable=nameval).grid(row=1, column=3)
genderentry = Entry(root, textvariable=genderval).grid(row=2, column=3)
phonentry = Entry(root, textvariable=phoneval).grid(row=3, column=3)
emergencyentry = Entry(root, textvariable=emergenceval).grid(row=4, column=3)
paymentmodentry = Entry(root, textvariable=paymentmodeval).grid(row=5, column=3)


# checkbutton!
foodservice = Checkbutton(text="want to prebook food?", variable=foodserviceval).grid(row=6,column=3)                     #check button for food service!

Button(text="SUBMIT", bg="red", fg="white", command=submit).grid()                                                         #submit button!



root.mainloop()