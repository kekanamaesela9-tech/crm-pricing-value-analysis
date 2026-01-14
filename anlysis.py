import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import log

# ===============================
# LOAD FINAL DATASET
# ===============================
df = pd.read_csv("crm_products_analysis.csv")

# ===============================
# RANKING BY VALUE SCORE
# ===============================
df = df.sort_values(by="value_score", ascending=False)

print("\nRANKING BY VALUE SCORE (HIGH → LOW):")
print(df[["product_name", "rating", "review_count", "max_price", "value_score"]])

# ===============================
# PRICE VS VALUE CHART
# ===============================
plt.figure()
plt.scatter(df["max_price"], df["value_score"])

for i, name in enumerate(df["product_name"]):
    plt.text(df["max_price"].iloc[i], df["value_score"].iloc[i], name)

plt.xlabel("Max Price (USD)")
plt.ylabel("Value Score")
plt.title("CRM Products: Price vs Perceived Value")

plt.show()

