from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbsparta2

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/api', methods=['GET'])
def listing():
    all_list = list(db.homework.find({}, {'_id':False}))
    return jsonify({'all_list': all_list})

## API 역할을 하는 부분
@app.route('/api', methods=['POST'])
def saving():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    doc = {
        'name':name_receive,
        'count':count_receive,
        'address':address_receive,
        'phone':phone_receive
    }
    db.homework.insert_one(doc)

    return jsonify({'msg':"저장완료"})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)