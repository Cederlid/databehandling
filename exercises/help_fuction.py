import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_missing_values(df: pd.DataFrame)->None:
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    sns.barplot(x= missing_values.values, y= missing_values.index, palette=["blue", "orange"], hue= missing_values.values)
    plt.title("Null values vs columns")
    plt.ylabel("Columns")
    plt.xlabel("Number nulls")
    plt.show()