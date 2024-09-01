from flask import Flask,request,jsonify,render_template
import os 
from flask_cors import CORS,cross_origin
from src.cnnClassifier.utils.common import decodeimage
from src.cnnClassifier.pipeline.predict import PredictPipeline


os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app=Flask(__name__)
CORS(app)


class Clinetapp:
    def __init__(self):
        self.filename="Inputimage.jpg"
        self.classifier=PredictPipeline(self.filename)




@app.route("/",methods=['GET'])
@cross_origin()
def home():
    return render_template('index.htm')     



@app.route("/train",methods=['GET','POST'])
@cross_origin()
def trainRoute():
       os.system("pytho main.py")
       return "Traning done successfully"
   
   
@app.route("/predict",methods=['POST'])
@cross_origin()
def predictRoute():
    image=request.json['image']
    decodeimage(image,clApp.filename)
    result=clApp.classifier.predict()
    return jsonify(result)   
        
if __name__=="__main__":
    clApp=Clinetapp()
   # app.run(host='0.0.0.0',port=8080) # local
    app.run(host='0.0.0.0',port=80) #azure
            
        

