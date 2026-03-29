import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Train model once at startup
X = np.array([[0.5,1.5],[1,1],[1.5,0.5],[3,0.5],[2,2],[1,2.5]])
Y = np.array([0,0,0,1,1,1])
model = LogisticRegression()
model.fit(X, Y)

def build_plot(x0, x1):
    fig, ax = plt.subplots(figsize=(7, 5))
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#1e293b')

    ax.scatter(X[Y==0][:,0], X[Y==0][:,1], color='#38bdf8', s=100, label='Benign', zorder=3)
    ax.scatter(X[Y==1][:,0], X[Y==1][:,1], color='#f472b6', marker='x', s=120,
               linewidths=2.5, label='Malignant', zorder=3)

    w = model.coef_[0]
    b = model.intercept_[0]
    x_vals = np.linspace(0, 4, 200)
    y_vals = -(w[0] * x_vals + b) / w[1]
    ax.plot(x_vals, y_vals, color='#a78bfa', linewidth=2, linestyle='--', label='Decision Boundary')

    ax.scatter(x0, x1, marker='*', s=300, color='#fbbf24', zorder=5,
               label='Your Input', edgecolors='white', linewidths=0.6)

    ax.set_xlabel('Tumor Size', color='#cbd5e1', fontsize=11)
    ax.set_ylabel('Tumor Density', color='#cbd5e1', fontsize=11)
    ax.tick_params(colors='#94a3b8')
    for spine in ax.spines.values():
        spine.set_edgecolor('#334155')
    ax.legend(facecolor='#1e293b', labelcolor='#e2e8f0', edgecolor='#334155')
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)

    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=110)
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_b64

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    x0 = float(data['size'])
    x1 = float(data['density'])
    inp = np.array([[x0, x1]])
    pred = model.predict(inp)[0]
    prob = model.predict_proba(inp)[0]
    label = 'Malignant' if pred == 1 else 'Benign'
    chart = build_plot(x0, x1)
    return jsonify({
        'label': label,
        'benign_prob': round(float(prob[0]) * 100, 1),
        'malignant_prob': round(float(prob[1]) * 100, 1),
        'chart': chart
    })

if __name__ == '__main__':
    app.run(debug=True, port=5050)
