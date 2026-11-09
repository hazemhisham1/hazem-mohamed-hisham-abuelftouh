import pandas as pd

def clean_dataset():
    input_file = "diabetes_prediction_dataset.csv"
    output_file = "cleaned data set _predictions.csv"

    print(f"Loading data from '{input_file}'...")
    df = pd.read_csv(input_file)


    print("\n--- Initial Dataset Summary ---")
    print(f"Shape: {df.shape}")


    print("\n--- Checking for Missing / Null Values ---")
    null_counts = df.isnull().sum()
    total_nulls = null_counts.sum()
    print(null_counts)
    print(f"Total Null Values: {total_nulls}")


    print("\n--- Checking for Duplicates ---")
    duplicates_count = df.duplicated().sum()
    print(f"Total Duplicate Rows Found: {duplicates_count}")


    if duplicates_count > 0:
        df_cleaned = df.drop_duplicates().copy()
        print(f"Removed {duplicates_count} duplicate rows.")
    else:
        df_cleaned = df.copy()


    if total_nulls > 0:
        df_cleaned = df_cleaned.dropna().copy()
        print(f"Dropped rows with null values.")


    print("\n--- Cleaned Dataset Summary ---")
    print(f"New Shape: {df_cleaned.shape}")
    print(f"Remaining Duplicates: {df_cleaned.duplicated().sum()}")
    print(f"Remaining Nulls: {df_cleaned.isnull().sum().sum()}")


    df_cleaned.to_csv(output_file, index=False)
    print(f"\nCleaned dataset successfully saved to '{output_file}'!")

if __name__ == "__main__":
    clean_dataset()
