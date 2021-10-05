1. set up virtual environment
source env/bin/activate

2. create requirements.txt and install all packages
python -m pip install Django

3. create a project, which ia a container for site
django-admin startproject name [directory]
this command will create a directory with files

4. run localhost project (with cd before)
python3 manage.py runserver

5. update db
python3 manage.py makemigrations
python3 manage.py migrate

###########################TEST RUN:###########################
1. run functional tests
taskmanager/main/templates/tests/functional_tests.py

2. run module tests (without run server)
python3 manage.py test main/templates/tests/
###############################################################
