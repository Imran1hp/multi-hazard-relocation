def filter_relocation_candidates(df):

    # Settlements requiring relocation consideration
    relocation_candidates = df[
        df["risk_category"].isin(["HIGH", "CRITICAL"])
    ].copy()

    return relocation_candidates
