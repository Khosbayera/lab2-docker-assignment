# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . /app

# Expose port 80
EXPOSE 80

# Run the app
CMD ["python", "app.py"]
