# Test Project 1 - Starter Notebook

import pandas as pd
import matplotlib.pyplot as plt
import os

# Adjust if needed (works for both local and Colab)
DATA_PATH = 'data/sample.csv'

# Load the dataset
try:
    df = pd.read_csv(DATA_PATH)
    print("✅ Data loaded successfully!")
except FileNotFoundError:
    print(f"❌ Could not find {DATA_PATH}. Please upload it.")

# Quick preview
df.head()

# Simple plot (if columns exist)
if 'x' in df.columns and 'y' in df.columns:
    plt.plot(df['x'], df['y'])
    plt.title("Sample Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
