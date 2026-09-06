import pandas as pd


def normalize_0_100(series):
    """
    Normalize a numeric series to a 0-100 scale.
    """
    min_value = series.min()
    max_value = series.max()

    # Prevent division by zero
    if max_value == min_value:
        return pd.Series([50] * len(series), index=series.index)

    return 100 * (series - min_value) / (max_value - min_value)


def preprocess_settlements(df):

    print("Checking settlement data...")

    # Check missing values
    if df.isnull().values.any():
        print("Warning: Missing values found.")
        df = df.fillna(df.median(numeric_only=True))
    else:
        print("No missing values found.")

    # The source data stores some risk indicators under more descriptive names.
    # Create the engine-facing fields here so the scoring engines have a stable
    # input schema.
    df = df.copy()
    df["flood_risk"] = df["flood_frequency"] * df["flood_depth"]
    df["landslide_risk"] = df["landslide_susceptibility"]
    # A cyclone measurement is not present in the settlement dataset. Rainfall
    # is used as the available weather-hazard proxy for this prototype.
    df["cyclone_risk"] = df["rainfall"]
    df["poverty"] = df["poverty_index"]
    df["historical_disasters"] = df["historical_disaster_count"]

    # Columns that need normalization
    columns_to_normalize = [
        "flood_risk",
        "landslide_risk",
        "cyclone_risk",
        "rainfall",
        "elevation",
        "slope",
        "population_density",
        "poverty",
        "infrastructure_access",
        "historical_disasters"
    ]

    for column in columns_to_normalize:
        df[f"{column}_normalized"] = normalize_0_100(df[column])

    return df


def preprocess_sites(df):

    print("Checking candidate site data...")

    if df.isnull().values.any():
        print("Warning: Missing values found.")
        df = df.fillna(df.median(numeric_only=True))
    else:
        print("No missing values found.")

    df = df.copy()
    # ``available_land_area`` is the name used in the supplied site data;
    # carrying-capacity calculations use the shorter engine-facing name.
    df["available_land"] = df["available_land_area"]

    columns_to_normalize = [
        "flood_risk",
        "landslide_risk",
        "slope",
        "elevation",
        "available_land",
        "water_availability",
        "healthcare_access",
        "education_access",
        "electricity_access",
        "distance_to_road"
    ]

    for column in columns_to_normalize:
        df[f"{column}_normalized"] = normalize_0_100(df[column])

    return df
