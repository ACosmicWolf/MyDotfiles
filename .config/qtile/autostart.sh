#!/usr/bin/env bash

# Wallpaper
nitrogen --restore &

# Dunst
dunst &

# Picom 
picom &

# Polkit Agent
/usr/lib/xfce-polkit/xfce-polkit &

# Cool Volume Bar
python ~/.local/bin/pulse-volume-watcher.py | xob &

