# Use an official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY multithreading.py /app

# Set environment variable to prevent Python from buffering stdout/stderr (useful for logging)
ENV PYTHONUNBUFFERED=1

# Command to run the Python script
CMD ["python", "multithreading.py"]
