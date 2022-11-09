# Virtual Environement
## Interessting Source
- [Using Python Environments in Visual Studio Code](https://code.visualstudio.com/docs/python/environments)
- [A Complete Guide to Python Virtual Environments (2022) – Dataquest](https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/)

## Create a virtual environment
### Windows
In the relevant folder, type the following command in a terminal :
```
python -m venv .venv
```
In this example the virtual environment is called ".venv"

## Activate virtual environment
When the virtual environment is set, the following enable the virtual environment (in this example the virtual environment is store in the ".venv" folder) :

### Windows
```
.venv\Scripts\activate
```

As activation indicator, the terminal command line has the environment's name between parenthesis at its beggining :
```
(.venv) C:\Users\fsc11\Documents\3_PERS_WORKSPACE\knowledge>
```

## Deactivate virtual environment
The virtual environment can be deactivate with the following command (not very useful)

### Windows
```
deactivate
```

## Ususal commands
Different command serves to check if the virtual environment is activate and to check other things.

### List the package installed in the environment
```
pip list
```
The result shows the list of the packages installed the virtual environment and their versions. Directly after the virtual environment creation, this latter contains the following package :
- pip (that may be upgrades directly)
- setuptools