# PyQt Spotlight App

A simple spotlight effect application that darkens the screen except for a circular area around the mouse pointer or a smartphone (via KDEConnect/GSConnect), inspired by https://github.com/jahnf/Projecteur. The spotlight follows the mouse movement and automatically hides after a period of inactivity.

## Installation

Create and activate the Conda environment:
```bash
conda env create -f environment.yml
conda activate spotlight_app
```


## Running

```bash
python spotlight_app.py
```
Usage:
- `--spotlight_radius SPOTLIGHT_RADIUS` Spotlight radius
- `--timeout TIMEOUT` Timeout (ms) for spotlight to vanish after pointer stops moving
- Move mouse to show/move spotlight
- Spotlight automatically hides after mouse stops moving
- Press `ESC` to exit

The app will automatically fall back to X11/xcb if Wayland is not available.
