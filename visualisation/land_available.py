import pandas as pd
import matplotlib.pyplot as plt


sites = pd.read_csv(
    "data/site.csv"
)


plt.figure(figsize=(10, 7))


plt.barh(
    sites["site_name"],
    sites["available_land_area"]
)


plt.title(
    "Available Land Area Across Candidate Relocation Sites"
)

plt.xlabel("Available Land Area")
plt.ylabel("Candidate Site")


plt.tight_layout()
plt.show()