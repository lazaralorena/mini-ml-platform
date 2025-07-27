# Use the official Python 3.10 image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Add /app to PYTHONPATH so "serve" can be imported from anywhere
ENV PYTHONPATH=/app

# Copy and install build tools before installing project dependencies
RUN pip install --upgrade pip setuptools wheel build

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Start the FastAPI application using Uvicorn
CMD ["uvicorn", "serve.app:app", "--host", "0.0.0.0", "--port", "8000"]