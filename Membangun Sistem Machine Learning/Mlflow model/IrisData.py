import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import random

# Data preparation
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Use a local file-based MLflow tracking store to avoid needing a remote server
mlflow.set_tracking_uri("file:///e:/Asah - Dicoding/mlruns")

# Ensure an experiment exists (will create if missing)
mlflow.set_experiment("IrisExperiment")

input_example = X_train[0:5]

# Start tracking
with mlflow.start_run():
    # Log parameters
    n_estimators = random.randint(10,200)
    max_depth = random.randint(1,50)
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)

    # Enable autologging (captures metrics, params, model automatically)
    mlflow.autolog()

    # Train model
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)

    # Log model artifact after training
    mlflow.sklearn.log_model(sk_model=model, artifact_path="model", input_example=input_example)

    # Log metrics
    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", float(accuracy))

    print(f"Accuracy: {accuracy}")