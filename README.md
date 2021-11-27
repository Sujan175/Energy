# Energy Efficiency Prediction
In this project, we develop a maching  learning model to predict the Heating Load & Cooling Load(units-kWh/m<sup>2</sup>) of residential buildings based on 8 input parameters. Several regression models were tested and finally RandomForestRegressor was chosen. Further hyper-parameter tuning was performed to obtain best performance.

The imput parameters are-
1. Relative Compactness
2. Surface Area-m<sup>2</sup>
3. Wall Area-m<sup>2</sup>
4. Roof Area-m<sup>2</sup>
5. Height-m
6. Orientation - 2:North, 3:East, 4:South, 5:West
7. Glazing Area- 0%, 10%, 25%, 40%
8. Glazing Variations - 1:Uniform, 2:North, 3:East, 4:South, 5:West

## Webpage link: [link](https://energyeff.herokuapp.com/)

## Tech Stack
* Front-End: HTML, Bootstrap
* Back-End: Flask
* IDE: VScode, Jupyter Notebook

## How to run the app
1. First create a virtual environment by using this command: 
   - conda create -n myenv python=3.7
2. Activate the environment using the command: 
   - conda activate myenv
3. Install the necessary packages: 
   - pip install -r requirements.txt
4. Run the app: 
   - python app.py
 
## Workflow

### Data Collection: [link](https://archive.ics.uci.edu/ml/datasets/energy+efficiency)

### Data-Preprocessing:
* Check for missing values
* Since all the features are numerical values, No need to perform data-preprocessing

### Model Selection:
* Different regressor models were tried and out of these randomforestregressor was chosen.
* The conclusion was made using MSE, MAE, RMSE scores.
* Performed hyperparameter tuning to improve performance.

### Deployment:
The model is deployed using flask on heroku.
