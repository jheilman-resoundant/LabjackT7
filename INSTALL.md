Setup for LabjackT7


Install labjack LJM

https://support.labjack.com/docs/ljm-software-installer-downloads-t4-t7-t8-digit

install python requirements...
... to a venv ...

(on ubuntu)
$ sudo apt install python3-venv -y
(or python way)
$ python3 -m pip install venv

make venv:
$ cd <project_directory>
$ python3 -m venv venv

$ python3 -m pip install -r requirements.txt

... install into base system ...
TBD/not recommended, but basically don't make the venv and use sudo when you have to