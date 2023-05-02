FROM python:3.10-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
#This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
#Redirects the python output to container log (terminal) without being forced buffered. Helps seeing Django logs in real time. 
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
#In requirments.txt will avoid installing backports.zoneinfo for python >=3.9 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt


# copy project
COPY . /usr/src/app

EXPOSE 8000
#Docker Image Entry Point
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]