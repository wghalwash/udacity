import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn as sns
sns.set_style('darkgrid')

def load_data():
    df = pd.read_csv('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    return df

def plot_hist(arg1, arg2, label1, label2):
    plt.hist(arg1, color='b', alpha=0.5, label=label1)
    plt.hist(arg2, color='r', alpha=0.5, label=label2)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    df = load_data()
    egypt = df.query('country == "egypt"')
    ethiopia = df.query('country == "Ethiopia"')
    plot_hist(egypt, ethiopia, 'Egypt', 'Ethiopia')