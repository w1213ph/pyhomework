import tkinter as tk
from tkinter import ttk
from db import db
class aboutframe(tk.Frame):#关于页面
    def __init__(self,root):
        super().__init__(root)
        tk.Label(self, text='本程序由nwpu小辉制作').pack()
        tk.Label(self, text='因为刚开始学图形库，所以有些错误，请老师多多包涵').pack()

class changeframe(tk.Frame):#修改功能页面
    def __init__(self,root):#初始化
        super().__init__(root)
        self.name = tk.StringVar()
        self.sex = tk.StringVar()
        self.age = tk.StringVar()
        self.id= tk.StringVar()
        self.status = tk.StringVar()
        self.creat_page()

    def creat_page(self):#显示修改功能时的图形
        tk.Label(self).grid(row=0, pady=10)
        tk.Label(self, text="姓名：").grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)

        tk.Label(self, text="性别：").grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.sex).grid(row=2, column=2, pady=10)

        tk.Label(self, text="年龄：").grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.age).grid(row=3, column=2, pady=10)

        tk.Label(self, text="学号：").grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=4, column=2, pady=10)
        tk.Button(self, text="修改", command=self.change_user).grid(row=5, column=1, pady=10)
        tk.Button(self, text="查询", command=self.seacher_user).grid(row=5, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=6, column=2, pady=10, sticky=tk.E)
    def seacher_user(self):#查找函数，通过姓名

        flag,info=db.seacher_by_username(self.name.get())
        if flag:
            self.name.set(info['name'])
            self.sex.set(info['sex'])
            self.age.set(info['age'])
            self.id.set(info['id'])
            self.status.set("数据查询成功")
        else:
            self.status.set(info)
        pass
    def change_user(self):#修改数据功能
        stu = {"name": self.name.get(), "sex": self.sex.get(),
               "age": self.age.get(), "id": self.id.get()}
        print(stu)
        self.name.set('')
        self.sex.set('')
        self.age.set('')
        self.id.set('')
        print(stu)
        db.update(stu)
        self.status.set("修改数据成功")
        pass

class insertframe(tk.Frame):#插入数据功能
    def __init__(self,root):
        super().__init__(root)
      #  tk.Label(self, text='插入页面').pack()
        self.name=tk.StringVar()
        self.sex = tk.StringVar()
        self.age = tk.StringVar()
        self.id= tk.StringVar()
        self.status = tk.StringVar()
        self.creat_page()
    def creat_page(self):#插入数据页面展示
        tk.Label(self).grid(row=0,pady=10)
        tk.Label(self,text="姓名：").grid(row=1,column=1, pady=10)
        tk.Entry(self,textvariable=self.name).grid(row=1,column=2, pady=10)

        tk.Label(self, text="性别：").grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.sex).grid(row=2, column=2, pady=10)

        tk.Label(self, text="年龄：").grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.age).grid(row=3, column=2, pady=10)

        tk.Label(self, text="学号：").grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=4, column=2, pady=10)
        tk.Button(self,text="录入",command=self.recode_info).grid(row=5,column=2,pady=10)
        tk.Label(self,textvariable=self.status).grid(row=6,column=2,pady=10,sticky=tk.E)
    def recode_info(self):
        stu={"name":self.name.get(),"sex":self.sex.get(),
             "age":self.age.get(),"id":self.id.get()}
        print(stu)
        self.name.set('')
        self.sex.set('')
        self.age.set('')
        self.id.set('')

        db.insert(stu)
        self.status.set("插入数据成功")
class searchframe(tk.Frame):#查找功能
    def __init__(self,root):
        super().__init__(root)

        self.table_view =tk.Frame()
        self.table_view.pack()
        self.create_page()
    def create_page(self):#查找页面显示
        column=("name","sex","age","id")
        columns_values=("姓名","性别","年龄","学号")
        self.tree_view = ttk.Treeview(self, show='headings' , columns=column)
        self.tree_view.column('name', width=80, anchor='center')
        self.tree_view.column('sex', width=80, anchor='center')
        self.tree_view.column('age', width=80, anchor='center')
        self.tree_view.column('id', width=80, anchor='center')
        self.tree_view.heading('name',text='姓名')
        self.tree_view.heading('sex', text='性别')
        self.tree_view.heading('age', text='年龄')
        self.tree_view.heading('id', text='学号')
        self.tree_view.pack(fill=tk.BOTH,expand=True)
        self.show_date_frame()

        tk.Button(self,text='刷新数据',command=self.show_date_frame).pack(anchor=tk.E,pady=5)
    def show_date_frame(self):
        #删除旧的阶段
        for _ in map(self.tree_view.delete,self.tree_view.get_children('')):
            pass
        students=db.all()
        index=0
        for stu in students:
            print(stu)
            self.tree_view.insert('',index+1,values=(stu['name'],stu["sex"],stu['age'],stu['id']))
class deletframe(tk.Frame):#删除数据页面
    def __init__(self,root):
        super().__init__(root)
        self.username=tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self, text='根据名称删除数据').pack()
        tk.Entry(self, textvariable=self.username).pack()
        tk.Button(self, text='删除',command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()
    def delete(self):#删除数据函数
        username=self.username.get()
        flag,message= db.delete_by_username(username)
        self.status.set(message)
        pass