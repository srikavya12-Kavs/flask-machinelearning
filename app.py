from flask import Flask, request, render_template
import pickle

# Initialize Flask app
app = Flask(__name__)

with open('updated_news.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the HTML form

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input from the form
    news_text = request.form['news']
    if not news_text:
        return "Please enter news content.", 400

    # Predict using the loaded model
    prediction = model.predict([news_text])  # No preprocessing needed; the pipeline handles it
    result = "Fake News" if prediction[0] == "FAKE" else "Real News"

    return render_template('index.html', prediction_text=f'Prediction: {result}')

