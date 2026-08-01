import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Data Analysis Projects\Multiple Linear Regression\kc_house_data (Final Data).csv")

plt.title("Correlation Heatmap")

sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="rocket")

plt.show()
plt.tight_layout()
plt.show()
