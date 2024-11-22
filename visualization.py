import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_premiums(df):
    sns.barplot(x="Driver ID", y="Premium ($)", data=df)
    plt.title("Insurance Premiums by Driver")
    plt.xlabel("Driver ID")
    plt.ylabel("Premium ($)")
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv("insurance_premiums.csv")
    plot_premiums(data)
