# Movie Genre Classification

This project predicts the genre of a movie using its plot summary.  
It uses Machine Learning (TF-IDF + Linear SVC) and includes a Streamlit web application.

------------------------------------

## Project Files
- app.py → Streamlit web application for predicting movie genre  
- movie_genre_model.joblib → Trained machine learning model  
- requirements.txt → List of required Python libraries  
- final_movie_genre.ipynb → Jupyter notebook containing full model training  
- .venv → Virtual environment (ignored in Git)

------------------------------------

## How to Run This Project (Windows)

1. Open the project folder in terminal:
   cd C:\Users\syedt\movieGenre

2. Activate the virtual environment:
   .venv\Scripts\activate

3. Install required libraries:
   pip install -r requirements.txt

4. Download NLTK data (only the first time):
   python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"

5. Start the Streamlit app:
   streamlit run app.py

After running, the app will automatically open in your browser at:
http://localhost:8501

------------------------------------

## Model Details
• Text cleaning: lowercase, remove special characters, remove stopwords  
• Lemmatization: using WordNetLemmatizer  
• Feature extraction: TF-IDF Vectorizer  
• Machine Learning model: Linear Support Vector Classifier  
• Hyperparameter tuning: RandomizedSearchCV  
• Evaluation metric: F1-Macro Score  

Example score (replace with your real score):
F1 Score: 0.87

------------------------------------

## Project Structure

movieGenre/
│   app.py  
│   movie_genre_model.joblib  
│   requirements.txt  
│   final_movie_genre.ipynb  
│   README.md  
│   .venv/ (virtual environment)

------------------------------------

## Author
SATHESH  
Machine Learning Intern  
GitHub: https://github.com/SATHESH214  
Project Repo: https://github.com/SATHESH214/CODSOFT-

