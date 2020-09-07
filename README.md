# rt2600ac-py

Python sandbox for Synology RT2600ac router

Utilizes the synology-srm python wrapper
- https://pypi.org/project/synology-srm/

As of now:
  
- List all the available API endpoints
- List certificate
- Get all the hosts, but filter for one specfic known host
- Test mannually passing in an api endpoint request

Using the -v and -vv flags will show you the actual URL being called

    usage: main.py [-h] [--version] [-v] [-vv]

    Just a demonstration of the Synology Router API wrapper

    optional arguments:
      -h, --help           show this help message and exit
      --version            show program's version number and exit
      -v, --verbose        set loglevel to INFO
      -vv, --very-verbose  set loglevel to DEBUG

Note: update username and password with your own!