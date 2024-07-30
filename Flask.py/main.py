from flask import Flask, render_template, request

app = Flask(__name__)

# 기본 index 페이지 
@app.route('/')
def index():
    return render_template("index.html")

# post 페이지로 이동
@app.route('/postResult', methods=['POST','GET'])
def postResult():
    # msg_input(POST방식으로 데이터 전송)
    msg_input_post = request.form["msg_input_post"]
    return render_template("postResult.html", msg_input_post = msg_input_post)

# get 페이지로 이동
@app.route('/getResult', methods=['POST','GET'])
def getResult():
    # msg_input(Get방식으로 데이터 전송)
    msg_input_get = request.args.get("msg_input_get")
    return render_template("getResult.html", msg_input_get = msg_input_get)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)