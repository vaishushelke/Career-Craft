import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# 1. Define Training Data (Skills to Career mapping)
data = [
    ("html css javascript react vue angular frontend typescript sass bootstrap tailwind", "Front-end Developer"),
    ("python flask django node.js express backend java spring boot sql postgresql mongodb apis", "Back-end Developer"),
    ("python pandas numpy scikit-learn statistics data science machine learning visualization matplotlib seaborn r sql", "Data Scientist"),
    ("machine learning ai artificial intelligence tensorflow pytorch deep learning nlp cv keras neural networks", "AI/ML Engineer"),
    ("sql oracle mysql postgresql dba database administration management backup query optimization indexing", "Database Administrator"),
    ("android kotlin swift ios flutter mobile react native mobile development", "Mobile App Developer"),
    ("aws azure cloud devops docker kubernetes jenkins ci/cd linux sysadmin terraform", "DevOps Engineer")
]

X_train = [d[0] for d in data]
y_train = [d[1] for d in data]

# 2. Define Roadmap Steps (Career to Steps mapping)
roadmaps = {
    "Front-end Developer": "Learn HTML/CSS & Modern Layouts|Master JavaScript (ES6+)|Build Projects with React or Vue|Learn State Management (Redux/Pinia)|Understand Responsive Design & Web Accessibility",
    "Back-end Developer": "Master a Backend Language (Python/Node/Java)|Understand Relational Databases (SQL)|Design & Build RESTful APIs|Learn Authentication & Security|Deploy to Heroku/AWS/Vercel",
    "Data Scientist": "Master Python for Data Science (Pandas/NumPy)|Learn Exploratory Data Analysis (EDA)|Understand Machine Learning Algorithms|Master SQL for Data Extraction|Build a Portfolio of Real-world Projects",
    "AI/ML Engineer": "Master Linear Algebra & Calculus|Learn Key ML Libraries (Scikit-learn)|Deep Dive into TensorFlow or PyTorch|Understand NLP & Computer Vision|Optimize & Deploy Models to Production",
    "Database Administrator": "Master SQL & Relational Algebra|Learn Database Design & Normalization|Understand Indexing & Performance Tuning|Master Backup & Disaster Recovery|Learn Cloud Database Solutions (RDS/Cloud SQL)",
    "Mobile App Developer": "Learn Kotlin (Android) or Swift (iOS)|Understand UI/UX Design Patterns|Master State Management & API Integration|Learn Cross-platform Tools (Flutter/React Native)|Publish to Play Store/App Store",
    "DevOps Engineer": "Master Linux Command Line|Learn Continerization with Docker|Understand Orchestration with Kubernetes|Implement CI/CD Pipelines|Learn Infrastructure as Code (Terraform)"
}

# 3. Create and Train the Pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

model.fit(X_train, y_train)

# 4. Save results to 'model/' directory
model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model')
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

model_path = os.path.join(model_dir, 'career_model.pkl')
roadmap_path = os.path.join(model_dir, 'roadmaps.pkl')

joblib.dump(model, model_path)
joblib.dump(roadmaps, roadmap_path)

print(f"✅ Career Roadmap Model trained and saved!")
print(f"📂 Model: {model_path}")
print(f"📂 Roadmaps: {roadmap_path}")
