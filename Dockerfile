# base image  
FROM docker.arvancloud.ir/python:3.11   

#SET ENV's
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# where your code lives  
WORKDIR /app

# Install dependencies
COPY ./requirements.txt  /app/requirements.txt
RUN pip install -r /app/requirements.txt  

COPY . /app/

#make migrations command
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
