import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

def change_to_int(features):
    int_features = [1 for i in range(7)]
    if int(features[0]) == 12 or int(features[0]) == 1 or int(features[0]) == 2:
        int_features[0] = 1
    elif int(features[0]) == 3 or int(features[0]) == 4 or int(features[0]) == 5:
        int_features[0] = 2
    elif int(features[0]) == 6 or int(features[0]) == 7 or int(features[0]) == 8:
        int_features[0] = 3
    elif int(features[0]) == 9 or int(features[0]) == 10 or int(features[0]) == 11:
        int_features[0] = 4
    int_features[1] = int(features[0])
    int_features[2] = int(features[1])
    int_features[3] = int(features[2])
    if int_features[2] == 1 or int_features[3] == 0 or int_features[3] == [6]:
        int_features[4] = 0
    else:
        int_features[4] = 1
    int_features[5] = int(features[3])
    int_features[6] = int(features[4]) / 41
    return int_features


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [x for x in request.form.values()]
    int_features = change_to_int(features)
    arr_features = [np.array(int_features)]
    prediction = model.predict(arr_features)
    # return render_template('index.html', prediction_text=int_features)
    return render_template('index.html', prediction_text='Number of rented bicycles should be {}'.format(round(prediction[0])))

if __name__ == "__main__":
    app.run(port=5000, debug=False)