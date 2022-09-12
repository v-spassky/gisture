### Description

It is a solution to [this](assets/task/task.md) test problem. Hosted **[<span style="color: white; background: linear-gradient(
        90deg,
        rgba(255, 0, 0, 1) 0%,
        rgba(255, 154, 0, 1) 10%,
        rgba(208, 222, 33, 1) 20%,
        rgba(79, 220, 74, 1) 30%,
        rgba(63, 218, 216, 1) 40%,
        rgba(47, 201, 226, 1) 50%,
        rgba(28, 127, 238, 1) 60%,
        rgba(95, 21, 242, 1) 70%,
        rgba(186, 12, 248, 1) 80%,
        rgba(251, 7, 217, 1) 90%,
        rgba(255, 0, 0, 1) 100%
    );">→here←</span>](http://ec2-3-71-109-60.eu-central-1.compute.amazonaws.com/)**.

### Notes

- Python <ins>3.8</ins> was used in development environment, as well as in Docker image;
- The code is deployed via Github Actions and Amazon ECS;
- There are three files with dependencies declaration: [Pipfile](Pipfile), [Pipfile.lock](Pipfile.lock) and [requirements.txt](requirements.txt). I use the first two in development environment on my machine with pipenv and the third one for docker image (turns out pipenv isn`t really meant to be used inside Docker, so it is just more convenient to use requirements.txt in Dockerfile);
- Sample data to try it out is included in the repo [here](static/samples) and can be accessed from the frontend as well;

### Demonstration

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
