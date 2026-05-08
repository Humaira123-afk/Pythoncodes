import tkinter as tk 
from time import strftime #strftime => time and date import ko direct use krskte

root = tk.Tk() #root nam ka obj create
root.title ("Digital Clock")

#time and date ko update kraga
def time():
    string = strftime  ('%H : %M : %S \n  %D' )
    label.config(text = string)
    label.after(1000, time) #hr second time chng

label =  tk.Label(root, font= ('calibiri' , 50 , 'bold'), background= 'yellow', foreground= 'black')
label.pack (anchor= 'center') #lbel obj ko pack method mai paste , center mai align krega

time()
#user interfa ko update krta hai

root.mainloop()

