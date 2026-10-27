import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Age': [25, 30, 45, 35, np.nan, 50],
    'MonthlyCharges': [500, 700, 900, 600, 800, 1000],
    'Tenure': [2, 12, 24, 6, 18, 36],
    'Churn': ['Yes', 'No', 'No', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)
df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)
print(df.describe())
print("Average Monthly Charges:", np.mean(df['MonthlyCharges']))
print(df['Churn'].value_counts())

df['Churn'].value_counts().plot(kind='bar')
plt.title("Customer Churn Analysis")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()

df.boxplot(column='Tenure', by='Churn')
plt.title("Tenure vs Churn")
plt.suptitle("")
plt.show()

