from tkinter import * # import tkinter
import datetime # import date and time module 

# print(datetime.datetime.now()) # current datetime

def date_time(): # func to define date and time and config them accordingly
    # time
    time = datetime.datetime.now()
    hr = time.strftime('%I') #gives current hour
    mi = time.strftime('%M') #gives current minutes
    sec = time.strftime('%S') #gives current seconds
    am = time.strftime('%p') #gives current am/pm

    #date
    date = time.strftime('%d')# gives current date
    month = time.strftime("%m")# gives current month
    year = time.strftime('%y')# gives current year
    day = time.strftime('%a')# gives current day


    #stores the current values of time
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)

    #stores the current values of date
    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    # important step
    lab_sec.after(200, date_time) #change data i.e. recalling program update time to  in milliseconds

 


#  class ko object ke andr call krenge and then graphics lagayenge
clock =Tk() #create object

clock.title('    *****Digital Clock*****')# title of window
clock.geometry('1000x500') #size
clock.config(bg='Yellow') #background color

# ******TIME*********
# HOUR BOX and labeland specifying their characteristics
lab_hr=Label(clock, text="00",font=('Times New Roman', 60,"bold"),
             bg='red', fg="white")
lab_hr.place(x=120, y=50, height=110, width=100)
lab_hr_text=Label(clock, text="Hour",font=('Times New Roman', 20,"bold"),
             bg='red', fg="white")
lab_hr_text.place(x=120, y=190, height=40, width=100)


# Minutes box and labeland specifying their characteristics
lab_min=Label(clock, text="00",font=('Times New Roman', 60,"bold"),
             bg='red', fg="white")
lab_min.place(x=340, y=50, height=110, width=100)
lab_min_text=Label(clock, text="Minutes",font=('Times New Roman', 20,"bold"),
             bg='red', fg="white")
lab_min_text.place(x=340, y=190, height=40, width=100)


# Seconds box and labeland specifying their characteristics
lab_sec=Label(clock, text="00",font=('Times New Roman', 60,"bold"),
             bg='red', fg="white")
lab_sec.place(x=560, y=50, height=110, width=100)
lab_sec_text=Label(clock, text="Seconds",font=('Times New Roman', 20,"bold"),
             bg='red', fg="white")
lab_sec_text.place(x=560, y=190, height=40, width=100)


# AM/PM box and label and specifying their characteristics
lab_am=Label(clock, text="00",font=('Times New Roman', 55,"bold"),
             bg='red', fg="white")
lab_am.place(x=780, y=50, height=110, width=100)
lab_am_text=Label(clock, text="AM/PM",font=('Times New Roman', 20,"bold"),
             bg='red', fg="white")
lab_am_text.place(x=780, y=190, height=40, width=100)

# ********DATE******
#date box and label with its characteristics
lab_date=Label(clock, text="00",font=('Times New Roman', 60,"bold"),
             bg='red', fg="white")
lab_date.place(x=120, y=270, height=110, width=100)
lab_date_text=Label(clock, text="Date",font=('Times New Roman', 20,"bold"),
             bg='red', fg="white")
lab_date_text.place(x=120, y=410, height=40, width=100)

# Month box and label wwith its characteristics
lab_mon=Label(clock, text="00",font=('Times New Roman', 60,"bold"),
             bg='red', fg="white")
lab_mon.place(x=340, y=270, height=110, width=100)
lab_mon_text=Label(clock, text="Month",font=('Times New Roman', 20,"bold"),
             bg='red', fg="white")
lab_mon_text.place(x=340, y=410, height=40, width=100)


# Year box and label with its characteristics
lab_year=Label(clock, text="00",font=('Times New Roman', 60,"bold"),
             bg='red', fg="white")
lab_year.place(x=560, y=270, height=110, width=100)
lab_year_text=Label(clock, text="Year",font=('Times New Roman', 20,"bold"),
             bg='red', fg="white")
lab_year_text.place(x=560, y=410, height=40, width=100)

# Day box and label with its characteristics
lab_day=Label(clock, text="00",font=('Times New Roman', 35,"bold"),
             bg='red', fg="white")
lab_day.place(x=780, y=270, height=110, width=100)
lab_day_text=Label(clock, text="Day",font=('Times New Roman', 20,"bold"),
             bg='red', fg="white")
lab_day_text.place(x=780, y=410, height=40, width=100)
#call the func date_time
date_time()


clock.mainloop() #on graphics(give graphics)

# Calculations for the allignment of clock labels to be done precisely



