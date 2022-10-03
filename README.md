### Description

It is a solution to [this](assets/task/task.md) test problem.

### Notes

- Python <ins>3.8</ins> was used in development environment, as well as in Docker image;
- The code is deployed via Github Actions and Amazon ECS;
- There are three files with dependencies declaration: [Pipfile](Pipfile), [Pipfile.lock](Pipfile.lock) and [requirements.txt](requirements.txt). I use the first two in development environment on my machine with pipenv and the third one for docker image (turns out pipenv isn`t really meant to be used inside Docker, so it is just more convenient to use requirements.txt in Dockerfile);
- Sample data to try it out is included in the repo [here](static/samples) and can be accessed from the frontend as well;

### Demonstration

_The gif below is 40 Mb and might take a while to load. Sorry!_

<img src="assets/demo.gif" style="width:100%; max-width: 100%;">

### Algorithm explanation

All the work is done in these three lines:

```python
with fiona.open(shapefile_name) as shapefile:
    for record in shapefile:
        plt.plot(*zip(*record['geometry']['coordinates']), linewidth=0.5)
```

Somewhat simplistic, but it gets the job done 🤷‍♂️

### How to run locally

##### In Docker

Clone git repo:

`git clone https://github.com/v-spassky/gisture.git`

Navigate to the project folder:

`cd gisture`

Build the image:

`sudo docker build -t gisture .`

Run the image:

`sudo docker run -d -p 8000:8000 gisture`

Now the app is available on localhost:8000.

##### In virtual environment

Clone git repo and navigate to the project folder:

`git clone https://github.com/v-spassky/gisture.git`

`cd gisture`

Initialize virtual environment with the tool of your choice, activate it and install dependencies listed in [requirements.txt](requirements.txt) or [Pipfile](Pipfile).

`python3 -m virtualenv .`

`source bin/activate`

`pip install -r requirements.txt`

Run the app:

`gunicorn app:app`

Now the app is running on localhost:8000.
