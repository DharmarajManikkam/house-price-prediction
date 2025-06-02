FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Run the training script to generate the model
RUN python src/train.py

# Start the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
