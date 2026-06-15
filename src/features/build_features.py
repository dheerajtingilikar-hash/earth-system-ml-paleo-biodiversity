def create_ecosystem_features(df, taxon_col="accepted_name"):
    eco = df.groupby("early_interval").agg(
        richness=(taxon_col, "nunique"),
        occurrences=("occurrence_no", "count"),
        lat_mean=("lat", "mean"),
        lng_mean=("lng", "mean"),
    ).reset_index()
    return eco