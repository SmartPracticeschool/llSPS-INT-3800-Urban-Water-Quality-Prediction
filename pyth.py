import numpy as np
from flask import Flask, request, render_template
import pickle
model = pickle.load(open('randf2.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    float_features = []
    float_features.append(float(request.form['do']))
    float_features.append(float(request.form['ph']))
    float_features.append(float(request.form['co']))
    float_features.append(float(request.form['bod']))
    float_features.append(float(request.form['na']))
    float_features.append(float(request.form['tc']))
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    output = np.round_(prediction[[0]], 2)

    return render_template('index.html', wqi=output[0])

if __name__ == "__main__":
    app.run(debug=False)