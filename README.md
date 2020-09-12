# Requirement?

You must install Python first (recommend python 3.8)

```
git clone git@github.com:huytuong010101/TuViAPI.git
cd TuViAPI
python -m pip install -r requirements.txt
```

# How to start server?

## In Windown: 

```
python TuViAPI\manage.py runserver [port] 
```
( Ex: python TuViAPI\manage.py runserver 8000)

## In Linux: 

```
nohup python TuViAPI\manage.py runserver [port] &
```

```
The website at localhost:port
```

# How to restart server?

In Django, restarting automatically every time you modify any .py file
