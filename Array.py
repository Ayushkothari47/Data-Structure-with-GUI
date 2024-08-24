import customtkinter as ctk

root = ctk.CTk()
root.title('Array')
root.geometry('1020x1080')

screenWidth = root.winfo_screenwidth()

arr = []

def arrayInput():
    try:
        n = int(input("\nEnter Array Length: "))
        if n>25 or n<=0:
            print("\nArray size must be in range between 1-25")
            input()
            arrayInput()
    except ValueError:
        print("\nInvalid value !")
        input()
        arrayInput()
    
    i=0
    while i<n:
        try:
            val = int(input("\nEnter value: "))
            arr.append(val)
            i+=1
        except ValueError:
            print("\nInvalid value !")
            input()

arrayInput()


mainframe = ctk.CTkFrame(master=root,fg_color='white')
mainframe.pack(expand='true',fill='both')

arrayLable = ctk.CTkLabel(mainframe,text='AN ARRAY',text_color='red',font=('default',25,'bold'))
arrayLable.place(x=screenWidth//2 - len(arr)*3, y=100) 

subframe = ctk.CTkFrame(mainframe,fg_color='white',height=400,width=1000)
subframe.pack(pady=(200,200))

i=0
while i<len(arr):
    indexFrame = ctk.CTkFrame(master=subframe, border_width=1, border_color='red', height=40, width=40,fg_color='red')
    indexFrame.pack(anchor='center',side='left',padx=(2,2))
    indexData = ctk.CTkLabel(master=indexFrame, text=arr[i],height=40, width=40 ,text_color='white',font=('default',18,'bold'))
    indexData.pack(fill='both',expand=True, side='bottom')

    indexData = ctk.CTkLabel(master=indexFrame, text=i,height=40, width=40 ,fg_color='white',text_color='blue',font=('default',18,'bold'))
    indexData.pack(fill='both',expand=True)

    i+=1 

root.mainloop()
