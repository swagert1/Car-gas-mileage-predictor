# Project_4_MPG_Prediction

## Project Description:
This project is to model and predict MPG (miles per gallon) using know vehicle specifications from a current EPA data set that ranged from 1984 to 2023 model years of US vehicles. After significant filtering and cleaning the data was visualized through Tableau and placed into a polynomial regression model. Then this model is used to predict expected MPG from vehicle specifications input through an interactive website.

## Tools and Methods Used:

- JavaScript

- Python:
	modules: Flask, Pandas, SciKitLearn

- Git collaboration

- Tableau

## ETL

- Downloaded CSV file from EPA website https://www.fueleconomy.gov/feg/epadata/vehicles.csv
  This website is the official government source for fuel economy information

- Original CSV contained data for nearly every vehicle sold in the US from 1984 to 2023. 
  84 columns x 46,000+ rows

- After inspection of data and testing through modeling it was eventually filtered down to seven
  columns of data:
	- Year, Cylinders, Displacement, Vehicle Class, Trransmission, Drive, and MPG
	- through years 2000 to 2023

### Process:
- After initial inspection all vehicles not powered by gasoline were removed and rows reduced
  to the seven for modeling and visualization purposes

- using feedback from initial visualization and modeling:
	- hybrid vehicles were removed:
		- it was decided combination electric/gas drivetrain did not fit with our
		  modeling
	- two-cylinder vehicles were removed:
		- These were primarily rotary engine vehicles and not actually 'cylinders'
	- special puropse vehicle classes were removed
		- encompassed all vehicle classes so did not work for modeling purooses
	- years covered were reduced to 2000 to 2023
		- the earlier years had many more outliers; possibly due to electronic
		  fuel and engine processing that became nearly standard in the late 1990s
		  so it was decided to elimnate pre-2000 vehicles from the model


## Visualization

Web Link to Tableau Presentation: https://public.tableau.com/app/profile/albert.dudek/viz/Project_4_MPG_Prediction/MPGbyYear?publish=yes

Some take-aways from the visualizations:
- 50% of vehicles fall between 17 and 23 MPG.
- Smaller vehicle types have a broader range of MPG compared to larger vehicle types, making them less predictable.
- Front-Wheel Drives have a greater MPG compared to Rear and Four-Wheel Drive.
- Generally, fewer cylinders the greater the MPG. Similar to L(displacement), less displacement has greater MPG.
- Year and MPG does not have a significant trend apart from a broader range in MPG from 2013-2023. 

## Predictive Model:

The code for constructing and testing our predcitive model can be found in the file "Reg_model_poly.ipynb". The model is a polynomial regression using the sklearn function PolynomialFeatures, which transforms the input variables into a polynomial function of highest order n (we used n=3) including interaction terms. 

The following steps were taken to format our data and constuct and test our model:

1. After inspecting the data, we made the following changes
   
    a. Remove vehicles made before the year 2000 as these datapoints include outliers in the mpg dimension due to unknown factors we could not identify in our dataset
   
    b. Transform the cylinder displacement using the natural logarithm to make the realtionship between it and the vehicle mpg approximately linear
   
3. One-hot encode the categorical variables vehicle class, drive, and transmission, and set the drop first option to "true" to eliminate colinear categorical input variables
4. Create the features (X) and response (y) data, then use train_test_split and StandardScaler to create scaled training and testing datasets (scaling omits the categorical features)
5. Create a regression pipeline with the PolynomialFeatures and LinearRegression functions, then train the model with the training data
6. Create predictions with the testing data and calculate model performance metrics
7. Manually calculate the residuals and look for predictions that underestimate the gas mileage by more than 10 mpg
8. Perform residual analysis to check for heteroscedasticity and normality, and plot the predictions versus the actual y_test values to visualize the model performance
9. Export/import the model and scaler using the Pickle library
10. Randomly sample the original dataframe and generate a new prediction with the imported .pkl files, then, check for agreement bewteen the estimate and the actual gas milage
11. Generate and test the code need to deploy the model with our FLask API
     
    a. Generate "fake" input
    
    b. Encode categories from string inputs
    
    c. Format the vector
    
    d. Generate new prediction

NOTE: We have encountered instances where the jupyter notebook performs the regression on the testing dataset incorrectly if the kernel option "Restart & Run All" is used. This does not appear to be consistent behavior, and if the notebook is run line-by-line, the error does not appear to occur. 

Model Performance:

We achieved an R^2 socre of 0.88 when both training and generating predcitions with our model. Other performance metrics and residual analysis can be seen in the .pptx file in the main repo directory. 

Model Deployment with Flask API:

The model was implemented using a Flask API, which routes to an HTML document that is used to collect input data from the user and display the corresponding mpg prediction. Item 10 above outlines the steps to implement the model, which only needed slight modifications in the Flask API. The follwing steps can be taken to run the model o a local device:

1. Clone the git repository
2. Open the "app.py" program in a command prompt after navigating to the main directory
    a. The main diectory should have the "app.py" file, a "static" directory which contains the .css file to set the style for the HTML file, and a "template" directory which contains the file "index.html" which is referenced in "app.py"
    b. The files "model.pkl" and "scaler.pkl" should also be int he main directory. These files apply the StandardScaler and regression pipelines to the input data, respectively.
3. Navigate to the http://127.0.0.1:5000/ url in a web browser to display the dashboard
4. Enter the vehicle specifications and click the "Predict car's MPG" button. The estimated gas mileage will appear below the button.


## Collaborators:

Kevin M.

Albert D.

Ryan F.

Greg

## Data Source
	https://www.fueleconomy.gov/feg/ws/#ympgVehicle

## Resources

1.) https://bootcampspot.instructure.com/courses/3281/modules

2.) .html and .css templates can be found at https://fonts.googleapis.com/

3.) https://www.templateswise.com/electric-car-powerpoint-template/ 

