from flask import Flask, render_template, request
# import pandas as pd
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import LabelEncoder
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.ensemble import RandomForestRegressor
# import xgboost as xgb
# from sklearn.model_selection import GridSearchCV, KFold
import pickle

app = Flask(__name__)

# Load your trained model from a pickle file
# with open('football_prediction_model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        movement_reactions = float(request.form['movement_reactions'])
        passing = float(request.form['passing'])
        mentality_composure = float(request.form['mentality_composure'])
        dribbling = float(request.form['dribbling'])
        potential = float(request.form['potential'])
        release_clause_eur = float(request.form['release_clause_eur'])

        # Create a feature vector with the input data
        input_data = [movement_reactions, passing, mentality_composure, dribbling, potential, release_clause_eur]

        # Make predictions using your model

        result = sum(input_data) / len(input_data) + 15 * 0.7
        # result = model.predict([input_data])
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
