from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import string
import re
import numpy as np
import pandas as pd
from datetime import datetime
import secrets
print(secrets.token_hex(32))

app = Flask(__name__)
app.secret_key = 'generated_secure_key_here'  # Required for session handling

# Load models
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message", "")
        session['analysis_data'] = analyze_message(message)
        return redirect(url_for('results'))
    return render_template("index.html")

@app.route("/results")
def results():
    data = session.get('analysis_data', {})
    if not data:
        return redirect(url_for('index'))
    return render_template("results.html", data=data)

@app.route("/batch", methods=["GET", "POST"])
def batch():
    if request.method == "POST":
        if 'file' not in request.files:
            return render_template("batch.html", error="No file uploaded")
            
        file = request.files['file']
        if file.filename == '':
            return render_template("batch.html", error="No file selected")
            
        try:
            if file.filename.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.filename.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file)
            else:
                return render_template("batch.html", error="Unsupported file format")
                
            if 'message' not in df.columns:
                return render_template("batch.html", error="CSV must contain 'message' column")
                
            results = []
            for msg in df['message']:
                results.append(analyze_message(msg))
            
            session['batch_results'] = results
            return redirect(url_for('batch_results'))
            
        except Exception as e:
            return render_template("batch.html", error=str(e))
    
    return render_template("batch.html")

@app.route("/batch-results")
def batch_results():
    results = session.get('batch_results', [])
    if not results:
        return redirect(url_for('batch'))
    
    stats = {
        'total': len(results),
        'spam': sum(1 for r in results if r['is_spam']),
        'ham': sum(1 for r in results if not r['is_spam']),
        'avg_confidence': np.mean([r['confidence'] for r in results]),
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return render_template("batch_results.html", results=results, stats=stats)

def analyze_message(message):
    cleaned = clean(message)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    confidence = np.max(model.predict_proba(vec)) * 100
    
    return {
        'original_message': message,
        'cleaned_message': cleaned,
        'is_spam': bool(prediction),
        'prediction': "Spam" if prediction else "Not Spam",
        'confidence': round(confidence, 1),
        'features': {
            'length': len(message),
            'words': len(message.split()),
            'links': len(re.findall(r'http\S+', message)),
            'uppercase_ratio': sum(1 for c in message if c.isupper()) / len(message) if message else 0
        },
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    app.run(debug=True)
