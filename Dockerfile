# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies needed for building Python packages
RUN apt-get update && apt-get install -y \
    pkg-config \
    libhdf5-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the application
CMD ["python3", "app.py"]
