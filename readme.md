# Seminar Website Generator

This repository contains:

* A JSON file (`context.json`) containing data on a seminar schedule.
* A program that reads the JSON file and outputs a static website for the seminar.

## Generating the website

The generator is written in python.
First, download the dependencies:

    pip install -r requirements.txt

Then, run the generator:

    python jinjait.py index.html.jinja2 context.json index.html

The output is written to the file `index.html`.
This repository also contains other assets required by the website, like CSS and images.
Simply serve all files in this directory using an HTTP server.

## Making modifications

If you want to make changes to the seminar schedule,
edit `context.json` and regenerate the website.

If you want to make changes to the website's HTML template,
edit `index.html.jinja2` and regenerate the website.
