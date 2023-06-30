
import json

class MysqlDatebases:#数据
    def __init__(self):
        with open('user.json',mode='r',encoding='utf-8') as f:
            text=f.read()
        self.users=json.loads(text)
        self.students=json.loads(open('stus.json',mode='r',encoding='utf-8').read())

    def check_login(self,username,password):

        for user in self.users:
            if username==user['username']:
                if password ==user['password']:
                    return True,'登录成功'
                else:
                    return False,"密码错误"
        return False,"登录失败，用户不存在"
       # return self.users
    def all(self):
        return self.students

    def insert(self,student):
        self.students.append(student)
    def delete_by_username(self,name):
        for student in self.students:
            print(student)
            if student['name']==name:
                self.students.remove(student)
                return True,f'{name}删除用户成功'
        return False,f'{name}用户不存在'

    def seacher_by_username(self, name):
        for student in self.students:
            print(student)
            if student['name'] == name:

                print(student)
                return True, student

        return False, f'{name}用户不存在'
    def update(self,stu):
        for student in self.students:
            print(student)
            if student['name'] == stu['name']:
                student.update(stu)
                print(stu['name'])
                return True,f'{stu["name"]}用户数据修改成功'

        return False, f'{stu["name"]}用户不存在'
db=MysqlDatebases()
if __name__ == '__main__':
    print(db.check_login('admin','123456'))
    print(db.all())
    print(db.seacher_by_username('1'))