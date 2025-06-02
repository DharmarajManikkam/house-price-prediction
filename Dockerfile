# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy everything to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run training script
CMD ["python", "src/train.py"]
