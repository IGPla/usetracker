# usetracker
usetracker is a Django app, that will allow you to keep tracking of all dynamic calls on your server, and then, query them

![Raw data query](https://github.com/IGPla/usetracker/blob/master/raw/images/showcase1.jpg "Raw data query")
![Chart data query](https://github.com/IGPla/usetracker/blob/master/raw/images/showcase2.jpg "Chart data query")

## Requirements
 - django version >= 1.7

## Install
 - Clone git repo ```git clone https://github.com/IGPla/usetracker.git```
 - Add 'usetracker' in your apps settings (INSTALLED_APPS)
 - Add  'usetracker.middlewares.UseTrackerMiddleware' in your middleware settings (MIDDLEWARE_CLASSES)
 - Install requirements.txt (for example, with pip, ``` pip install -r usetracker/requirements.txt```)
 - Execute your migrations ```python manage.py migrate```
 - Add url endpoint (for example, ```url(r'^usetracker/', include("usetracker.urls")),```)

## Usage
Now you only need to navigate to your usetracker root, and start querying for database.
