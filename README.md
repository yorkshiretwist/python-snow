# Python snow

Simple python script which simulates snow falling.

My son made a valiant effort to make a snow falling effect in python for a school project, but it didn't quite work. I had a go, maybe it's better.

## Make it snow

To run it execute: `python snow.py`

## Options

You can add parameters to the call to the `generate_snow()` function to change how the snow falls:

`lines` (int): how many lines of snow (ahem) to draw. Default: 15.

`width` (int): how many characters wide the snow is. Default: 70.

`max_density` (int): the maximum number of snowflakes on each line. Default: 5.

`delay` (float): the gap in seconds between drawing each line. Default: 0.1.

For example, to simulate lots of snow falling slowly you can do this:

`generate_snow(max_density=15, delay=0.3)`

## Just for fun

You can also pass in a `char` parameter which changes the character of the snowflake. Try using an emoji, like this:

`generate_snow(char="💩")`