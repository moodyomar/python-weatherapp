# Python Webapp CI/CD ready


<img alt="devmoody" src="https://github.com/moodyomar/python-weatherapp/blob/develop/preview.png" width="350">

to run the app <br>
`python3 main.py`

to run unitests <br>
`python3 -m unitest`

to build docker image <br>
`docker build -t your_user_name/image_name:tag`

to run the app with nginx and gunicorn with docker-compose <br>
`docker-compose up -d`

to deploy on K8S cluster use the deployment.yaml file, Run <br>
`kubectl create -f deployment.yaml`
