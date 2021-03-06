![N. Logo](logo_100x100_20padding_white.png)

A simple python script to generate my personal logo. Width, height, padding and background color are configurable.

## Install

- `brew install pipenv` - install python package/virtual environment manager

## Usage

```
  pipenv run python main.py [-h] [-p [PADDING]] [-b [{black,white}]] [-v] width height
```

e.g.

```
  pipenv run python main.py -p 100 -b white -v 600 400
```

Arguments:

- `width` (required) Width of output file in pixels
- `height` (required) Height of output file in pixels
- `--padding` `-p` (optional) Padding on all sides in pixels, defaults to 0
- `--bgcolor` `-b` (optional) Background color for logo, defaults to black
- `--preview` `-v` (optional) Preview logo instead of saving to file

Output:

`logo.png`
