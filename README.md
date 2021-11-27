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

# Webpage link: [link](https://energyeff.herokuapp.com/)

# Tech Stack
* Front-End: HTML, Bootstrap
* Back-End: Flask
* IDE: VScode, Jupyter Notebook
