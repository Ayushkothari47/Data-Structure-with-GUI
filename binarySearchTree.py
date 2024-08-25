import customtkinter as ctk
import math

root = ctk.CTk()
root.title('Binary Search Tree')
root.geometry('500x500')

totalLevel = 0

def drawRoot(node, frame, xCenter, yCenter):
    # Define the circle's diameter and canvas size


    circle_diameter = 100
    # Create the canvas with the size matching the circle's diameter
    canvas = ctk.CTkCanvas(frame, width=circle_diameter, height=circle_diameter, bg="white", highlightthickness=1)
    canvas.place(x=xCenter,y=yCenter+100)
    

    # Calculate the coordinates for the bounding box of the circle
    x1 = 0
    y1 = 0
    x2 = circle_diameter
    y2 = circle_diameter

    # Draw the circle (oval) on the canvas
    canvas.create_oval(x1, y1, x2, y2, outline="green", fill="green", width=2)

    # Draw the text inside the circle, centered
    text_x = circle_diameter / 2
    text_y = circle_diameter / 2
    canvas.create_text(text_x, text_y, text=node.data, fill="white", font=("Arial", 24))

    # Create and place a label in the frame (optional)
    # dataLabel = ctk.CTkLabel(frame, text=node.data, font=('default', 25, 'bold'), text_color='white', height=20, width=40)
    # dataLabel.pack()
    
    return


def drawLeft(node,frame,xCenter, yCenter):
    
    circle_diameter = 100
    
    canvas = ctk.CTkCanvas(frame, width=circle_diameter, height=circle_diameter, bg="white",highlightthickness=1)
    canvas.place(x=xCenter-100,y=yCenter+100)

    x1=0
    y1=0
    x2=circle_diameter
    y2=circle_diameter

    canvas.create_oval(x1, y1, x2, y2, outline="green", fill="green", width=2)

    text_x=circle_diameter/2
    text_y=circle_diameter/2

    canvas.create_text(text_x,text_y, text=node.data,fill="white", font=("Arial", 24))
    # dataLable = ctk.CTkLabel(frame, text=node.data, font=('default',25,'bold'), text_color='white',height=20,width=40)
    # dataLable.pack()
    return


def drawRight(node,frame,xCenter, yCenter):
    circle_diameter = 100
    
    canvas = ctk.CTkCanvas(frame, width=circle_diameter, height=circle_diameter, bg="white",highlightthickness=1)
    canvas.place(x=xCenter+100,y=yCenter+100)

    x1=0
    y1=0
    x2=circle_diameter
    y2=circle_diameter

    canvas.create_oval(x1, y1, x2, y2, outline="green", fill="green", width=2)

    text_x=circle_diameter/2
    text_y=circle_diameter/2

    canvas.create_text(text_x,text_y, text=node.data,fill="white", font=("Arial", 24))
    # dataLable = ctk.CTkLabel(frame, text=node.data, font=('default',25,'bold'), text_color='white',height=20,width=40)
    # dataLable.pack()
    return


class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self,newNode):
        if self.root is None:
            self.root = newNode
        
        else:
            currNode = self.root
            while True:
                if newNode.data < currNode.data:
                    if currNode.left!=None:
                        currNode = currNode.left
                    else:
                        currNode.left = newNode
                        break
                
                else:
                    if currNode.right!=None:
                        currNode = currNode.right
                    else:
                        currNode.right = newNode
                        break
        
        print("\nInserted Successfully ")

    
    def preOrderTraversal(self,root,mainFrame,xCenter,yCenter):
        if root is None:
            return

        else:
            if root.left!=None:
                xCenter-=100
                yCenter+=100
                drawLeft(root.left,mainFrame,xCenter,yCenter)

                    
            if root.right!=None:
                xCenter+=200
                drawRight(root.right,mainFrame,xCenter,yCenter)
            
            print(root.data, end=' ')
            xCenter-=200
            self.preOrderTraversal(root.left,mainFrame,xCenter,yCenter)
            xCenter+=200
            self.preOrderTraversal(root.right,mainFrame,xCenter,yCenter)
            
            
    def levelChecker(self,root):
        if root is None:
            return 
        else:
            global totalLevel
            self.levelChecker(root.left)
            self.levelChecker(root.right)
            totalLevel+=1



    def display(self):
        if self.root is None:
            print("Tree is empty, nothing to show !")
            return
        
        else:
            MainNode = self.root
            currNode = MainNode
            self.levelChecker(currNode)
            n = totalLevel
            H = int(math.log2(n+1))
            print("\nTotal Level: ",H)
            mainFrame = ctk.CTkFrame(master=root,fg_color='white')
            mainFrame.pack(expand=True, fill='both')
            treeTitle = ctk.CTkLabel(master=mainFrame, text='Binary Search Tree',font=('default',25,'bold'), text_color='green')
            treeTitle.pack(pady=(50))

            

            xCenter = root.winfo_screenwidth()//1.4
            yCenter = root.winfo_screenheight()//4

            
         
            if MainNode!=None:
                print("Drawing root")
                drawRoot(currNode,mainFrame,xCenter,yCenter)

                self.preOrderTraversal(currNode,mainFrame,xCenter,yCenter)         
                root.mainloop()


tree = Tree()

menu ='''
    1. Insert
    2. Display Tree
 
'''

while True:
    print(menu)
    ch = int(input("\nEnter Chocie: "))
    if ch==1:
        data = int(input("\nEnter Data: "))
        n = Node(data)
        tree.insert(n)

    elif ch==2:
        tree.display()
    
    else:
        print("\nInvalid choice !")
    
    print("")
    input()







