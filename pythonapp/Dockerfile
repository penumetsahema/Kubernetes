# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script to the container
COPY app.py .

# Install the necessary dependencies
RUN pip install flask mysql-connector-python

# Expose the port your Flask app will be running on
EXPOSE 3010

# Run the Python script when the container starts
CMD [ "python", "app.py" ]
