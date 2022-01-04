from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta2


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_stars():
    all_list = list(db.mystar.find({}, {'_id':False}).sort('like', -1))
    return jsonify({'all_list': all_list})


@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']
    like = db.mystar.find_one({"name":name_receive}, {"_id":False})['like']
    db.mystar.update_one({'name':name_receive}, {'$set':{'like':like + 1}})
    print(name_receive)
    return jsonify({'msg': '좋아요!'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give']
    db.mystar.delete_one({'name':name_receive})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)