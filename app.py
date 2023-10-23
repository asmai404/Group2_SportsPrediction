import numpy as np
from flask import Flask, render_template, request
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, KFold
import pickle

app = Flask(__name__)

# Loading trained model from a pickle file
with open('football_prediction_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        movement_reactions = float(request.form['movement_reactions'])
        passing = float(request.form['passing'])
        mentality_composure = float(request.form['mentality_composure'])
        dribbling = float(request.form['dribbling'])
        potential = float(request.form['potential'])
        wage_eur = float(request.form['wage_eur'])
        release_clause_eur = float(request.form['release_clause_eur'])
        value_eur = float(request.form['value_eur'])
        power_shot_power = float(request.form['power_shot_power'])
        physic = float(request.form['physic'])
        mentality_vision = float(request.form['mentality_vision'])
        attacking_short_passing = float(request.form['attacking_short_passing'])

        # Create a feature vector with the input data
        input_data = {
            "movement_reactions":[movement_reactions],
            "passing": [passing],
            "mentality_composure": [mentality_composure],
            "dribbling": [dribbling],
            "potential": [potential],
            "release_clause_eur": [release_clause_eur],
            "wage_eur": [wage_eur],
            "value_eur": [value_eur],
            "power_shot_power": [power_shot_power],
            "physic":[physic],
            "mentality_vision": [mentality_vision],
            "attacking_short_passing": [attacking_short_passing],

        }

        # print(list(input_data.values()))
        # sc = StandardScaler()
        # scaled = sc.fit_transform(list(input_data.values()))
        # print(scaled)


        input_data_scaled = pd.DataFrame(input_data, columns=input_data.keys())

        

        # Make predictions using your model

        # result = sum(input_data) / len(input_data) + 15 * 0.7
        result = model.predict(input_data_scaled)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
