import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("students.csv")
df["average"] = df[["math", "physics", "history", "english"]].mean(axis=1)

X = np.array(range(len(df))).reshape(-1, 1)
y = df["average"].values

model = LinearRegression()
model.fit(X, y)

future = np.array([[5], [6], [7]])
predictions = model.predict(future)

print("Болашақ болжам:")
for i, pred in enumerate(predictions):
    print(f"Студент {i+6}: {round(pred, 2)}")

plt.figure(figsize=(8, 5))
plt.scatter(X, y, color="steelblue", label="Нақты балл")
plt.plot(X, model.predict(X), color="red", label="Тренд")
plt.title("Үлгерім болжамы")
plt.xlabel("Студент")
plt.ylabel("Орташа балл")
plt.legend()
plt.tight_layout()
plt.show()