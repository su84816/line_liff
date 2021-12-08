from flask import Flask , render_template
app = Flask(__name__) #代表目前執行的模組

@app.route("/") #函式的裝飾:以函示為基礎,提供附加功能
def home():
    return "Hello Flask2"

@app.route("/test") #代表處理的網站路徑/test
def test(): #定義如何處理
    return "testing"

@app.route('/input')
def input():
    return render_template('user_input.html')

@app.route('/page/text')
def pageText():
    return render_template('page.html', text="Python Flask !"
    
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

if __name__=="__main__": #如果以主程式執行
    app.run() #啟動伺服器

#Procfile 裡面的web gunicorn app(檔名):app(第2行的變數)
#如果修改程式(本機端開發完)>要重新部署(不用初始化)>git add .>git commit -m "">git push heroku master