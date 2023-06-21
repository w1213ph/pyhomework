def addemp(listemp:list):
    emp={'id':1,'name':'xxxx','sex':'xxx','address':'xxxsxs','sal':10000}
    #定义员工字典
    emp['id']=input('输入员工编号：')
    emp['name'] = input('输入员工姓名：')
    emp['sex'] = input('输入员工性别：')
    emp['address'] = input('输入员工地址：')
    emp['sal'] = input('输入员工薪资：')
    listemp.append(emp)
    print('添加完成!')
    pass
def showAll(listemp:list):
    if listemp==None or len(listemp)==0:
        print('没有任何员工信息存在！')
        return

    print('编号\t\t 姓名\t\t 性别\t\t 地址\t\t 薪资')
    print('-'*80)
    for emp in listemp:
        print('%s\t\t %s\t\t %s\t\t %s\t\t %s\t\t'
              %(emp['id'],emp['name'],emp['sex'],emp['address'],emp['sal'],))
    print('-' * 80)
    pass
def update(listemp:list):
    if listemp==None or len(listemp)==0:
        print('没有任何员工信息存在！')
        return
    sindex=-1;
    sid=input('请输入要修改的员工编号:')
    for i,stu in enumerate(listemp):
        if stu['id']==sid:
            sindex=i
            break
    if sindex!=-1:
        print('要修改的员工信息为：')
        emp=listemp[sindex]
        print('%s\t\t %s\t\t %s\t\t %s\t\t %s\t\t'
              % (emp['id'], emp['name'], emp['sex'], emp['address'], emp['sal'],))

        print('输入新的员工信息：')
        emp['address'] = input('输入地址：')
        emp['sal'] = input('输入薪资：')
        print('更新成功！')
    else:
        print('没有该编号的员工信息存在！')
    pass
def delById(listemp:list):
    if listemp==None or len(listemp)==0:
        print('没有任何员工信息存在！')
        return
    sindex=-1;
    id=input('请输入要删除的员工编号:')
    for i,stu in enumerate(listemp):
        if stu['id']==id:
            sindex=i
            break
    if sindex!=-1:
        print('要删除的员工信息为：')
        emp=listemp[sindex]
        print('%s\t\t %s\t\t %s\t\t %s\t\t %s\t\t'
              % (emp['id'], emp['name'], emp['sex'], emp['address'], emp['sal'],))
        listemp.remove(emp)
        print('删除成功！')
    else:
        print('没有该编号的员工信息存在！')
    pass
def findempBySname(listemp: list):
    if listemp==None or len(listemp)==0:
        print('没有任何员工信息存在！')
        return

    sindex=-1;
    searcherName=input('请输入要查找的员工姓名:')
    for i,emp in enumerate(listemp):
        if emp['name']==searcherName:
            sindex=i
            print('%s\t\t %s\t\t %s\t\t %s\t\t %s\t\t'
                  % (emp['id'], emp['name'], emp['sex'], emp['address'], emp['sal'],))
    if sindex==-1:
        print('没有找到该姓名的员工信息！')
    pass
def show():
    print("请选择你要进行的功能输入前面的数字进行功能选择：")
    print("1.输入员工信息")
    print("2.展示目前员工信息")
    print("3.修改员工信息")
    print("4.查找员工信息")
    print("5.删除员工信息")
    print("0.退出")
if __name__ == '__main__':
    listemp = []
    while True:
        show()
        a=input("\033[96m选择你要进行的功能：\033[0m")
        if a=='1':
            while True:
                addemp(listemp)  # 调用添加学生的函数
                choose = input('是否继续输入 按任意键继续，输入n键退出:')
                if choose != 'n':
                    continue
                else:
                    break
        elif a=='2':
            showAll(listemp)
        elif a=='3':
                update(listemp)  # 调用修改信息的函数
                showAll(listemp)
        elif a=='4':
                findempBySname(listemp)  # 调用查找的函数
        elif a=='5':
            delById(listemp)  # 调用删除的函数
            showAll(listemp)
        elif a=='0':
            print('感谢你的使用')
            break
        else:print('输入格式不对请重新输入')




