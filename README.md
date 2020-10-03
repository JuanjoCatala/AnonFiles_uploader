## AnonFiles_uploader

Automatically upload files to anonshare, with the possibility to use a proxy, including tor.

Even you have the option of output information of the file


***Install requirements***
>pip3 install requirements.txt

***In first execution a folder named 'upload' will be created, just move your file there to upload it.***
> python3 anonfiles_uploader.py

***For more information:***
>python3 anonfiles_uploader.py -h

![alt text](https://i.imgur.com/tCbVFbE.png)

#***Example of use:***

>python3 anonfiles_uploader.py -f test.zip -t True -o /home/User/Documents/

***In this command we are uploading 'test.zip', with tor proxy, and an output in /home/User/Documents/***

![alt text](https://i.imgur.com/7fkB0ce.jpeg)

>python3 anonfiles_uploader.py -f test.zip -p 103.42.195.70:53281 -o /home/User/Documents/

***In this command we are uploading 'test.zip', with a custom https proxy, and an output in /home/User/Documents/***

![alt text](https://i.imgur.com/g2urSOA.jpeg)




