import pandas as pd

def load_data():

    disease_df = pd.read_csv("data/disease_gene.csv")
    protein_df = pd.read_csv("data/protein_features.csv")

    # Rename gene column to match protein_id
    disease_df = disease_df.rename(columns={"gene":"protein_id"})

    # Merge datasets
    df = pd.merge(disease_df, protein_df, on="protein_id", how="inner")

    return df