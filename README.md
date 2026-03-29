# 🧬 Tumor Prediction — AI Classifier

[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-GitHub%20Pages-818cf8?style=for-the-badge)](https://vedantthamke01.github.io/Tumor-Prediction-ML/)
[![Python](https://img.shields.io/badge/Python-3.x-38bdf8?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-f472b6?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Flask](https://img.shields.io/badge/Flask-Backend-34d399?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)

A **Logistic Regression** based tumor classifier with a modern, dark-themed web UI. Predicts whether a tumor is **Benign** or **Malignant** based on tumor size and density — with real-time probability scores and an interactive decision boundary visualization.

---

## ✨ Features

- 🤖 **Logistic Regression** model (scikit-learn / pure JS)
- 📊 **Interactive decision boundary plot** with Chart.js
- 🎚️ **Live sliders** for tumor size & density inputs
- 📈 **Probability bars** showing benign vs malignant confidence
- 🌐 **GitHub Pages version** — runs 100% in-browser (no server)
- 🖥️ **Flask version** — full Python backend with matplotlib charts

---

## 🖼️ Preview

```
┌─────────────────┬──────────────────────────────────┐
│ INPUT PARAMS    │  Diagnosis: Malignant ⚠️          │
│                 │                                  │
│ Tumor Size  ──● │  Benign     ████░░░░░░  28%      │
│ Tumor Density ● │  Malignant  ████████░░  72%      │
│                 │                                  │
│ [Predict Now]   │  [Decision Boundary Chart]       │
└─────────────────┴──────────────────────────────────┘
```

---

## 🚀 Live Demo

> 🔗 **[vedantthamke01.github.io/Tumor-Prediction-ML](https://vedantthamke01.github.io/Tumor-Prediction-ML/)**

No setup required — runs entirely in your browser.

---

## 📁 Project Structure

```
Tumor_Prediction/
├── index.html                          # 🌐 GitHub Pages (client-side ML)
├── app.py                              # 🖥️  Flask backend
├── templates/
│   └── index.html                      # Flask UI template
├── Logistic_regression_Decision_Boundray.py  # Original CLI script
├── .gitignore
└── README.md
```

---

## 🖥️ Run Locally (Flask Version)

### Prerequisites

```bash
sudo apt install python3-flask
# numpy, matplotlib, scikit-learn should already be present
```

### Start Server

```bash
python3 app.py
```

Open → [http://localhost:5050](http://localhost:5050)

---

## 🧠 How It Works

### Model
- **Algorithm:** Logistic Regression
- **Features:** `Tumor Size (cm)`, `Tumor Density`
- **Labels:** `0 = Benign`, `1 = Malignant`

### Training Data

| Tumor Size | Tumor Density | Label     |
|:----------:|:-------------:|:---------:|
| 0.5        | 1.5           | Benign    |
| 1.0        | 1.0           | Benign    |
| 1.5        | 0.5           | Benign    |
| 3.0        | 0.5           | Malignant |
| 2.0        | 2.0           | Malignant |
| 1.0        | 2.5           | Malignant |

### Decision Boundary
```
w₀·x₀ + w₁·x₁ + b = 0  →  x₁ = -(w₀·x₀ + b) / w₁
```

---

## 🛠️ Tech Stack

| Layer       | Flask Version         | GitHub Pages Version |
|-------------|----------------------|---------------------|
| ML          | scikit-learn         | Gradient descent JS |
| Chart       | Matplotlib (base64)  | Chart.js            |
| Backend     | Flask (Python)       | None (static)       |
| Frontend    | HTML/CSS/JS          | HTML/CSS/JS         |

---

## 📜 License

MIT © [vedantthamke01](https://github.com/vedantthamke01)
