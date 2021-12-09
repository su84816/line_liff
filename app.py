from flask import Flask , render_template
from flask import request, redirect, url_for

app = Flask(__name__) #代表目前執行的模組

@app.route("/") #函式的裝飾:以函示為基礎,提供附加功能
def home():
    return "home page"

@app.route('/input')#處理的網站路徑
#定義如何處理
def input():
    return render_template('user_input.html')

@app.route('/info')
def info():
    return render_template('user_info.html')

    
@app.route('/page/app')
def pageAppInfo():
    appInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo)

# 這邊是寫靜態網頁的資料交換,Liff是否取代了?
@app.route('/form')
def formPage():
    return render_template('Form.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        print("post : user => ", user)
        return redirect(url_for('success', name=user, action="post"))
    else:
        user = request.args.get('user')
        print("get : user => ", user)
        return redirect(url_for('success', name=user, action="get"))
@app.route('/success/<action>/<name>')
def success(name, action):
    return '{} : Welcome {} ~ !!!'.format(action, name)

if __name__=="__main__": #如果以主程式執行
    app.run() #啟動伺服器

#Procfile 裡面的web gunicorn app(檔名):app(第2行的變數)
#如果修改程式(本機端開發完)>要重新部署(不用初始化)>git add .>git commit -m "note">git push heroku master
#heroku網址:https://bestplace1130liff.herokuapp.com/ 
#看log:heroku logs --tail