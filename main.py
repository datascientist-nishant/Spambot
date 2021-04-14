from flask import Flask, render_template, url_for, request
import pickle
import joblib
import gzip
import random

spam_classifier98_47 = open('spam_classifier98_47 .pkl','rb')
clf= joblib.load(spam_classifier98_47)

transform= open('transform .pkl','rb')
cv= joblib.load(transform)


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
@app.route('/spambot')
def start():
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        message= request.form['message']
        data= [message]
        vect= cv.transform(data).toarray()
        my_prediction= clf.predict(vect)
        random_spam = random.choice(list_spam)

        random_ham = random.choice(list_ham)

    return render_template('result.html',prediction= my_prediction, random_ham=random_ham,random_spam=random_spam)


@app.route('/spamshot1')
def end():
    return render_template('predict.html')

list_spam = ["Beware, It's a Spam.", "You've probably gotten Spam message.", "It's a Spam.", "Stop Right There..!, It's a Spam."]
list_ham = ["Chill Out, It's not Spam..!!", "Not a Spam, Go For it..!", "Not a Spam, It's Safe..!!"  ]


if __name__ == '__main__':
    app.run(debug=True)