from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    message=request.form['message']
    data=[message]
    vect = cv.transform(["this is spam"]).toarray()
    my_prediction = spam_detect_model.predict(vect)[0]
    #{"ham":1,"spam":0}
    print(my_prediction)
    if int(my_prediction)==1:
        my_prediction="it's a ham"
    else:
        my_prediction="it's a spam"
        
    return render_template("index.html",output=my_prediction)
if __name__=="__main__":
    app.run()