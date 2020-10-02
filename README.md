# AnonFiles_uploader
Automatically upload files to anonshare, with the possibility to use a proxy, including tor.
Even you have the option of output information of the file

***Install requirements***
>pip3 install requirements.txt

***In first execution a folder will be created, just move your file there to upload it.***
> python3 anonfiles_uploader.py

***For more information:***
>python3 anonfiles_uploader.py -h

***Example of use:***
>python3 anonfiles_uploader.py -f test.zip -t True -o /home/User/Documents/

***In this command we are uploading 'test.zip', with tor proxy, and an output in /home/User/Documents/***
