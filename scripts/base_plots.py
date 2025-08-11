import matplotlib.pyplot as plt
import seaborn as sns

def get_countplot(df, col_name):
    sns.countplot(x=col_name, data=df)
    plt.show()


def get_countplot_with_hue(df, col_name, hue, figsize=(20, 8)):
    plt.figure(figsize=figsize)
    plt.title(f'{col_name} and {hue}', fontsize=16)
    sns.countplot(x=col_name, hue=hue, data=df)
    plt.show()


def get_barplot(df, x, y, figsize=(7, 7)):
    plt.figure(figsize=figsize)
    plt.title(f'Mean {y} for {x}', fontsize=16)
    sns.barplot(x=x, y=y, data=df)
    plt.show()