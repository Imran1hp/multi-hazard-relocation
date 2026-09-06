def calculate_carrying_capacity(df):

    # Prototype assumptions

    # 1 unit of available land supports 100 people
    df["land_capacity"] = df["available_land"] * 100

    # Water availability score represents a maximum
    # population support level for simulation purposes
    df["water_capacity"] = (
        df["water_availability"] * 50
    )

    # Infrastructure capacity based on the weakest
    # essential infrastructure component
    df["infrastructure_capacity"] = (
        df[
            [
                "healthcare_access",
                "education_access",
                "electricity_access"
            ]
        ]
        .mean(axis=1)
        * 60
    )

    # Final carrying capacity is constrained by
    # the weakest available resource
    df["carrying_capacity"] = df[
        [
            "land_capacity",
            "water_capacity",
            "infrastructure_capacity"
        ]
    ].min(axis=1)

    # Round capacity to whole people
    df["carrying_capacity"] = (
        df["carrying_capacity"]
        .round()
        .astype(int)
    )

    return df