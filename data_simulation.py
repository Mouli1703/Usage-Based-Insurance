import random
import pandas as pd

def generate_data(num_drivers=10):
    data = {
        "Driver ID": [f"D{i+1}" for i in range(num_drivers)],
        "Distance (km)": [random.randint(50, 500) for _ in range(num_drivers)],
        "Hard Brakes": [random.randint(0, 10) for _ in range(num_drivers)],
        "Average Speed (km/h)": [random.randint(40, 120) for _ in range(num_drivers)],
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    data = generate_data()
    data.to_csv("simulated_data.csv", index=False)
    print("Simulated data saved to 'simulated_data.csv'")
