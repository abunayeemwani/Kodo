Setup

The first thing to do is to clone the repository:

$ git clone https://github.com/zeeshanwani/Kodo.git

$ cd kodocards


Create a virtual environment to install dependencies in and activate it:

$ virtualenv venv

$ venv/Scripts/activate (Windows)

$ source venv/bin/activate (Linux)

Then install the dependencies:


(venv)$ pip install -r requirements.txt


Once pip has finished downloading the dependencies:

(venv)$ python manage.py runserver

And navigate to http://127.0.0.1:8000/assignment1/.

For API navigate to http://127.0.0.1:8000/get_api/.
