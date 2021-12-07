from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# 路由解析：通过用户访问路径，匹配相应函数
# 路由唯一路径
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!!'

@app.route('/index')
def hello():  # put application's code here
    return 'Hello'

@app.route('/index/<name>')
def welocome(name):  # put application's code here
    return 'Hello,%s'%name

@app.route('/index/<int:id>')
def welocome2(id):  # put application's code here
    return 'Hello,%d会员'%id

# 返回用户渲染后的网页文件
@app.route("/index2")
def index2():
    return render_template("index2.html")

# 向页面传递变量
@app.route("/index3")
def index3():
    time = datetime.date.today()  # 普通变量
    name = ["小组", "小王", "老王"]  # 列表类型
    task = {"任务": "打扫卫生","时间": "3小时"}  # 字典类型
    return render_template("index2.html", var=time, list=name, task=task)

# 表单提交
@app.route('/test/register')
def register():
    return render_template("register.html")
# 接受表单提交的路由，需要指定method为post
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


# 新手debug模式开启
if __name__ == '__main__':
    app.run(debug=True)
