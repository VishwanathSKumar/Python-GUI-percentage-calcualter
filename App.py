#This is an app for calculatint the perctage of the different subjects of the cycle test .
#This program is a GUI based program and has a GUI interface.

#Importing the packages.
import tkinter as tk


#Initilizing the package and making the variable need to the program
window = tk.Tk()


#Getting the marks.
#Window properties.
window.geometry("400x500")
window.title("Percentage calculator")

lable = tk.Label(window, text ="Enter the marks",font ={'Arial',10}).pack(pady=10) # type: ignore


#Generating the variable.
eng1_mark = tk.DoubleVar()
eng2_mark = tk.DoubleVar()
phy_mark = tk.DoubleVar()
chem_mark = tk.DoubleVar()
bio_mark = tk.DoubleVar()
his_mark = tk.DoubleVar()
geo_mark = tk.DoubleVar()
comp_mark = tk.DoubleVar()
math_mark = tk.DoubleVar()
hindi_mark = tk.DoubleVar()
max_mark_main = tk.DoubleVar()
total_percentage = 0.0
 

#English-I marks entry
English1 = tk.Label(window,text = "English-I ",font={'Arial',5}).place(x=60,y=59) # type: ignore
entry = tk.Entry(window,textvariable=eng1_mark).place(x=200,y=60)


#English-II marks entry
English2 = tk.Label(window,text = "English-II ",font={'Arial',5}).place(x=60,y=89) # type: ignore
entry1 = tk.Entry(window,textvariable=eng2_mark).place(x=200,y=90)


#Physics marks entry
Physics = tk.Label(window,text = "Physics ",font={'Arial',5}).place(x=60,y=119) # type: ignore
entry2 = tk.Entry(window,textvariable=phy_mark).place(x=200,y=120)

#Chemistry marks entry
Chemistry = tk.Label(window,text = "Chemistry ",font={'Arial',5}).place(x=60,y=149) # type: ignore
entry3 = tk.Entry(window,textvariable=chem_mark).place(x=200,y=150)

#Biology marks entry
Biology = tk.Label(window,text = "Biology ",font={'Arial',5}).place(x=60,y=179) # type: ignore
entry4 = tk.Entry(window,textvariable=bio_mark).place(x=200,y=180)

#History marks entry
History = tk.Label(window,text = "History ",font={'Arial',5}).place(x=60,y=209) # type: ignore
entry5 = tk.Entry(window,textvariable=his_mark).place(x=200,y=210)

#Geography marks entry
Geography = tk.Label(window,text = "Geography ",font={'Arial',5}).place(x=60,y=239) # type: ignore
entry6 = tk.Entry(window,textvariable=geo_mark).place(x=200,y=240)

#Computer marks entry
Computer = tk.Label(window,text = "Computer ",font={'Arial',5}).place(x=60,y=269) # type: ignore
entry7 = tk.Entry(window,textvariable=comp_mark).place(x=200,y=270)

#Mathematics marks entry
Mathematics = tk.Label(window,text = "Mathematics ",font={'Arial',5}).place(x=60,y=299) # type: ignore
entry8 = tk.Entry(window,textvariable=math_mark).place(x=200,y=300)

#Hindi language marks entry
Hindi = tk.Label(window,text = "Hindi ",font={'Arial',5}).place(x=60,y=329) # type: ignore
entry9 = tk.Entry(window,textvariable=hindi_mark).place(x=200,y=330)


#total number to be calculated to .
max_mark = tk.Label(text="Enter max mark",font={'Arial',5}).place(x=20,y=370) # type: ignore
max_entry = tk.Entry(window,textvariable=max_mark_main).place(x=200,y=370)  

#Total percentage
Total_Percentage = tk.Label(window,text = "The total percentage scored by you is",font={'Arial',10}).place(x=20,y=410) # type: ignore 


#Entry of the marks
def entry_marks():
   #marks entry
   eng1 = eng1_mark.get()
   eng1_mark.set(0.0)
   eng2 = eng2_mark.get()
   eng2_mark.set(0.0)
   phy = phy_mark.get()
   phy_mark.set(0.0)
   chem = chem_mark.get()
   chem_mark.set(0.0)
   bio = bio_mark.get()
   bio_mark.set(0.0)
   his = his_mark.get()
   his_mark.set(0.0)
   geo = geo_mark.get()
   geo_mark.set(0.0)
   comp = comp_mark.get()
   comp_mark.set(0.0)
   math = math_mark.get()
   math_mark.set(0.0)
   hindi = hindi_mark.get()
   hindi_mark.set(0.0)
   max = max_mark_main.get()
   max_mark_main.set(0.0)

   #percantage calcuation
   lang_avg = (eng1+eng2)/2
   sci_avg = (phy+chem+bio)/3
   sst_avg = (his+geo)/2
   total_percentage = ((lang_avg+sci_avg+sst_avg+comp+math+hindi)/max)*100
   percentage = tk.Label(window,text=total_percentage,font={'Arial',5}).place(x=300,y=410) # type: ignore


Calculate = tk.Button(window, text='Caculate the percenteage',font={'Arial',10},bg="red",command = entry_marks) #type: ignore
Calculate.pack(side=tk.BOTTOM,pady=10)



#Window execution.
window.mainloop()