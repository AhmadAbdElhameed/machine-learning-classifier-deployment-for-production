## How to use it

1- put all files in the same directory 
2- open terminal & run docker build --tag rf_clf .
3- image will built and you can see it by running : docker images
4- then run our image as a container by running : docker run -p 3000:5000 rf_clf
5- in your browser go to : localhost:5000/apidocs/
6- you can see two apies for prediction first on take four inputs
7- second api for prediction by file
8- to stop container open another terminal and stop run : docker stop container_id
