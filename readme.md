# Seminar Website Generator

This repository contains:

* A JSON file (`context.json`) containing data on a seminar schedule.
* A program that reads the JSON file and outputs a static website for the seminar.

## Generating the website

The generator is written in python 3.
First, download the dependencies:

    pip3 install -r requirements.txt

Then, run the generator:

    python3 jinjait.py index.html.jinja2 context.json index.html

The output is written to the file `index.html`.
This repository also contains other assets required by the website:
`script.js`, `style.css`, `sprites.svg`.
To deploy, serve `index.html` and these assets using an HTTP server.

## Making modifications

If you want to make changes to the seminar schedule,
edit `context.json` and regenerate the website.

If you want to make changes to the website's HTML template,
edit `index.html.jinja2` and regenerate the website.
