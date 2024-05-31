from python:3.8-slim


label maintainer=loki


run pip install --upgrade pip 
run  pip install flask


workdir /app

copy . .
 
expose 5000

CMD ["python", "./app.py"]




