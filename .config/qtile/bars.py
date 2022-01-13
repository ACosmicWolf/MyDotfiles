from qtile_extras import widget
from libqtile import bar
from qtile_extras.widget.decorations import RectDecoration

from libqtile.widget import base

from libqtile.command import lazy

import os


decor = {
    "decorations": [
        RectDecoration(colour="#2e3440", radius=12, filled=True, padding_y=5)
    ],
    "padding": 10,
}

home = os.path.expanduser('~')

colors = [
	["#2e3440", "#2e3440"],  # 0 background
	["#d8dee9", "#d8dee9"],  # 1 foreground
	["#3b4252", "#3b4252"],  # 2 background lighter
	["#bf616a", "#bf616a"],  # 3 red
	["#a3be8c", "#a3be8c"],  # 4 green
	["#ebcb8b", "#ebcb8b"],  # 5 yellow
	["#81a1c1", "#81a1c1"],  # 6 blue
	["#b48ead", "#b48ead"],  # 7 magenta
	["#88c0d0", "#88c0d0"],  # 8 cyan
	["#e5e9f0", "#e5e9f0"],  # 9 white
	["#4c566a", "#4c566a"],  # 10 grey
	["#d08770", "#d08770"],  # 11 orange
	["#8fbcbb", "#8fbcbb"],  # 12 super cyan
	["#5e81ac", "#5e81ac"],  # 13 super blue
	["#242831", "#242831"],  # 14 super dark background
]

widget_defaults = dict(
	font="FiraCode Nerd Font", fontsize=18, background=colors[14]
)


class DotWidget(base._TextBox):
    def __init__(self, **config):
        super().__init__("", **config)
        self.text=""
        self.foreground="#4c566a"
        self.background="#242831"



main_bar = bar.Bar([
    widget.Spacer(length=4,background=colors[14]),
    widget.TextBox(
        **decor,
        text='',
        fontsize=14,
        foreground=colors[5],
        background=colors[14]
    ),
    widget.Spacer(length=2,background=colors[14]),
    DotWidget(),
    widget.Spacer(length=2,background=colors[14]),
    widget.GroupBox(
        **decor,
        borderwidth= 4,
	    active= colors[9],
	    inactive= colors[2],
	    disable_drag= True,
	    highlight_method= "text",
        highlight_color=colors[13],
	    foreground= colors[1],
	    background= colors[14],
    ),
    DotWidget(),
    widget.CurrentLayout(
        **decor,
        background=colors[14],
    ),
    DotWidget(),
    widget.CPU(
        background=colors[14],
        format="  {load_percent}%",
        fontsize=14,
        foreground=colors[5]
    ),
    DotWidget(),
    widget.Memory(
        background=colors[14],
        format=" {MemUsed: .0f} MB",
        fontsize=14,
        foreground=colors[8]
    ),
    DotWidget(),
    widget.Spacer(background=colors[14]),
    widget.Clock(**decor,
        format=" %I:%M %p",
        foreground=colors[8],
        font='FiraCode Nerd Font',
        background=colors[14]
    ),
    widget.Spacer(background=colors[14]),
   # widget.PulseVolume(
   #     **decor,
   #     foreground=colors[13],
   #     background=colors[14],
   #     fmt="墳  {}",
   #     mouse_callbacks={'Button3': lazy.spawn("pavucontrol")}
   # ),
    widget.ALSAWidget(
        mode="both",
        theme_path="/usr/share/icons/Paper/24x24/panel",
        background=colors[14],
    ),
    DotWidget(),
    widget.Backlight(
        **decor,
        foreground=colors[8],
        background=colors[14],
        brightness_file="/sys/class/backlight/intel_backlight/brightness",
        max_brightness_file="/sys/class/backlight/intel_backlight/max_brightness",
        format="  {percent:2.0%}"
    ),
    DotWidget(),
    widget.Wlan(
            **decor,
        interface="wlp0s20f0u6",
        format=" {essid}",
        foreground=colors[7],
        background=colors[14],
        font="FiraCode Nerd Font",
        mouse_callbacks={'Button1': lazy.spawn("networkmanager_dmenu")}
    ),
    widget.Spacer(length=4,background=colors[14]),
    DotWidget(),
    widget.Spacer(length=4,background=colors[14]),
    widget.Systray(
        background=colors[14],
    ),
    widget.Spacer(length=4,background=colors[14]),
    DotWidget(),
    widget.Spacer(length=4,background=colors[14]),
    widget.TextBox(
        **decor,
        text="",
        background=colors[14],
        font="FiraCode Nerd Font",
        foreground=colors[3],
        mouse_callbacks={'Button1': lazy.spawn(home+"/.config/rofi/powermenu.sh")}
    ),
    widget.Spacer(length=4,background=colors[14])
    ], 35)









