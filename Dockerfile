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

# Set the environment variables
ENV ENTS_BASE_URL=https://raw.githubusercontent.com/LakinduOshadha/mylocal-data/main/ents \
    CENSUS_BASE_URL=https://raw.githubusercontent.com/nuuuwan/gig-data/master/gig2 \
    GEO_SERVER_URL=https://geo-server.datafoundation.lk \
    API_HOST=0.0.0.0 \
    API_PORT=4000 

COPY config.py .
COPY application /mylocal_service/application
# Expose a port for the API to listen on
EXPOSE 4000

# Run the Python API
CMD ["python", "mylocal_service.py"]
