import customtkinter as ctk
from tkinter import messagebox

root = ctk.CTk()
root.title("Stack")
root.geometry('500x500')
screenHeight = root.winfo_screenheight()
screenWidth = root.winfo_screenwidth()
stack = []

def error(errorName):
    if errorName=='INVALID_INPUT':
        messagebox.showinfo("Error","Invalid value type ")
    elif errorName=='UNDERFLOW':
        messagebox.showinfo("Error","Case: Underflow")
    elif errorName=='OVERFLOW':
        messagebox.showinfo("Error","Case: Overflow")

    
def push():
    global stack
    try:
        val = valueInput.get()
        if val.isnumeric():
            if len(stack)>15:
                error('OVERFLOW')
            else:
                stack.append(val)
                update()
        else:
            error('INVALID_INPUT')
    except ValueError:
        error('INVALID_INPUT')
    
    

def pop():
    global stack
    
    try:
        val = stack[len(stack)-1]
        found = 0
        if val.isnumeric():
            for i in stack:
               if i==val:
                   stack.remove(i)
                   found = 1
                   break
            
            if found==0:
                error('VALUE_NOT_EXIST')
            else:
                update()
        else:
            error('INVALID_INPUT')
    except ValueError:
        error('INVALID_INPUT')
    except IndexError:
        error('UNDERFLOW')
    

def clearDiagram():
    for widget in digramFrame.winfo_children():
        widget.destroy()

def update():
    clearDiagram()
    if len(stack)==0:
        text = ctk.CTkLabel(digramFrame,text="Stack is Empty !",text_color='red',font=('default',18,'bold'))
        text.pack(pady=(100,0))

    i=0
    while i<len(stack):
        indexFrame = ctk.CTkFrame(master=digramFrame, border_width=1, border_color='red', height=40, width=40,fg_color='red')
        indexFrame.pack(anchor='center',side='left',padx=(2,2),pady=(50,50))
        indexData = ctk.CTkLabel(master=indexFrame, text=stack[i],height=40, width=40 ,text_color='white',font=('default',18,'bold'))
        indexData.pack(fill='both',expand=True, side='bottom')

        indexData = ctk.CTkLabel(master=indexFrame, text=i,height=40, width=40 ,fg_color='white',text_color='blue',font=('default',18,'bold'))
        indexData.pack(fill='both',expand=True)

        i+=1 

mainframe = ctk.CTkFrame(master=root,fg_color='white')
mainframe.pack(expand='true',fill='both')

digramFrame = ctk.CTkFrame(master=mainframe,fg_color='white',width=screenWidth,height=screenHeight*60//100)
digramFrame.pack()

inputFrame = ctk.CTkFrame(mainframe,fg_color='white')
inputFrame.pack(expand=True)



valueInput = ctk.CTkEntry(inputFrame,fg_color='black',text_color='white',font=('default',15,),placeholder_text='Enter Value here ',placeholder_text_color='white',height=40,width=120)
valueInput.pack(side="left", padx=10, pady=10)

pushBtn = ctk.CTkButton(inputFrame,text='PUSH',fg_color='green',text_color='white',command=push)
pushBtn.pack(side="left", padx=10, pady=10)

popBtn = ctk.CTkButton(inputFrame,text='POP',fg_color='red',text_color='white',command=pop)
popBtn.pack(side='left',padx=10, pady=10)

update()

root.mainloop()