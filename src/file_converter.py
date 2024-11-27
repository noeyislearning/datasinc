import os
import pandas as pd
from tqdm import tqdm


# :: Create the output directory if it doesn't exist
def create_output_directory(output_dir):
    os.makedirs(output_dir, exist_ok=True)


# :: Read the .txt file into a DataFrame
def read_txt_file(txt_file_path, delimiter="\t", low_memory=False):
    print("Reading the .txt file...")
    return pd.read_csv(txt_file_path, delimiter=delimiter, low_memory=low_memory)


# :: Save the DataFrame to a .csv file with a loading UI
def save_csv_file(df, csv_file_path, chunk_size=10000):

    print("Saving the DataFrame to a .csv file...")
    total_rows = len(df)

    with tqdm(total=total_rows, desc="Saving rows") as pbar:
        for i in range(0, total_rows, chunk_size):
            chunk = df.iloc[i : i + chunk_size]
            if i == 0:
                chunk.to_csv(csv_file_path, index=False, mode="w", header=True)
            else:
                chunk.to_csv(csv_file_path, index=False, mode="a", header=False)
            pbar.update(chunk_size)


# :: Convert a .txt file to a .csv file.
def convert_txt_to_csv(
    txt_file_path,
    output_dir,
    csv_filename="converted_file.csv",
    delimiter="\t",
    low_memory=False,
    chunk_size=10000,
):
    # :: Create the output directory
    create_output_directory(output_dir)

    # :: Specify the path where you want to save the .csv file
    csv_file_path = os.path.join(output_dir, csv_filename)

    # :: Read the .txt file into a DataFrame
    df = read_txt_file(txt_file_path, delimiter=delimiter, low_memory=low_memory)

    # :: Save the DataFrame to a .csv file
    save_csv_file(df, csv_file_path, chunk_size=chunk_size)

    print(f"File successfully converted and saved to {csv_file_path}")
