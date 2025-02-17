from tkinter import*
from PIL import Image, ImageTk  ##using pilllow library
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
class IMS:
    def __init__(self,root):        ##default constructor
        self.root = root  
        self.root.geometry("1450x800+0+0")  ##lengthxwidth+x-axis+y-axis
        self.root.title("Inventory Management System")

        ##title
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Inventory Management System",image=self.icon_title, compound=LEFT, font=("times new roman",40,"bold"),bg="#c72840",fg="white").place(x=0,y=0,relwidth=1,height = 70)
        ## relwidth denotes the relative width so that it takes the width of root and then adjust itself
        ## #6421b0 good color

        ##button
        btn_logout = Button(self.root,text="Logout", font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1250,y=13,height=50,width=130)

        ## clock

        ##left menu
        ## we will be ceating frame so that jo bhi widget we put up , we will put it in frame and not in root
        
        

        ## modifying, resizing the image 
        self.menuLogo = Image.open("images/menu_im.png")
        self.menuLogo = self.menuLogo.resize((200,200))  ##antialias resize kar dega but will not disturb the clarity
        self.menuLogo =ImageTk.PhotoImage(self.menuLogo)   ##its role is to open the resized image, now since we do not have idea of the location of the resized image thus we will be passing the whole name as it is

        leftMenu = Frame(self.root, bd= 2 , relief=RIDGE, bg="white")   ##relief basically specifies the type of border
        leftMenu.place(x=0,y=120,width=200,height=555)

        lbl_menuLogo = Label(leftMenu, image=self.menuLogo)  ##placing the image on left menu
        lbl_menuLogo.pack(side=TOP, fill=X)    ##filling will take the x axis apce of the menu

        ##designing the left menu buttons and labels
        ##button
        lbl_menu = Label(leftMenu,text="Menu", font=("times new roman",20,"bold"),bg="#009688").pack(side=TOP , fill=X)
        space = Frame(leftMenu, height=10).pack(side=TOP)
        self.icon_side = PhotoImage(file="images/side.png")
        btn_employee = Button(leftMenu,text="Employee", image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman",15,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP , fill=X)
        ##setting the anchor as west so that it does not come in center , basically setting its position
        space = Frame(leftMenu, height=10).pack(side=TOP) # Adjust the height as per your requirement   
        btn_supplier = Button(leftMenu,text="Supplier",command=self.supplier , image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman",15,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP , fill=X)
        space = Frame(leftMenu, height=10).pack(side=TOP)
        btn_category = Button(leftMenu,text="Category",command=self.category, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman",15,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP , fill=X)
        space = Frame(leftMenu, height=10).pack(side=TOP)
        btn_product = Button(leftMenu,text="Product",command=self.product, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman",15,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP , fill=X)
        space = Frame(leftMenu, height=10).pack(side=TOP)
        btn_sales = Button(leftMenu,text="Sales", image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman",15,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP , fill=X)
        space = Frame(leftMenu, height=10).pack(side=TOP)
        btn_exit = Button(leftMenu,text="Exit", image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman",15,"bold"),bg="white",bd=3,relief=RIDGE,cursor="hand2").pack(side=TOP , fill=X)

        ##content

        self.lbl_employee = Label(self.root, text="Total Employee\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20,"bold")) ## relief defines the type of border
        self.lbl_employee.place(x=300,y=120,height = 150, width=300)  ##since the left menu was placed at x axis of 200 thus placimg this at x axis of 300

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20,"bold")) ## relief defines the type of border
        self.lbl_supplier.place(x=650,y=120,height = 150, width=300)  ##since the left menu was placed at x axis of 200 thus placimg this at x axis of 300

        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20,"bold")) ## relief defines the type of border
        self.lbl_category.place(x=1000,y=120,height = 150, width=300)  ##since the left menu was placed at x axis of 200 thus placimg this at x axis of 300

        self.lbl_product = Label(self.root, text="Total Product\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20,"bold")) ## relief defines the type of border
        self.lbl_product.place(x=300,y=300,height = 150, width=300)  ##since the left menu was placed at x axis of 200 thus placimg this at x axis of 300

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style",20,"bold")) ## relief defines the type of border
        self.lbl_sales.place(x=650,y=300,height = 150, width=300)  ##since the left menu was placed at x axis of 200 thus placimg this at x axis of 300

        ##footer
        lbl_footer=Label(self.root,text="IMS-Inventory Management System")

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)



if __name__=="__main__":
    root =Tk()              ##object of tkinter class
    obj = IMS(root)         ##object of IMS
    root.mainloop()         ##for the gui to stay


##pillow library has been used to play around with any image extension










