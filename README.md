
## My own personal TEMPLATE and usfull commands

## Temp
- custom user model
- auth with JWT
- profiles
- 2 apps(uuid,FK,time)
- .env
- image, files

## Setup
* python -m virtualenv myenv
* .\myenv\Scripts\activate
* pip install requirements.txt

## Usfull commands
* py .\manage.py makemigrations
* py .\manage.py migrate
* py .\manage.py runserver
* py .\manage.py createsuperuser
* pip freeze > requirements.txt
* django-admin startproject myproj .    (the dot is part of the command)
* django-admin startapp (app name)	


## Superuser:
Email: or@mail.com
Username: or
password: 123

## Seed DB:
* py ./manage.py dumpdata db.json
* py ./manage.py loaddata db.json


## Git
* git init
* git add .
* git commit -m "commit name"
* git branch -M main
* git remote add origin (link to github repo)
* git push -u origin main

## Git branch
*  git pull
*  git checkout -b "bramchname/xxx"
*  git add (files)
*  git commit -m "useful comment"
*  git push --set-upstream origin (branch-name)

* Create pull request.
* Merge.