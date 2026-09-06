import pandas as pd
import matplotlib.pyplot as plt


settlements = pd.read_csv("data/settlements.csv")


plt.figure(figsize=(10, 7))


plt.scatter(
    settlements["elevation"],
    settlements["slope"],
    s=settlements["population"] / 50
)


# Settlement labels
for _, settlement in settlements.iterrows():

    plt.annotate(
        settlement["settlement_name"],
        (
            settlement["elevation"],
            settlement["slope"]
        ),
        fontsize=8
    )


plt.title(
    "Terrain Relationship: Elevation vs Slope"
)

plt.xlabel("Elevation")
plt.ylabel("Slope")


plt.tight_layout()
plt.show()