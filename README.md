# Quiz App
Simple quiz app with Django, DRF, GraphQL and a little bit JS .

## Features
- Authentication
  - login
  - register
  - profile
- Timer (for each question 10 second)
- Quiz result (at the end of the exam)



### Usage :
```bash
git clone https://github.com/Aron-S-G-H/quizApp.git
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver # and see in localhost:8000
# In another terminal, enter the following command to run celery
celery -A QuizApp worker -l info
# Again in another terminal, enter the following command to run flower
celery -A QuizApp flower
# you also need RabbitMQ as broker
```

---
#### any contributions are welcome
