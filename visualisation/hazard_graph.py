import pandas as pd
import matplotlib.pyplot as plt


settlements = pd.read_csv("data/settlements.csv")


hazard_columns = [
    "flood_frequency",
    "flood_depth",
    "rainfall",
    "landslide_susceptibility"
]


# Normalize each variable to 0–1
normalized_hazards = settlements[hazard_columns].copy()

for column in hazard_columns:

    min_value = normalized_hazards[column].min()
    max_value = normalized_hazards[column].max()

    normalized_hazards[column] = (
        normalized_hazards[column] - min_value
    ) / (
        max_value - min_value
    )


# Add settlement names
normalized_hazards["settlement_name"] = settlements["settlement_name"]


# Plot
normalized_hazards.set_index(
    "settlement_name"
)[hazard_columns].plot(
    kind="bar",
    figsize=(14, 7)
)


plt.title(
    "Normalized Hazard Factor Comparison Across Wayanad Settlements"
)

plt.xlabel("Settlement")
plt.ylabel("Normalized Hazard Value (0–1)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()