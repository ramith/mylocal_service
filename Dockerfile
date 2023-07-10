FROM python:3.10.9-slim-buster
WORKDIR /mylocal_service

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

# Copy the requirements.txt file to the container
COPY requirements.txt .

RUN apt-get update && apt-get install libgl1 libglib2.0-0 -y

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy files to the container
COPY mylocal_service.py .

COPY config.py .
COPY application /mylocal_service/application
# Expose a port for the API to listen on
EXPOSE 4000

# Run the Python API
CMD ["python", "mylocal_service.py"]
