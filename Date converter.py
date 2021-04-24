import tkinter as tk

isclicked = False

def isLeapYear(year):

    leapyear = False
    if year % 4 == 0 or year % 400 == 0:
        if year % 100 != 0:
            leapyear = True
    
    return leapyear

def convertdate():

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday"]
    monthsanddays = {'1' : 0, '2' : 31, '3' : 59, '4' : 90,
                     '5' : 120, '6' : 151, '7' : 181, '8' : 212,
                     '9' : 243, '10' : 273, '11' : 304, '12' : 334 }
    
    date = ent_date.get()
    m,d,y = date.split('/')
    
    years = int(y) - 2020
    days = years * 365
    days += years // 4
    days -= years // 100
    days += years // 400

    days += monthsanddays[m]
    days += int(d)

    # Correction for current year, if leap year
    if(int(m) <= 2 and isLeapYear(int(y))):
        days -= 1

    if ((int(y) == 1752) and (int(m) == 9) and (int(d) > 2) and (int(d) < 14)):
        output["text"] = "This day doesn't exist because of the change from the Julian to the Gregorian Calendar."
        
    elif ((int(y) <= 1752) and (int(m) <= 9) and (int(d) <= 2)):
        dayofweek = (days) % 7 # Julian to Gregorian calendar adjustment
        output["text"] = weekdays[dayofweek]
    else:
        dayofweek = (3 + days) % 7 # Jan 1, 2020 is a Wednesday
        output["text"] = weekdays[dayofweek]
        
window = tk.Tk()
window.title("date converter")

frm_entry = tk.Frame(master=window)
lbl_date = tk.Label(master=frm_entry, text="enter a date")
ent_date = tk.Entry(master=frm_entry, width = 10)
output = tk.Label(master=frm_entry, text="giraffe")

btn_convert = tk.Button(
    master=window,
    text='Convert',
    command=convertdate
)

lbl_date.grid(row=0, column=0, sticky="w")
ent_date.grid(row=0,column=1, sticky='e')
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=1,column=0, pady=10)
output.grid(row=0,column=2,sticky='e')
window.mainloop()








