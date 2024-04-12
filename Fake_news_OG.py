from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle 
import pandas as pd
from sklearn.model_selection import train_test_split 

app = Flask(__name__)

vectorization = TfidfVectorizer(stop_words='english', max_df=0.7)
loaded_model = pickle.load(open('model.pkl', 'rb')) 
dataset = pd.read_csv('news.csv')
x = dataset['text'] 
y = dataset['label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

def fake_news_det(news):
    xv_train = vectorization.fit_transform(x_train) 
    xv_test = vectorization.transform(x_test) 
    input_data = [news] 
    vectorized_input_data = vectorization.transform(input_data) 
    prediction = loaded_model.predict(vectorized_input_data) 
    return prediction 

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/predict', methods=['POST']) 
def predict():
    if request.method == 'POST':
        message = request.form['message'] 
        pred = fake_news_det(message) 
        print(pred)
        return render_template('home.html', prediction=pred)
    else:
        return render_template('home.html', prediction="Something went wrong")

if __name__ == '__main__':
    app.run(debug=True)
