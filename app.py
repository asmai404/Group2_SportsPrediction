from flask import Flask, render_template, request

app = Flask(__name__)

# Load your trained model from the pickle file
import pickle

# with open('football_prediction_model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        # Get user input from the form
        input_data = request.form['input_data']

        # Preprocess the input data as needed for your model

        # Then, make predictions using your model
        # result = model.predict(input_data)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
