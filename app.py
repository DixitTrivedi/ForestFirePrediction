from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

loadModel = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    values = [np.array(int_features)]
    prediction = loadModel.predict_proba(values)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('index.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
    else:
        return render_template('index.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")

if __name__ == ('__main__'):
    app.run(host='0.0.0.0', port=8080)