from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    num_receive = request.form['num_give']
    adders_receive = request.form['adders_give']
    phone_receive = request.form['phone_give']

    doc = {'name': name_receive,
           'num': num_receive,
           'adders': adders_receive,
           'phone': phone_receive}

    db.dbtest.insert_one(doc)

    return jsonify({'msg': '저장 완료..'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    users = list(db.dbtest.find({},{'_id':False}))
    return jsonify({'all_user': users})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)