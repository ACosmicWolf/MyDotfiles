from libqtile.widget import base

import alsaaudio

import math

import os





class VolumeWidget(base._TextBox):

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("device", "default", "Device Name"),
        ("update_interval", 0.2, "Update time in seconds."),
    ]

    def __init__(self, **config):
        base._TextBox.__init__(self, '0', width=bar.CALCULATED, **config)
        self.add_defaults(VolumeWidget.defaults)

        self.background = "#242831"
        self.fontsize = 18

        self.volume = self.getvolume()

        self.add_callbacks({
            'Button1': self.cmd_mute,
           # 'Button3': self.cmd_run_app,
            'Button4': self.cmd_increase_vol,
            'Button5': self.cmd_decrease_vol,
        })

    def timer_setup(self):
        self.timeout_add(self.update_interval, self.update)

    def update(self):
        vol = self.getvolume()
        if vol != self.volume:
            self.volume = vol
            # Update the underlying canvas size before actually attempting
            # to figure out how big it is and draw it.
            self._update_drawer()
            self.bar.draw()
        self.timeout_add(self.update_interval, self.update)


    def _update_drawer(self):
        if self.volume <= 0:
            self.text = "婢 Mute"
            self.foreground = "#4c566a"
        elif self.volume > 0 and self.volume < 30:
            self.text = "奄 " 
            self.foreground = "#e5e9f0"
        elif self.volume >= 30 and self.volume < 80:
            self.foreground = "#e5e9f0" 
            self.text = "奔 " 
        elif self.volume >= 80:
            self.text = "墳 " 
            self.foreground = "#e5e9f0" 

    def button_press(self, x, y, button):
        base._TextBox.button_press(self, x, y, button)
        self.draw()
   
    def getvolume(self):
        volume = int(alsaaudio.Mixer().getvolume()[0])
        return volume

    def draw(self):
        base._TextBox.draw(self)

    def cmd_mute(self):
        alsaaudio.Mixer().setvolume(0)

    def cmd_increase_vol(self):
        alsaaudio.Mixer().setvolume(self.getvolume()+5)

    def cmd_decrease_vol(self):
        if self.getvolume() >=5:
            alsaaudio.Mixer().setvolume(self.getvolume()-5)
        else:
            alsaaudio.Mixer().setvolume(0)