import os

from libqtile.config import Key
from libqtile.command import lazy
from libqtile.widget import backlight

from groups import groups


home = os.path.expanduser("~")                      # Home Folder
mod = "mod4"                                        # Sets mod key to SUPER KEY
myTerm = "alacritty"                                # Terminal
myBrowser = "firefox"                               # Browser
fileManager = "nautilus"                            # File Manager
launcher = home + "/.config/rofi/launcher.sh"       # Launcher Script
powerMenu = home + "/.config/rofi/powermenu.sh"     # Power Menu Script


keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod, "shift"], "Return",
             lazy.spawn(launcher),
             desc='Run Launcher'
             ),
         Key([mod], "b",
             lazy.spawn(myBrowser),
             desc='Opens Browser'
             ),
         Key([mod], "e",
             lazy.spawn(fileManager),
             desc='Opens File Manager'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
        Key([], "XF86AudioRaiseVolume",
            lazy.spawn("amixer -c 0 -q set Master 2dB+")
            ),
        Key([], "XF86AudioLowerVolume",
            lazy.spawn("amixer -c 0 -q set Master 2dB-")
            ),
        Key([], "XF86AudioMute",
            lazy.spawn("amixer -c 0 -q set Master toggle")
            ),
        Key([],"Print",
            lazy.spawn("flameshot gui"),
            desc='Open Screenshot Utility'
            ),
        Key(
            [],
            "XF86MonBrightnessUp",
            lazy.widget['backlight'].change_backlight(backlight.ChangeDirection.UP)
        ),
        Key(
            [],
            "XF86MonBrightnessDown",
            lazy.widget['backlight'].change_backlight(backlight.ChangeDirection.DOWN)
        ),
        Key(
            [mod],
            "l",
            lazy.spawn("bash /home/cosmo/.config/eww/launch_eww")
        ),
]

for i in groups:
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen(toggle=True)))
    keys.append(Key([mod, 'shift'], i.name,
                    lazy.window.togroup(i.name))) 
