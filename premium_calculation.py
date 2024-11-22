import pandas as pd

def calculate_premium(df):
    base_premium = 100
    df["Premium ($)"] = df["Risk Score"].apply(lambda x: base_premium + max(0, (x - 5) * 10))
    return df

if __name__ == "__main__":
    data = pd.read_csv("risk_scores.csv")
    data = calculate_premium(data)
    data.to_csv("insurance_premiums.csv", index=False)
    print("Insurance premiums saved to 'insurance_premiums.csv'")
