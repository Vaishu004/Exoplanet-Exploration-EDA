Exoplanet Hunting in Deep Space: EDA

This project explores a dataset from Kaggle, containing information about exoplanets discovered in deep space. The goal of this Exploratory Data Analysis (EDA) is to better understand the dataset, identify trends and patterns, and prepare the data for further analysis and machine learning applications.

•	Loaded dataset:
Using  “pandas”.
df =pd.read_csv(“exoTest.csv”)
print(df.head())
Shows first few rows of dataset.
 
Values like LABEL, FLUX.1, FLUX.2, etc.

•	Checked basic info :
Using df.info() and df.describe()
Checked no. of rows and columns, type of data in every row and columns, missing values, etc
LABEL : category of data
FLUX : numeric data
 
•	Plot data distributions :
1)	Distribution of labels : 
Using seaborn and matplotlib. 
Distribution of labels (LABEL 1, LABEL 2)
 

2)	Flux Value Distributions :
Using seaborn and matplotlib.
 

•	Correlation analysis : 
Identify relationships between flux, find patterns in data.
Heatmap : visually represents how each column of flux values is related to each other.
Dark/bright regions : strong relation.
Light regions : weak relations
In this heatmap : Red : positive relations, Blue : negative relations
 



•	Visualize Flux time series for one row
To understand patterns and trends in flux values.
Shows intensity ( change in flux values ) over 3197 columns in dataset.
