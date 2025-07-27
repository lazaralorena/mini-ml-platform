# Mini ML Platform

This project simulates a simplified platform for deploying Machine Learning models, composed of:

- Automated training of a model
- Serving via REST API documented with Swagger
- Containerization with Docker and Docker Compose

The API is designed to consume locally trained models. In this example, the Iris dataset is used along with a RandomForestClassifier.

## Project Structure

mini-ml-platform/
├── train/              # Code to train the model
│   └── train.py
├── serve/              # REST API with FastAPI
│   ├── app.py
│   ├── init.py
│   └── model.pkl       # Trained model saved after training
├── tests/              # Automated tests using pytest
│   └── test_api.py
├── Dockerfile          # Docker image of the application
├── docker-compose.yml  # Container orchestration
├── requirements.txt    # List of dependencies
└── README.md           # Instructions and project information

## What the code does

1. `train/train.py`: trains a RandomForest model using the Iris dataset and saves it as serve/model.pkl.
2. `serve/app.py`: implements a REST API using FastAPI that loads the trained model and exposes the /predict endpoint.
3. `Dockerfile` and `docker-compose.yml`: allow training, API serving, and automated testing in isolated containers.
4. The model is accessed inside a Docker container and exposed locally via port `8000`.

## How to Run Locally

### Clone the repository

```bash
git clone https://github.com/lazaralorena/mini-ml-platform.git
cd mini-ml-platform
```

### Create and activate the virtual environment
## Python version used for this project: Python 3.12.10

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
.\venv\Scripts\activate    # Windows
```

### Install dependencies - Python version used: 3.12.10

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Train the model

To train the model inside a Docker container and generate the file `serve/model.pkl`, run:

```bash
docker-compose run --rm train
```

💡 Note: To adapt the platform for other models and datasets, simply modify the `train/train.py` script, training the desired model and saving it as `serve/model.pkl`. The API will automatically load it upon startup.

## Start the API with Docker Compose

After training, start the containers:

```bash
docker-compose up --build
```

## Access Swagger Documentation

Open in your browser: http://localhost:8000/docs

## How to Test the API using Swagger

1. Click the `POST /predict` endpoint
2. Click the "Try it out" button
3. Enter the following request body:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

4. Click "Execute"
5. The response will be a number representing the predicted class. For example:

```json
{
  "prediction": 0
}
```

## Prediction Interpretation

The model trained with the Iris dataset returns the following codes:

- 0: Setosa
- 1: Versicolor
- 2: Virginica

## Run Tests

With Docker:

```bash
docker-compose run --rm test
```

## Main Dependencies

Contained in the `requirements.txt` file:

```
fastapi==0.111.0
uvicorn==0.29.0
scikit-learn==1.4.2
joblib==1.4.2
numpy==1.26.4
pytest==8.2.1
```

## Contact
Lázara Camila  
lazaracamila@gmail.com