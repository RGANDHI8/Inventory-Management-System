from tkinter import*
from PIL import Image, ImageTk  ##using pilllow library
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self,root):        ##default constructor
        self.root = root  
        self.root.geometry("1100x500+250+140")  ##length x width + x-axis + y-axis
        self.root.title("Inventory Management System")
        self.root.config(bg="lightyellow")
        self.root.focus_force()
        #================================================= 
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)

        ##title
        title = Label(product_Frame, text="Manage Products Details", font = ("times new roman",18), bg="#03045E",fg="white").pack(side=TOP,fill=X)
        #=== column 1
        lbl_category= Label(product_Frame, text="Category", font = ("times new roman",18), bg="white").place(x=30,y=60)
        lbl_supplier= Label(product_Frame, text="Supplier", font = ("times new roman",18), bg="white").place(x=30,y=110)
        lbl_product_name= Label(product_Frame, text="Name", font = ("times new roman",18), bg="white").place(x=30,y=160)
        lbl_price= Label(product_Frame, text="Category", font = ("times new roman",18), bg="white").place(x=30,y=210)
        lbl_qty= Label(product_Frame, text="Quantity", font = ("times new roman",18), bg="white").place(x=30,y=260)
        lbl_status= Label(product_Frame, text="Status", font = ("times new roman",18), bg="white").place(x=30,y=310)


        ##== column 2
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list,state='readonly',justify=CENTER, font=("times new roman",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)  


        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.sup_list,state='readonly',justify=CENTER, font=("times new roman",15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)  

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("times new roman",15),bg='lightyellow').place(x=150,y=160,width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("times new roman",15),bg='lightyellow').place(x=150,y=210,width=200)
        txt_sqty = Entry(product_Frame, textvariable=self.var_qty, font=("times new roman",15),bg='lightyellow').place(x=150,y=260,width=200)
        
        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active","Inactive"),state='readonly',justify=CENTER, font=("times new roman",15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)  


        ##buttons
        #btn_save = Button(product_Frame, text="Save",command=self.Save, font = ("times new roman",15), bg="#03045E",fg="white", cursor="hand2").place(x= 10,y=400, width=100,height=40) 
        #btn_update = Button(product_Frame, text="Update",command=self.Update,font = ("times new roman",15), bg="#03045E",fg="white", cursor="hand2").place(x= 120,y=400, width=100,height=40) 
        #btn_delete = Button(product_Frame, text="Delete",command=self.delete, font = ("times new roman",15), bg="#03045E",fg="white", cursor="hand2").place(x= 230,y=400, width=100,height=40) 
        #btn_clear = Button(product_Frame, text="Clear",command=self.clear, font = ("times new roman",15), bg="#03045E",fg="white", cursor="hand2").place(x= 340,y=400, width=100,height=40) 

        