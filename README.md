Description of medical_data_visualizer.py
This Python script is designed for visualizing and analyzing medical examination data. The dataset contains information about patients, including body measurements, blood test results, and lifestyle choices. The script performs several key tasks to clean the data, calculate additional features, and generate visualizations to explore relationships within the data.

1. Import Libraries
The script begins by importing the necessary libraries:

pandas for data manipulation and analysis.
seaborn and matplotlib.pyplot for data visualization.
numpy for numerical operations.
2. Load the Dataset
The dataset is loaded from a CSV file into a DataFrame df using pandas.read_csv(). The script handles any issues with improperly formatted lines by skipping them (on_bad_lines='skip').

3. Inspect Column Names and Data
Before proceeding, the script prints out the column names and the first few rows of the DataFrame to check the structure and ensure the necessary columns are present. This step helps diagnose any issues with column names or data formatting.

4. Add Overweight Column
If the columns 'weight' and 'height' are present, the script calculates the Body Mass Index (BMI) using the formula: 
BMI
=
weight
(
height
/
100
)
2
BMI= 
(height/100) 
2
 
weight
​
  It then creates an overweight column where a value of 1 indicates overweight (BMI > 25) and 0 otherwise.

5. Normalize Data
The script normalizes the cholesterol and gluc columns:

Cholesterol: Set to 0 if normal (value 1), otherwise 1.
Glucose: Set to 0 if normal (value 1), otherwise 1.
6. Draw Categorical Plot
The draw_cat_plot() function:

Transforms the DataFrame into a long format suitable for categorical plotting using pd.melt().
Groups and counts the occurrences of each categorical feature (cholesterol, glucose, smoke, alcohol intake, physical activity, overweight) by the cardio status.
Creates a bar plot using seaborn.catplot() to show the counts of each feature, split by the presence or absence of cardiovascular disease.
7. Clean Data
The clean_data(df) function:

Filters out incorrect data where diastolic pressure is higher than systolic pressure.
Removes patients with height or weight outside the 2.5th to 97.5th percentile range to exclude extreme values.
8. Draw Heat Map
The draw_heat_map() function:

Cleans the data using the clean_data() function.
Calculates the correlation matrix of the cleaned DataFrame.
Generates a mask for the upper triangle of the correlation matrix to make the heatmap more readable.
Plots the correlation matrix using seaborn.heatmap() with annotations and a color map to visualize the strength of relationships between features.
9. Function Calls
The script includes placeholders for calling the plotting functions (draw_cat_plot() and draw_heat_map()) to generate the visualizations. These calls are commented out but can be uncommented to execute the functions and produce the plots.
