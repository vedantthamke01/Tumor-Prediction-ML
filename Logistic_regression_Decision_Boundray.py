import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

X = np.array([[0.5,1.5],[1,1],[1.5,0.5],[3,0.5],[2,2],[1,2.5]])
Y = np.array([0,0,0,1,1,1])

model = LogisticRegression()
model.fit(X,Y)

X0 = float(input("Enter the  tumor size: "))
X1 = float(input("Enter the tumor density: "))

input_data = np.array([[X0, X1]])
prediction = model.predict(input_data)
probability = model.predict_proba(input_data)
make 
if prediction[0] == 1:
    print("The tumor is malignant.") 
else:
    print("The tumor is benign.")

print(f"Probability of being benign: {probability[0][0]:.2f}")
print(f"Probability of being malignant: {probability[0][1]:.2f}")

# ---------------- GRAPH ----------------
plt.scatter(X[Y==0][:,0], X[Y==0][:,1], label="Class 0 (Benign)")
plt.scatter(X[Y==1][:,0], X[Y==1][:,1], marker='x', label="Class 1 (Malignant)")

# decision boundary
w = model.coef_[0]
b = model.intercept_[0]

x_vals = np.linspace(0,4,100)
y_vals = -(w[0]*x_vals + b)/w[1]

plt.plot(x_vals, y_vals, label="Decision Boundary")

# plot user point
plt.scatter(X0, X1, marker='*', s=200, label="Your Input")

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()