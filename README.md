If you encounter any issues during this process, ask a backend developer for help!

Python and virtualenv setup:
```
brew install python
pip install virtualenv
```

Django setup:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

After you make changes to your models.py:
```
./manage.py makemigrations
./manage.py migrate
```

Recommended steps for creating your parking app:
1. Think about how to structure your database (your Models and their Fields)
2. Think about what APIs (Views) you'll need and what they should be called (their url paths)
3. Think about how you'd test these APIs

