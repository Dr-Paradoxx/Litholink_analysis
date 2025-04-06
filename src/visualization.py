import matplotlib.pyplot as plt
import pandas as pd

def plot_variable_distribution(df: pd.DataFrame, variable: str):
    """
    Generates a boxplot of a variable across Stone Categories.
    """
    categories = df['Stone_Category'].unique()
    data = [df[df['Stone_Category'] == cat][variable] for cat in categories]
    plt.figure(figsize=(8, 6))
    plt.boxplot(data, labels=categories)
    plt.title(f'Distribution of {variable} by Stone Category')
    plt.xlabel('Stone Category')
    plt.ylabel(variable)
    plt.tight_layout()
    plt.savefig(f'plots/{variable}_by_Stone_Category.png')
    plt.close()

def plot_variability(df: pd.DataFrame, variable: str):
    """
    Generates a plot for variability in Same Day Sample Pairs.
    """
    categories = df['Stone_Category'].unique()
    means = df.groupby('Stone_Category')[variable].mean()
    plt.figure(figsize=(8,6))
    plt.bar(categories, means)
    plt.title(f'Mean {variable} in Same Day Sample Pairs by Stone Category')
    plt.xlabel('Stone Category')
    plt.ylabel(f'Mean {variable}')
    plt.tight_layout()
    plt.savefig(f'plots/variability_{variable}.png')
    plt.close()
