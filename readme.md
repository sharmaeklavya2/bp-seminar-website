# Seminar Website Generator

This repository contains:

* A JSON file (`context.json`) containing data on a seminar schedule.
* A program that reads the JSON file and outputs a static website for the seminar.

## Features of the website

* Pleasant and simple UI.
* Responsive: works well for many screen sizes, especially mobile and desktop.
* Performant: low page load times and few HTTP requests.
* Light and dark mode friendly:
  switches to light mode or dark mode depending on user's system preferences.
* Time zone handling: specify a default time zone and times will be displayed correctly,
  taking daylight-savings into account. For example, if you specify
  the default timezone as "Europe/Paris",
  then "2021-02-24 15:00:00" will be displayed as "24 February 2021, 03:00 PM CET",
  but "2021-03-31 15:00:00" will be displayed "31 March 2021, 03:00 PM CEST".
  In JavaScript-enabled browsers, when a user hovers over a time, the corresponding time
  in their local timezone will be shown.

## Generating the website

The generator is written in python 3.
First, download the dependencies:

    pip3 install -r requirements.txt

Then, run the generator:

    python3 jinjait.py

The output is written to the file `index.html`.
This repository also contains other assets required by the website:
`script.js`, `style.css`, `sprites.svg`.
To deploy, serve `index.html` and these assets using an HTTP server.

## Making modifications

If you want to make changes to the seminar schedule,
edit `context.json` and regenerate the website.

If you want to make changes to the website's HTML template,
edit `index.html.jinja2` and regenerate the website.
