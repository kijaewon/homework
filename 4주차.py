from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('onepage.html')


@app.route('/orders')
def get_orders():
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({
        'result': 'success',
        'msg': '주문을 성공적으로 받아옴',
        'orders': orders})


@app.route('/orders', methods=['POST'])
def make_orders():
    name = request.form['name']
    num = request.form['num']
    address = request.form['address']
    phonenum = request.form['phonenum']

    new_order = {
        'name': name,
        'num': num,
        'address': address,
        'phonenum': phonenum
    }

    db.orders.insert_one(new_order)

    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 작성되었어요'})


if __name__ == '__main__':
    app.run('localhost', 5001)
