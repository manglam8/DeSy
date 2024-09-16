from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from data_preprocessing import load_data, preprocess_data, split_data

# Train the model
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(f"Classification Report:\n {classification_report(y_test, y_pred)}")

def save_model(model, model_path='models/ml_model.pkl'):
    joblib.dump(model, model_path)
    print(f"Model saved at {model_path}")

if __name__ == "__main__":
    df = load_data('data/NSL-KDD-Dataset.csv')
    features, target = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(features, target)
    
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model)

