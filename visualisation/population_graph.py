import pandas as pd
import matplotlib.pyplot as plt


# Load settlement data
settlements = pd.read_csv("data/settlements.csv")


# Create graph
plt.figure(figsize=(12, 6))

plt.bar(
    settlements["settlement_name"],
    settlements["population"]
)

plt.xlabel("Settlement")
plt.ylabel("Population")

plt.title(
    "Population Distribution Across Selected Wayanad Settlements"
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()