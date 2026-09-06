import pandas as pd


def calculate_hazard_score(df):

    # Hazard weights
    flood_weight = 0.40
    landslide_weight = 0.35
    cyclone_weight = 0.25

    df["hazard_score"] = (
        df["flood_risk_normalized"] * flood_weight
        + df["landslide_risk_normalized"] * landslide_weight
        + df["cyclone_risk_normalized"] * cyclone_weight
    )

    return df