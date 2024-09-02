import customtkinter as ctk
import math


root = ctk.CTk()
root.title('Binary Search Tree')
root.geometry('500x500')

totalLevel = 0

def drawRoot(node, frame, parentNodeWidth, parentNodeHeight):
    circle_diameter = 60
    canvas = ctk.CTkCanvas(frame, width=circle_diameter, height=circle_diameter, bg="white", highlightthickness=1)
    canvas.place(x=parentNodeWidth,y=parentNodeHeight)
    
    x1 = 0
    y1 = 0
    x2 = circle_diameter
    y2 = circle_diameter
    canvas.create_oval(x1, y1, x2, y2, outline="green", fill="green", width=2)


    text_x = circle_diameter / 2
    text_y = circle_diameter / 2
    canvas.create_text(text_x, text_y, text=node.data, fill="white", font=("Arial", 20))

    return


def drawLeft(node,frame,parentNodeWidth, parentNodeHeight):
    
    circle_diameter = 60
    
    canvas = ctk.CTkCanvas(frame, width=circle_diameter, height=circle_diameter, bg="white",highlightthickness=1)
    canvas.place(x=parentNodeWidth+30,y=parentNodeHeight)

    x1=0
    y1=0
    x2=circle_diameter
    y2=circle_diameter

    canvas.create_oval(x1, y1, x2, y2, outline="green", fill="green", width=2)

    text_x=circle_diameter/2
    text_y=circle_diameter/2

    canvas.create_text(text_x,text_y, text=node.data,fill="white", font=("Arial", 20))

    return


def drawRight(node,frame,parentNodeWidth, parentNodeHeight):
    circle_diameter = 60

    
    canvas = ctk.CTkCanvas(frame, width=circle_diameter, height=circle_diameter, bg="white",highlightthickness=1)
    canvas.place(x=parentNodeWidth-30,y=parentNodeHeight)


    x1=0
    y1=0
    x2=circle_diameter
    y2=circle_diameter

    
    canvas.create_oval(x1, y1, x2, y2, outline="green", fill="green", width=2)

    text_x=circle_diameter/2
    text_y=circle_diameter/2

    canvas.create_text(text_x,text_y, text=node.data,fill="white", font=("Arial", 20))

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
                        print("")
                        print(currNode.left.data,"Inserted Successfully ")
                        break
                
                else:
                    if currNode.right!=None:
                        currNode = currNode.right
                    else:
                        currNode.right = newNode
                        print("")
                        print(currNode.right.data,"Inserted Successfully ")
                        break
        
        

    
    def preOrderTraversal(self,root,mainFrame,rootNodeGap,parentNodeWidth,parentNodeHeight):
        if root is None:
            return

        else:
            if root.left!=None:
                leftChildNodeHeight = parentNodeHeight + 100
                leftChildNodeWidth = parentNodeWidth - rootNodeGap
                drawLeft(root.left,mainFrame,leftChildNodeWidth,leftChildNodeHeight)
            
            else:
                leftChildNodeHeight = parentNodeHeight
                leftChildNodeWidth = parentNodeWidth


                    
            if root.right!=None:
                rightChildNodeHeight = parentNodeHeight + 100
                rightChildNodeWidth = parentNodeWidth + rootNodeGap
                drawRight(root.right,mainFrame,rightChildNodeWidth,rightChildNodeHeight)
            
            else:
                rightChildNodeHeight = parentNodeHeight+100
                rightChildNodeWidth = parentNodeWidth
            
            rootNodeGap-=100
            self.preOrderTraversal(root.left,mainFrame,rootNodeGap,parentNodeWidth=leftChildNodeWidth,parentNodeHeight=leftChildNodeHeight)
            self.preOrderTraversal(root.right,mainFrame,rootNodeGap,parentNodeWidth=rightChildNodeWidth,parentNodeHeight=rightChildNodeHeight)
            
            
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

            rootNodeGap = H*100

            mainFrame = ctk.CTkFrame(master=root,fg_color='white')
            mainFrame.pack(expand=True, fill='both')
            treeTitle = ctk.CTkLabel(master=mainFrame, text='Binary Search Tree',font=('default',20,'bold'), text_color='green')
            treeTitle.pack(pady=(50))

            parentNodeWidth = int(root.winfo_screenwidth()//1.4)
            parentNodeHeight = int(root.winfo_screenheight()//4)

            print(f"Top Root node coordinates({parentNodeWidth,parentNodeHeight})")

            if MainNode!=None:
                drawRoot(currNode,mainFrame,parentNodeWidth,parentNodeHeight)
                self.preOrderTraversal(currNode,mainFrame,rootNodeGap,parentNodeWidth,parentNodeHeight)         
                root.mainloop()


tree = Tree()

menu ='''
    1. Insert
    2. Display Tree
 
'''

while True:
    print(menu)
    try:
        ch = int(input("\nEnter Chocie: "))

        if ch==1:
            data = int(input("\nEnter Data: "))
            n = Node(data)
            tree.insert(n)
    
        elif ch==2:
            tree.display()
        
        else:
            print("\nInvalid choice !")

    except ValueError: 
        print("\nInvalid value !")
    
    print("")
    input()







