Spam Message Detection System

A Spam Detection Web Application built using Python and Machine Learning.
This project detects whether a message is Spam or Not Spam. The user enters a message in the web interface and the system predicts the result instantly.

---

📌 Project Description

Spam messages are unwanted messages commonly found in emails or SMS.
This project uses Natural Language Processing (NLP) and Machine Learning to classify messages as Spam or Ham (Not Spam).

The system provides a simple web interface where users can enter a message and get a prediction.

---

🚀 Features

- Detects whether a message is Spam or Not Spam
- User-friendly web interface
- Real-time message prediction
- Machine learning based classification
- Simple and lightweight application
- Batch result analysis
- Clean HTML result display

---

🛠 Technologies Used

- Python
- Flask
- Machine Learning
- Scikit-learn
- HTML
- CSS
- Natural Language Processing (NLP)

---

📂 Project Structure

spam-detection-project
│
├── app.py                # Main Flask application
├── index.html            # Home page for entering message
├── result.html           # Displays prediction result
├── batch_result.html     # Displays batch prediction results
├── model.pkl             # Trained spam detection model
├── vectorizer.pkl        # Text vectorizer
├── requirements.txt      # Required Python libraries
└── README.md             # Project documentation

---

⚙️ How It Works

1. User enters a message in the input box on the homepage.
2. The message is sent to the Flask backend (app.py).
3. The message is processed using a trained ML model.
4. The model predicts whether the message is Spam or Not Spam.
5. The result is displayed on the result page.

---

▶️ How to Run the Project

1️⃣ Clone the Repository

git clone https://github.com/your-username/spam-detection-project.git

2️⃣ Go to Project Folder

cd spam-detection-project

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Application

python app.py

5️⃣ Open in Browser

http://127.0.0.1:5000/

---

📊 Example

Input Message:

Congratulations! You won a free iPhone. Click here now.

Output:

Spam

---

📌 Future Improvements

- Add email spam detection
- Improve model accuracy
- Add dataset upload feature
- Create dashboard with spam statistics
- Deploy the project online

---

👩‍💻 Author

Rutuja Tiwari

---

⭐ If you like this project, give it a star on GitHub.
