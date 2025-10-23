# Use an official Python runtime as a parent image
# Using a "slim" version keeps the image size smaller
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port the app runs on (Flask default is 5000)
EXPOSE 5000

# Define environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# The command to run your application using Flask's built-in server
# This is great for development but not recommended for production
CMD ["flask", "run"]



