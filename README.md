#Book Finder
An application that calls an external API to find books through Google Books.

##Motivation
This project was written to wotk with REST APIs and learn better software development practices.
Feel free to read the code and leave suggestions to how I can improve any part of it.

##Tech
Built with Flask and Python 3.7. Browse requirements for more details.

##Installation Instructions
- Clone the repository into its own folder.
- Set up a python virtualenv
- Linux/MAC: Activate the virtualenv in bash terminal with `source <your_env_name>/bin/activate`
- Windows: `<your_env_name>\Scrips\activate`
- Run `pip install requirements.txt`
- You'll need to add an evironment variable `export FLASK_APP=application.py`
- You'll also need to add an envorinment variable `export GOOG_API_KEY=<your-api-key>`

##Tests
Tests are written using Python's vanilla unittest framework.

Running `python -m unittest discover tests` will run all the tests.

##Using the project:
If you've set the `FLASK_APP` and `GOOG_API_KEY` variable as described above,
use the command `flask run` from the project root directory to run the applcation locally.

You can log onto it by entering 127.0.0.1:5000 into your web browser.
