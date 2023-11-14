from  flask import  Flask,render_template,request
import pickle
import Templates

app = Flask(__name__)


@app.route('/home',methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/api',methods= ["GET"])
def api():
     
     with open("iris_data_new.pkl","rb")as model:
        data = pickle.load(model)

        "sepal_length" ==eval(1)
        "sepal_width" == eval(4)
        "petal_length" == eval(2)
        "petal_width" == eval(3)

     result = data.predict([['sepal_width', 'petal_length', 'petal_width', 'target']])
     return  result
   


app.run()
A