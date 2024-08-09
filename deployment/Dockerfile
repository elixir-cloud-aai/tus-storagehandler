##### BASE IMAGE #####
FROM elixircloud/foca:20240711-py3.12

##### METADATA ##### 
LABEL software="Cloud Storage Handler"
LABEL software.description="API for handling files on a cloud storage service"
LABEL software.website="https://github.com/elixir-cloud-aai/tus-storagehandler"
LABEL maintainer.organisation="ELIXIR Cloud & AAI"

## Copy app files
COPY ./tus_storage_handler /app

## Install app
RUN cd /app \
  && poetry install \
  && poetry shell \
  && python app.py    

WORKDIR /app

CMD ["python", "tus_storage_handler/app.py"]