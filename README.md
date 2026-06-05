1. PROJECT OVERVIEW 
The project focuses on predicting heart disease using machine learning classification algorithms 
based on various mobile parameters.


2.DATASET
source : The dataset have taken from the kaggle.
Rows   : The data set contains around 2000 observations and 21 features.

    1. battery_power : Total energy a battery can store in one time measured in mAh
    2. blue :           Has bluetooth or not
    3. clock_speed :    speed at which microprocessor executes instructions
    4. dual_sim :       Has dual sim support or not
    5. fc :             Front Camera mega pixels
    6. four_g :         Has 4G or not
    7. int_memory :     Internal Memory in Gigabytes
    8. m_dep :          Mobile Depth in cm
    9. mobile_wt :      Weight of mobile phone
    10. n_cores :       Number of cores of processor
    11. pc :            Primary Camera mega pixels
    12. px_height :     Pixel Resolution Height
    13. px_width :      Pixel Resolution Width
    14. ram :           Random Access Memory in Mega Bytes
    15. sc_h :          Screen Height of mobile in cm
    16. sc_w :          Screen Width of mobile in cm
    17. talk_time :     longest time that a single battery charge will last when you are    
    18. three_g:        Has 3G or not
    19. touch_screen :  Has touch screen or not
    20. wifi :          Has wifi or not
    21. price_range :   This is the target variable with value of 0(low cost), 1(medium cost), 2(high cost) and 3(very high cost).

Project_Type : This is a classical basic ML project - using a Classification model to predict the mobile price in some ranges as high or mid or low.


3.WORKFLOW
 -Data loading
 -Data preprocessing
 -EDA
 -Standardization
 -Model Building
 -Model Evaluation
 -Model Saving
 -Model Deployment


4.TECHNOLOGIES USED
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Gradient Boosting
- Jupyter Notebook
 

5. MODEL USED 
  -Logistic Regression
  -Decision Tree
  -Random Forest
  -Gradient Boosting 


6. METRICS
 -Accuracy Score
 -Confusion Matrix
 -Classification Report
 -ROC Curve
 -AUC Score


7. BEST MODEL
After comparing Logistic Regression, Random Forest, and Gradient Boosting using Accuracy, Recall, and ROC-AUC metrics, 
Logistic Regression was selected as the final model due to its strong accuracy score and best ROC-AUC performance. 


8.MODEL COMPARISON

Model                 Accuracy        ROC-AUC 
Logistic Regression  	0.96	  	    0.99
Random Forest	        0.86	  	    0.97
Decision Tree	        0.82	  	    0.88
Gradient Boosting       0.90	  	    0.98



9. FUTURE SCOPE 
 - This just a basic Ml project .
 -To understand the concept of classification 


