# First Let's move to Docker Python Quote

In the following files, we create a docker image, test the docker image, login in docker hub, create a tag for project and then publish our docker image on Hub

>```docker build -t python-project .```
>
>```docker image list```
>
>```docker run -p 9001:9001 python-project```
>
>```docker login```
>
>```docker tag python-project juancvilla/python-api-project:python-project```
>
>```docker image ls```
>
>```docker push juancvilla/python-api-project:python-project```

## Finally, to test docker image try:

```docker run -p 9001:9001 juancvilla/python-api-project:python-project```

fin
