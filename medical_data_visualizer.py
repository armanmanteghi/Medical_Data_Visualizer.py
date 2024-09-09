import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv(r'C:\Users\arman\OneDrive\Desktop\Coding\medical_examination.csv', on_bad_lines='skip')

# Print column names to diagnose issues
print("Column names:", df.columns)

# Print the first few rows to check data
print(df.head())

# Rename columns if necessary
# Example renaming based on column names observed
# df.rename(columns={'wt': 'weight', 'ht': 'height'}, inplace=True)

# Ensure 'weight' and 'height' columns exist
if 'weight' in df.columns and 'height' in df.columns:
    # Add the overweight column
    df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
    df['overweight'] = (df['BMI'] > 25).astype(int)
else:
    print("Required columns are missing from the DataFrame.")

# Normalize the data
if 'cholesterol' in df.columns and 'gluc' in df.columns:
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
else:
    print("Cholesterol or glucose columns are missing from the DataFrame.")

def draw_cat_plot():
    # Create DataFrame for categorical plot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count')
    
    # Draw the categorical plot
    fig = sns.catplot(data=df_cat, x='variable', hue='value', col='cardio', kind='bar', height=4, aspect=1.5).fig
    plt.show()
    return fig

def clean_data(df):
    # Filter out incorrect data
    df = df[df['ap_lo'] <= df['ap_hi']]
    df = df[(df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))]
    df = df[(df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    return df

def draw_heat_map():
    # Clean the data
    df_heat = clean_data(df)
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    plt.figure(figsize=(10, 8))
    
    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', center=0, vmin=-1, vmax=1)
    plt.show()

# Call functions to draw plots if necessary
# draw_cat_plot()
# draw_heat_map()
