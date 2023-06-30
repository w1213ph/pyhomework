import tkinter as tk
from views import aboutframe
from views import changeframe
from views import insertframe
from views import searchframe
from views import deletframe

class mainpage:
    def __init__(self,master:tk.Tk):
        self.root=master
        self.root.title("小辉的学生管理系统")
        self.root.geometry('600x400')
        self.creat_page()


    def creat_page(self):
        self.insert_frame = insertframe(self.root)
        self.search_frame = searchframe(self.root)
        self.delete_frame = deletframe(self.root)
        self.change_frame = changeframe(self.root)
        self.about_frame=aboutframe(self.root)





        menubar=tk.Menu(self.root)
        menubar.add_command(label="录入",command=self.show_insert)
        menubar.add_command(label="查询",command=self.show_seacher)
        menubar.add_command(label="删除",command=self.show_delete)
        menubar.add_command(label="修改",command=self.show_change)
        menubar.add_command(label="关于",command=self.show_about)
        self.root['menu']=menubar

    def show_insert(self):#插入

        self.insert_frame.pack()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.change_frame.pack_forget()
        self.about_frame.pack_forget()

    def show_seacher(self):#展示
        self.insert_frame.pack_forget()
        self.search_frame.pack()
        self.delete_frame.pack_forget()
        self.change_frame.pack_forget()
        self.about_frame.pack_forget()

    def show_delete(self):#删除
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack()
        self.change_frame.pack_forget()
        self.about_frame.pack_forget()

    def show_change(self):#修改
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.change_frame.pack()
        self.about_frame.pack_forget()
    def show_about(self):#关于
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.change_frame.pack_forget()
        self.about_frame.pack()


if __name__ == '__main__':
    root=tk.Tk()

    mainpage(root)
    root.mainloop()