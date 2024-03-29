import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Screen , Match, ScratchPad, DropDown, Key 
from libqtile.command import lazy
from libqtile import layout, hook, extension 
from typing import List  

from keys import keys
#from mouse import mouse
from groups import groups

from bars import main_bar

term = "alacritty"


# Default layout theme
layout_theme = {
	"border_width": 3,
	"margin": 9,
	"border_focus": "3b4252",
	"border_normal": "3b4252",
	"font": "FiraCode Nerd Font",
	"grow_amount": 2,
}


# Layouts pretty obvious
layouts = [
    layout.Floating(**layout_theme,fullscreen_border_width=3, max_border_width=3),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Zoomy(**layout_theme)
]

groups.extend([
    ScratchPad("scratchpad", [
        DropDown("pulsemixer", term + " -e pulsemixer", opacity=1, y=0.15, height=0.75),
        DropDown("term", term, opacity=1),
        DropDown("music", term + " -e ncmpcpp", opacity=1, y=0.15, height=0.75),
        DropDown("spotify", " spotify", opacity=1, y=0.15, height=0.75),
    ]),
])

keys.extend([
    Key([], 'F1', lazy.group['scratchpad'].dropdown_toggle('music')),
    Key(["mod1"], 'F1', lazy.group['scratchpad'].dropdown_toggle('spotify')),
    Key([], 'F11', lazy.group['scratchpad'].dropdown_toggle('pulsemixer')),
    Key([], 'F12', lazy.group['scratchpad'].dropdown_toggle('term')),
])

screens = [Screen(top=main_bar)]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
    Match(wm_class='Unity'),          # Unity
    Match(wm_class='unityhub'),       # UnityHub
], **layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
wmname = "LG3D"


home = os.path.expanduser("~")

# Autostart Script
@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/autostart.sh'])

