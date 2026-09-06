def calculate_site_suitability(df):

    df["flood_safety"] = 100 - df["flood_risk_normalized"]
    df["landslide_safety"] = 100 - df["landslide_risk_normalized"]

    # Reverse slope: lower slope = generally more suitable.
    df["slope_suitability"] = 100 - df["slope_normalized"]

    # Reverse road distance: closer = more suitable.
    df["road_access"] = 100 - df["distance_to_road_normalized"]

    # Weighted suitability score
    df["suitability_score"] = (
        df["flood_safety"] * 0.20
        + df["landslide_safety"] * 0.20
        + df["slope_suitability"] * 0.15
        + df["water_availability_normalized"] * 0.15
        + df["road_access"] * 0.10
        + df["healthcare_access_normalized"] * 0.08
        + df["education_access_normalized"] * 0.06
        + df["electricity_access_normalized"] * 0.06
    )

    return df