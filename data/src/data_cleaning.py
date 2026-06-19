import pandas as pd

# 1. Data inladen
df = pd.read_csv("data/sales_data.csv")

# 2. Eerste kijkje in data
print("Eerste rijen:")
print(df.head())

# 3. Missing values check
print("\nMissing values:")
print(df.isnull().sum())

# 4. Data schoonmaken
df = df.dropna()
df = df.drop_duplicates()

# 5. Kolommen netjes maken
df.columns = df.columns.str.lower()

# 6. Analyse (belangrijk voor werkgevers)
print("\nTotale sales:", df["sales"].sum())
print("Gemiddelde sales:", df["sales"].mean())

# 7. Output opslaan
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nKLAAR: data is schoongemaakt")
