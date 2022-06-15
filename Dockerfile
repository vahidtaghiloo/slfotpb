# set base image
FROM python:slim-buster

# set the working directory in the container
WORKDIR /code

# install dependencies
RUN apt-get update && apt-get install -y git cron

# copy cronjob file
COPY sample-crontab /etc/cron.d/sample-crontab

# register crontab file

RUN chmod 0644 /etc/cron.d/sample-crontab &&\
    crontab /etc/cron.d/sample-crontab

# copy the dependencies file to the working directory
COPY requirements.txt .

# install python code dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start

ENTRYPOINT ["cron", "-f"] 