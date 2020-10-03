# AnonFiles_uploader


## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Examples](#Examples)



## General info
>Automatically upload files to anonshare, with the possibility to use a proxy, including tor. 
Even you have the option to output information of the file




## Setup

***Install requirements***

`pip3 install requirements.txt`

***In first execution a folder named 'upload' will be created, just move your file there to upload it.***

`python3 anonfiles_uploader.py`





## Examples

***For basic info:***

`python3 anonfiles_uploader.py -h`

![alt text](https://i.imgur.com/tCbVFbE.png)


***In this command we are uploading 'test.zip', with tor proxy, and an output in /home/User/Documents/:***

`python3 anonfiles_uploader.py -f test.zip -t True -o /home/User/Documents/`

![alt text](https://i.imgur.com/7fkB0ce.jpeg)


***In this command we are uploading 'test.zip', with a custom https proxy, and an output in /home/User/Documents/:***

`python3 anonfiles_uploader.py -f test.zip -p 103.42.195.70:53281 -o /home/User/Documents/`

![alt text](https://i.imgur.com/g2urSOA.jpeg)




