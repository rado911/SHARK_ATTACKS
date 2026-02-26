import pandas as pd
from pathlib import Path


def read_dataframe(file_path: str) -> pd.DataFrame:
    file_type = Path(file_path).suffix.lower()
    if file_type == ".csv":
        return pd.read_csv(file_path)
    elif file_type in [".xls", ".xlsx"]:
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type")


def format_columns(df: pd.DataFrame, rename_dict: dict = None) -> pd.DataFrame:
    df = df.copy()df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_"))
    if rename_dict:
        df = df.rename(columns=rename_dict)
    return df


def clean_invalid_values(df: pd.DataFrame, column: str, replace_dict: dict) -> pd.DataFrame:
    df = df.copy()
    df[column] = df[column].replace(replace_dict)
    return df


def numeric_fill_nan(df: pd.DataFrame, column: str, method: str = "median") -> pd.DataFrame:
    df = df.copy()

    # Convert percent strings to numeric
    df[column] = (df[column].astype(str).str.replace("%", "", regex=False))

    df[column] = pd.to_numeric(df[column], errors="coerce")

    if method == "median":
        value = df[column].median()
    elif method == "mean":
        value = df[column].mean()
    else:
        raise ValueError("Method must be 'median' or 'mean'")

    df[column] = df[column].fillna(value)

    return df

def categorical_fill_na(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df = df.copy()
    mode_value = df[column].mode()[0]
    df[column] = df[column].fillna(mode_value)
    return df


def handle_duplicates_and_index(df: pd.DataFrame, id_column: str, output_file: str = None) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna(subset=[id_column])
    df = df.set_index(id_column)
    if output_file:
        df.to_csv(output_file)
    return df
