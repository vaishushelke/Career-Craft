import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib
import os

# Define absolute path based on script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'dataset.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'career_model.pkl')
ROADMAP_PATH = os.path.join(BASE_DIR, 'roadmaps.pkl')

def train():
    print("Loading dataset...")
    df = pd.read_csv(DATA_PATH)
    
    # We will build a model that predicts Career_Role based on Skills
    print("Training model...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    X = df['Skills']
    y = df['Career_Role']
    
    pipeline.fit(X, y)
    
    # Save the pipeline
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    
    # Also save the roadmap mappings dictionary for quick lookup
    # Creating a unique mapping from Career_Role to Roadmap
    roadmap_dict = df.drop_duplicates(subset=['Career_Role']).set_index('Career_Role')['Roadmap'].to_dict()
    joblib.dump(roadmap_dict, ROADMAP_PATH)
    print(f"Roadmap dictionary saved to {ROADMAP_PATH}")

if __name__ == '__main__':
    train()
