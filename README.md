# album_api

To create the virtual environment, open a terminal, navigate to this directory and run the following commands:

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r app/requirements.txt
```


Once you have set up your virtual enviroment, run the api server on localhost by running the following command:

```console
$ gunicorn -b localhost:8080 entrypoint:app
```


Once the api server is running, navigate to [localhost:8080/api/v1/docs](http://localhost:8080/api/v1/docs) to view the api docs and manually interact with the api as desired.


To run automated tests, open a new terminal, navigate to this directory and run the following commands:
```console
$ python3 -m venv .venv_test
$ source .venv_test/bin/activate
$ pip3 install -r app/requirements_test.txt 
$ python3 -m pytest "app/tests"
```