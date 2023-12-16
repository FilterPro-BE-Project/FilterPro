from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Load dataset

text = pd.read_csv("C:/Users/rauna/Downloads/updated_email (2).csv")  # List of text examples
texts=text['text']
labels = text['urgency'] 

# Preprocess text
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train logistic regression model
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)
print(y_train)

# Evaluate model on test set
score = clf.score(X_test, y_test)
print("Accuracy:", score)
# Use model to classify new text example
