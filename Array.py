import customtkinter as ctk
from tkinter import messagebox

root = ctk.CTk()
root.title("Array")
root.geometry('500x500')

screenHeight = root.winfo_screenheight()
screenWidth = root.winfo_screenwidth()

arr = []

def error(errorName):
    if errorName=='INVALID_INPUT':
        messagebox.showinfo("Error","Invalid value type ")
    

def insert():
    global arr
    try:
        val = valueInput.get()

        if val.isnumeric():
            arr.append(val)
        
        else:
            error('INVALID_INPUT')

    except ValueError:
        print("\nInvalid value !")
        
    
    print("Array: ",arr)

    update()

def clearDiagram():
    for widget in digramFrame.winfo_children():
        widget.destroy()

def update():
    clearDiagram()
    i=0
    while i<len(arr):
        indexFrame = ctk.CTkFrame(master=digramFrame, border_width=1, border_color='red', height=40, width=40,fg_color='red')
        indexFrame.pack(anchor='center',side='left',padx=(2,2),pady=(50,50))
        indexData = ctk.CTkLabel(master=indexFrame, text=arr[i],height=40, width=40 ,text_color='white',font=('default',18,'bold'))
        indexData.pack(fill='both',expand=True, side='bottom')

        indexData = ctk.CTkLabel(master=indexFrame, text=i,height=40, width=40 ,fg_color='white',text_color='blue',font=('default',18,'bold'))
        indexData.pack(fill='both',expand=True)

        i+=1 

mainframe = ctk.CTkFrame(master=root,fg_color='white')
mainframe.pack(expand='true',fill='both')

digramFrame = ctk.CTkFrame(master=mainframe,fg_color='white',width=screenWidth,height=screenHeight*60//100)
digramFrame.pack()

valueLable = ctk.CTkLabel(mainframe, text="Value: ",height=30,text_color='black',font=('default',18,'bold'))
valueLable.pack(padx=(screenWidth*10//100,screenWidth*1//100),side='left')

valueInput = ctk.CTkEntry(mainframe,fg_color='black',text_color='white',font=('default',18,'bold'))
valueInput.pack(side='left')

insertBtn = ctk.CTkButton(mainframe,text='Insert',fg_color='purple',text_color='white',command=insert)
insertBtn.pack(side='left')

root.mainloop()