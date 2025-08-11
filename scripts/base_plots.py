import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import seaborn as sns
import math

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


x = list(range(10))
x = [-i for i in x[::-1]] + x

y_1 = [i for i in x]
y_2 = [i**2 for i in x]
y_3 = [i**3 for i in x]

def get_polynomial_subplots():
    fig, axes = plt.subplots(1, 3)
    fig.set_size_inches(12, 4)
    fig.suptitle('Polynomial', fontsize=12)

    axes[0].plot(x, y_1, label='linear')
    axes[0].legend()
    axes[0].set_xlabel('x-values')
    axes[0].set_ylabel('y-values')
    axes[0].grid()

    axes[1].plot(x, y_2, label='square')
    axes[1].legend()
    axes[1].set_xlabel('x-values')
    axes[1].set_ylabel('y-values')
    axes[1].grid()

    axes[2].plot(x, y_3, label='cubic')
    axes[2].legend()
    axes[2].set_xlabel('x-values')
    axes[2].set_ylabel('y-values')
    axes[2].grid()

    plt.show()


get_polynomial_subplots()

x = list(range(100))
y = [int(10 + 5 * math.sin(i) + 2 * math.sin(10 * i) +
         -2 * math.sin(40 * i) + 2 * math.sin(80 * i)) for i in x]
def set_plots_tickers():
    fig, ax = plt.subplots()
    fig.suptitle('Daily site visitors', fontsize=12)
    fig.set_size_inches(10, 4)

    ax.plot(x, y,
            color='green',
            marker='o',
            linestyle='dashed',
            linewidth=1,
            markersize=5,
            label='Visitors count')

    ax.xaxis.set_major_locator(MultipleLocator(14))
    ax.xaxis.set_major_formatter('{x:.0f}')

    ax.xaxis.set_minor_locator(MultipleLocator(7))
    ax.xaxis.set_minor_formatter('{x:.0f}')

    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_formatter('{x:.0f}')

    ax.yaxis.set_minor_locator(MultipleLocator(2))
    ax.yaxis.set_minor_formatter('{x:.0f}')

    ax.tick_params(which='major', length=10)
    ax.tick_params(which='minor', length=4,)

    ax.grid(which='major', color='gray', linewidth=1)
    ax.grid(which='minor', color='gray', linewidth=0.5)

    ax.set_xlabel('Day of the year')
    ax.set_ylabel('Count')
    ax.legend()

    plt.show()

set_plots_tickers()