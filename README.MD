1. set up virtual environment
python3.8 -m venv venv
source venv/bin/activate

2. create requirements.txt and install all packages
pip3 install -r requirements.txt

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
pytest taskmanager/main/tests-django/tests/ui/
###############################################################
