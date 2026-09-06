def calculate_risk_score(df):

    # Exposure based on population.
    # Normalize population to a 0-100 scale.
    population_min = df["population"].min()
    population_max = df["population"].max()

    if population_max == population_min:
        df["exposure_score"] = 50
    else:
        df["exposure_score"] = (
            100
            * (df["population"] - population_min)
            / (population_max - population_min)
        )

    # Final multi-dimensional risk
    hazard_weight = 0.50
    vulnerability_weight = 0.30
    exposure_weight = 0.20

    df["risk_score"] = (
        df["hazard_score"] * hazard_weight
        + df["vulnerability_score"] * vulnerability_weight
        + df["exposure_score"] * exposure_weight
    )

    # Risk classification
    def classify_risk(score):

        if score >= 75:
            return "CRITICAL"
        elif score >= 50:
            return "HIGH"
        elif score >= 25:
            return "MODERATE"
        else:
            return "LOW"

    df["risk_category"] = df["risk_score"].apply(classify_risk)

    return df