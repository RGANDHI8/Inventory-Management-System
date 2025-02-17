from tkinter import*
from PIL import Image, ImageTk  ##using pilllow library
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):        ##default constructor
        self.root = root  
        self.root.geometry("1100x500+250+140")  ##length x width + x-axis + y-axis
        self.root.title("Inventory Management System")
        self.root.config(bg="#ADE8F4")
        self.root.focus_force()

        ##variable
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_icontact = StringVar()


        ##search frame

        SearchFrame = LabelFrame(self.root, text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE, bg="#90E0EF")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        ##options drop down
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER, font=("times new roman",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)  ##in order to let the 0th index gets selected as the default option

        txt_search = Entry(SearchFrame,textvariable=self.var_searchtxt, font = ("times new roman",15), bg="white").place(x=200,y=10) 
        btn_search = Button(SearchFrame, text="Search",font = ("times new roman",15), bg="#03045E",fg="white", cursor="hand2").place(x= 410,y=10, width=150,height=30) 

        ##title
        title = Label(self.root, text="Employee Details", font = ("times new roman",15), bg="#03045E",fg="white").place(x= 20,y=100, width=1050) 

        ##content
        ##row1
        lbl_emp_id = Label(self.root, text="Emp Id", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 50,y=150) 
        lbl_emp_gender = Label(self.root, text="Gender", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 350,y=150) 
        lbl_emp_contact = Label(self.root, text="Contact", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 750,y=150) 

        txt_emp_id = Entry(self.root, textvariable=self.var_sup_invoice, font = ("times new roman",15), bg="white",fg="black").place(x= 150,y=150,width=180) 
        
        ##txt_emp_gender = Entry(self.root, textvariable=self.var_emp_gender, font = ("times new roman",15), bg="white",fg="black").place(x= 500,y=150,width=180) 
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_emp_gender, values=("Select","Male","Female","Others"),state='readonly',justify=CENTER, font=("times new roman",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        txt_emp_contact = Entry(self.root, textvariable=self.var_emp_icontact, font = ("times new roman",15), bg="white",fg="black").place(x= 850,y=150,width=180) 


        ##row2
        lbl_emp_name = Label(self.root, text="Name", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 50,y=200) 
        lbl_emp_dob = Label(self.root, text="DOB", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 350,y=200) 
        lbl_emp_doj = Label(self.root, text="DOJ", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 750,y=200) 

        txt_emp_name = Entry(self.root, textvariable=self.var_emp_name, font = ("times new roman",15), bg="white",fg="black").place(x= 150,y=200,width=180) 
        txt_emp_dob = Entry(self.root, textvariable=self.var_emp_dob, font = ("times new roman",15), bg="white",fg="black").place(x= 500,y=200,width=180)  
        txt_emp_doj = Entry(self.root, textvariable=self.var_emp_doj , font = ("times new roman",15), bg="white",fg="black").place(x= 850,y=200,width=180) 


        ##row3
        lbl_emp_email = Label(self.root, text="Email", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 50,y=250) 
        lbl_emp_pass = Label(self.root, text="Password", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 350,y=250) 
        lbl_emp_utype = Label(self.root, text="User Type", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 750,y=250) 

        txt_emp_email = Entry(self.root, textvariable=self.var_emp_email, font = ("times new roman",15), bg="white",fg="black").place(x= 150,y=250,width=180) 
        txt_emp_pass = Entry(self.root, textvariable=self.var_emp_pass, font = ("times new roman",15), bg="white",fg="black").place(x= 500,y=250,width=180)  
        
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_emp_utype, values=("Select","Admin","Employee"),state='readonly',justify=CENTER, font=("times new roman",15))
        cmb_utype.place(x= 850,y=250,width=180)
        cmb_utype.current(0)

        ##row4
        lbl_address = Label(self.root, text="Address", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 50,y=300) 
        lbl_salary = Label(self.root, text="Salary", font = ("times new roman",15), bg="#ADE8F4",fg="black").place(x= 350,y=300) 

        self.txt_address = Text(self.root, font = ("times new roman",15), bg="white",fg="black")
        self.txt_address.place(x= 150,y=300,width=180,height=60) 
        ##we have used text method so as to to allow multiple line input in that field, however in entry method allows only for single line entry 
        txt_salary = Entry(self.root, textvariable=self.var_emp_salary, font = ("times new roman",15), bg="white",fg="black").place(x= 500,y=300,width=180) 

        ##buttons
        btn_save = Button(self.root, text="Save",font = ("times new roman",15), bg="#03045E",fg="white", cursor="hand2").place(x= 750,y=300, width=80,height=30) 
        btn_update = Button(self.root, text="Update",font = ("times new roman",15), bg="#03045E",fg="white", cursor="hand2").place(x= 850,y=300, width=80,height=30) 
        btn_delete = Button(self.root, text="Delete",font = ("times new roman",15), bg="#03045E",fg="white", cursor="hand2").place(x= 750,y=350, width=80,height=30) 
        btn_clear = Button(self.root, text="Clear",font = ("times new roman",15), bg="#03045E",fg="white", cursor="hand2").place(x= 850,y=350, width=80,height=30) 


        ##employee database treeview
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=400,relwidth=1,height=100)

        scrolly = Scrollbar(emp_frame, orient= VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid","name"))


    #########################################################################################
        
    def add(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Employee Id is required",parent=self.root)
            
            else:
                cur.execute("Select * from employee where eid = ?",(self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This id already assigned, try using different id")
                else:
                    cur.execute("Insert into employee (eid, name ,email ,gender ,contact ,dob ,doj ,pass ,utype ,addrress ,salary ) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.var_emp_name.get(),
                        self.var_emp_email.get(),
                        self.var_emp_gender.get(),
                        self.var_emp_icontact.get(),
                        self.var_emp_dob.get(),
                        self.var_emp_doj.get(),
                        self.var_emp_pass.get(),
                        self.var_emp_utype.get(),
                        self.var_emp_address.get('1.0',END),
                        self.var_emp_salary.get(),
                    ))

                    con.commit()
                    messagebox.showinfo("Sucess","Employee added successfully", parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


      


if __name__=="__main__":    
    root =Tk()              ##object of tkinter class
    obj = supplierClass(root)         ##object of IMS
    root.mainloop()         ##for the gui to stay