# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
alt = "mod1"
terminal = "alacritty"
browser = "firefox"

keys = [
   #Switch between windows
   Key([mod], "q",  lazy.layout.down(),   desc='Move focus down in current stack pane'),
   Key([mod], "w", lazy.layout.up(),  desc='Move focus up in current stack pane'),
   Key([alt], "q", lazy.layout.shuffle_down(),  lazy.layout.section_down(),  desc='Move windows down in current stack'),
   Key([alt], "w", lazy.layout.shuffle_up(), lazy.layout.section_up(), desc='Move windows up in current stack'),
   
    #groups/screens managment
    Key([alt], "Tab", lazy.screen.next_group(skip_managed=True), desc="scroll through all groups"),
    Key([mod], "Tab",  lazy.next_screen(),  desc='Move focus to next monitor'),
    Key([alt], "f",  lazy.window.toggle_fullscreen(),   desc='toggle fullscreen'),
    Key([mod], "a", lazy.layout.rotate(), lazy.layout.flip(), desc='Switch which side main pane occupies (XmonadTall)'),
    Key([mod], "s", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "n", lazy.window.toggle_floating(), desc="Reset all window sizes"),

    #spawns
    Key([mod, "control"], 'Return', lazy.spawn('rofi -show run')),
    Key([mod], 'Return', lazy.spawn('rofi -show drun')),
    Key([mod], 'x', lazy.spawn('rofi -show power-menu -modi power-menu:rofi-power-menu')),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "b", lazy.spawn(browser), desc="Spawn a browser"),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "v", lazy.spawn("code"), desc="launch vsscode"),
    Key([mod], "f", lazy.spawn("thunar"), desc="launch Thunar File explorer"),

    #Actions
    Key([mod], "d", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),





 #Key([sup, "shift"], "Tab", lazy.layout.rotate(), lazy.layout.flip(), desc='Switch which side main pane occupies (XmonadTall)'),


]


groups = [Group("1", label="", layout='monadtall'),
          Group("2", label="", layout='monadtall'),
          Group("3", label="", layout='monadtall'),
          Group("4", label="", layout='monadtall'),
          Group("5", label="", layout='monadtall'),
          Group("6", label="", layout='monadtall'),
          Group("7", label="", layout='monadtall')]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([alt], i.name, lazy.group[i.name].toscreen(),  desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        #Key([mod], i.name, lazy.window.togroup(i.name, switch_group=True),  desc="Switch to & move focused window to group {}".format(i.name)),

        # # mod1 + shift + letter of group = move focused window to group
        Key([mod], i.name, lazy.window.togroup(i.name),    desc="move focused window to group {}".format(i.name)),
    ])

layout_theme = {"border_width": 4,
                "margin": 12,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.Max(**layout_theme)    
    #layout.Floating(**layout_theme)
          ]

colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    padding=3,
)
##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 14,
    padding = 2,
    background = colors[2]
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 45,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),                
                widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ), 
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.Systray(
                       background = colors[0],
                       padding = 6,
                       icon_size = 25
                       ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
                widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 4,
                       fontsize = 16
                       ), 
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
                widget.TextBox(
                       text = " Net:",
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       fontsize = 14
                       ),                   
                widget.Net(
                       interface = "enp0s31f6",
                       format = '{down} ↓↑ {up} ',
                       foreground = colors[2],
                       background = colors[0],
                       padding = 2
                       ), 
                widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[0],
                       background = colors[0]
                       ),  
                widget.CPU(
                       format = 'CPU: {load_percent}%',
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0
                       ),
                widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[0],
                       background = colors[0]
                       ),                       
                widget.TextBox(
                       text = "Mem:",
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       fontsize = 14
                       ),
                widget.Memory(
                       foreground = colors[2],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                       padding = 2
                       ),
                widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[0],
                       background = colors[0]
                       ),
                widget.TextBox(
                      text = "Vol: ",
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0
                       ),
                widget.PulseVolume(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0
                       ),
                widget.TextBox(
                       text = "  ⟳",
                       padding = 0,
                       foreground = colors[2],
                       background = colors[0],
                       fontsize = 20
                       ),
                widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch",
                       display_format = "{updates} Updates",
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                       background = colors[0]
                       ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),                               
              widget.Clock(
                       foreground = colors[2],
                       background = colors[0],
                       format = "%A, %B %d - %l:%M "
                       )
            ], 35),
        ),
        #Screen()
    ]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
