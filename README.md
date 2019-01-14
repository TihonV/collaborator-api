# Requirements

- python version must be 3.6 or newer
- postgresql version must be 9.6 or newer

# Deployment procedure

```bash
# you must clone project to server

# prepare enviroment
python3.6 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt

# at this step you can setup other database setting
# in chem_collaborator/settings.py

# prepare application
python ./manage.py migrate
python ./manage.py collectstatic

# run server
python -m gunicorn chem_collaborator.wsgi:application
```

