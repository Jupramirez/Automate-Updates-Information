# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Create the uploads directory inside the container
RUN mkdir -p static/uploads

# 6. Inform Docker that the container listens on port 5000
EXPOSE 5000

# Copy the rest of your application code
COPY . .

# 7. Define the command to run your app
CMD ["python", "app.py"]