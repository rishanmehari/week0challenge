import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
ethiopia = pd.read_csv("ethiopia.csv")
sudan = pd.read_csv("sudan.csv")
tanzania = pd.read_csv("tanzania.csv")

# Show basic info
print("Ethiopia Summary:\n", ethiopia.describe())
print("\nSudan Summary:\n", sudan.describe())
print("\nTanzania Summary:\n", tanzania.describe())

# Example: Plot temperature trends (adjust column names if needed)
try:
    plt.figure(figsize=(10,5))
    plt.plot(ethiopia['Year'], ethiopia['Temperature'], label='Ethiopia')
    plt.plot(sudan['Year'], sudan['Temperature'], label='Sudan')
    plt.plot(tanzania['Year'], tanzania['Temperature'], label='Tanzania')

    plt.title("Temperature Trends Comparison")
    plt.xlabel("Year")
    plt.ylabel("Temperature")
    plt.legend()
    plt.show()
except:
    print("Check column names for plotting")