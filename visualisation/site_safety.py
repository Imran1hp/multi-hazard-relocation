import pandas as pd
import matplotlib.pyplot as plt


sites = pd.read_csv("data/site.csv")


safety_columns = [
    "flood_risk",
    "landslide_risk",
    "soil_stability"
]


sites.set_index(
    "site_name"
)[safety_columns].plot(
    kind="bar",
    figsize=(14, 7)
)


plt.title(
    "Candidate Site Safety Factor Comparison"
)

plt.xlabel("Candidate Site")
plt.ylabel("Normalized Safety Value (0–1)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()