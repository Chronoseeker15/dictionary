from flask import Flask,request, render_template,jsonify,redirect,url_for
from pymongo import MongoClient
import requests

app = Flask(__name__)

cxn_string = f'mongodb+srv://adrian:adrian@cluster0.b5hahmz.mongodb.net/?retryWrites=true&w=majority'
client  = MongoClient(cxn_string)

db = client.dbsparta_plus_week2

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/detail/<keyword>')
def detail(keyword):
    return render_template('detail.html', word=keyword)

@app.route('/api/save_word', methods =['post'])
def save_word():
    return jsonify({
        'result': 'success',
        'msg':'the word was saved',

    })
app.route('/api/delete_word', methods = ['post'])
def delete_word():
    return jsonify({
        'result': 'success',
        'msg':'the word was deleted',
    })

if __name__ == '__main__':
    app.run('0.0.0.0', port =5000, debug=True)
