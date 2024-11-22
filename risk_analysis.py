import pandas as pd

def calculate_risk_score(df):
    df["Risk Score"] = (df["Hard Brakes"] * 2) + (df["Average Speed (km/h)"] / 10) - (df["Distance (km)"] / 100)
    return df

if __name__ == "__main__":
    data = pd.read_csv("simulated_data.csv")
    data = calculate_risk_score(data)
    data.to_csv("risk_scores.csv", index=False)
    print("Risk scores saved to 'risk_scores.csv'")
