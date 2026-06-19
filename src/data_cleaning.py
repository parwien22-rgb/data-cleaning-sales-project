import pandas as pd

# Data inladen
df = pd.read_csv("data/sales_data.csv")

# Eerste kijkje in de data
print("Eerste rijen:")
print(df.head())

# Missing values checken
print("\nMissing values:")
print(df.isnull().sum())

# Data schoonmaken
df = df.dropna()
df = df.drop_duplicates()

# Kolomnamen netjes maken
df.columns = df.columns.str.lower()

# Analyse
print("\nTotale sales:", df["sales"].sum())
print("Gemiddelde sales:", df["sales"].mean())

# Opslaan van schone data
df.to_csv("data/cleaned_sales_data.csv", index=False)

print("\nKLAAR: data is schoongemaakt")
