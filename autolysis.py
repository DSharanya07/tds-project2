# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "pandas",
#   "matplotlib",
#   "seaborn",
#   "openai",
#   "python-dotenv",
# ]
# ///

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openai
from dotenv import load_dotenv

def main():
    if len(sys.argv) < 2:
        print("Usage: uv run autolysis.py <happiness.csv>")
        sys.exit(1)

    dataset_file = sys.argv[1]

    if dataset_file.startswith("-"):
        print("Error: Please provide a valid dataset file (CSV).")
        sys.exit(1)

    if not os.path.isfile(dataset_file):
        print(f"Error: The file '{dataset_file}' does not exist.")
        sys.exit(1)

    print(f"Processing dataset: {dataset_file}")

    try:
        df = pd.read_csv(dataset_file)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

    print(f"Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
    print("Summary statistics:")
    print(df.describe())

    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.savefig("correlation_matrix.png")
    print("Saved correlation matrix as 'correlation_matrix.png'.")

if __name__ == "__main__":
    main()
