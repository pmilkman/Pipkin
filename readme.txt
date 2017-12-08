/* create new django project*/
django-admin startproject [mysite]

/* create a new app [polls] in [mysite]*/
python manage.py startapp polls

/* start the django server */
python manage.py runserver


/*create a migration script - sql*/
python manage.py makemigrations pipkin

/*get the migtation script as text*/
python manage.py sqlmigrate pipkin 0008

/*run migration script on db*/
python manage.py migrate


/*open django shell*/
python manage.py shell


/*open danjgo shell an execute a py-script*/
python manage.py shell < myscript.py


/*create superuser for a project*/
python manage.py createsuperuser
  --username: admin
  --pwd: SPAadmin


