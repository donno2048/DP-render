# DP render

Render the double pendulum for every pendulum

Each point represents a pendulum

The _x_ coordinates are from -π to π and represent the first angle

The _y_ coordinates are from -π to π and represent the second angle

## Install dependencies

`pip3 install -r requirements.txt`

## Run

`python3 main.py <frames>`

Where _\<frame\>_ is the number of frames to render (60 fps)

The output will be saved to _output.gif_ and the frames to the _frames_ folder

`python3 main.py 300` Took me a whole hour to render and here it is:

![output](./output.gif)
