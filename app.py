from flask import Flask
app = Flask(__name__) #代表目前執行的模組

@app.route("/") #函式的裝飾:以函示為基礎,提供附加功能
def home():
    return "Hello Flask2"

@app.route("/test") #代表處理的網站路徑/test
def test(): #定義如何處理
    return "testing"

if __name__=="__main__": #如果以主程式執行
    app.run() #啟動伺服器

#Procfile 裡面的web gunicorn app(檔名):app(第2行的變數)