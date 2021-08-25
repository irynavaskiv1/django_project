1. set up virtual environment
source env/bin/activate

2. create requirements.txt and install all packages
python -m pip install Django

3. create a project, which ia a container for site
django-admin startproject name [directory]
this command will create a directory with files

4. run localhost project (with cd before)
python3 manage.py runserver


python3 manage.py makemigrations
python3 manage.py migrate

TODO list:
- add mobile support
- add correct photo
- add padding for new photo in religion block
- add additional info for contacts block
- test with different browsers and platforms
- add chat support
- create base html file
