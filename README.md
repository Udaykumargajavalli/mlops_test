# Hotel Booking Prediction Project

This repository serves as a sandbox for implementing MLOps practices, focusing on automating the machine learning lifecycle, including model training, deployment, and monitoring.

---

## 📁 Project Structure

```
mlops_test/
├── application.py                  # Flask API for model inference
├── Dockerfile                      # Docker config for containerizing the app
├── Jenkinsfile                     # Jenkins CI/CD pipeline script
├── requirements.txt                # Python dependencies
├── setup.py                        # Setup script for packaging
├── artifacts/                      # Intermediate/final pipeline outputs
├── config/                         # Environment and pipeline configs
├── custom_jenkins/                 # Jenkins automation scripts
├── notebook/                       # Jupyter notebooks for prototyping
├── pipeline/                       # Training pipeline components
├── src/                            # Source code (data processing, training, etc.)
├── static/, templates/             # Flask web assets
├── test/                           # Test scripts for components

```

---

## 🛠️ Getting Started

### ✅ Prerequisites

- Python 3.7+
- Google Cloud SDK
- Docker
- Jenkins

### 🔧 Installation

```bash
git clone https://github.com/Udaykumargajavalli/mlops_test.git
cd mlops_test
pip install -r requirements.txt
```

Set Google Cloud credentials (if needed):

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
```

---

## 🚀 Usage

### Run Flask App Locally

```bash
python application.py
```
Visit `http://localhost:5000/` in your browser.

### Docker Setup

```bash
docker build -t mlops_test .
docker run -p 5000:5000 mlops_test
```

### CI/CD with Jenkins

Configure Jenkins to use the `Jenkinsfile` in this repo for automating:
- Build
- Test
- Deployment

---

## 🧪 Testing

Run test scripts:

```bash
python test.py
python test_model.py
python test_mlflow.py
```

---

## 🌐 Live App

[Hotel Booking Status](https://mlopstest-749453970254.us-central1.run.app/)
