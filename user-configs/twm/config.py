from libqtile.manager import Key, Screen, Group
from libqtile.command import lazy
from libqtile import layout, bar, widget

# Cleaner key aliases
alt = "mod1"
super = "mod4"
shift = "shift"
control = "control"

groups = [
    Group("q"),
    Group("w"),
    Group("e"),
    Group("r"),
    Group("t"),
    Group("y"),
    Group("u"),
    Group("i"),
    Group("o"),
    Group("p"),
]

RUN = "dmenu_run"
TERMINAL = "gnome-terminal"
SUSPEND = "dbus-send --system --print-reply --dest=org.freedesktop.UPower /org/freedesktop/UPower org.freedesktop.UPower.Suspend"

keys = [
    Key([super],          g.name,   lazy.group[g.name].toscreen()) for g in groups
] + [
    Key([super, shift],   g.name,   lazy.window.togroup(g.name)) for g in groups
] + [
    Key([super],          "k",      lazy.layout.down()),
    Key([super],          "j",      lazy.layout.up()),
    Key([super, control], "k",      lazy.layout.shuffle_down()),
    Key([super, control], "j",      lazy.layout.shuffle_up()),
    Key([alt],            "Tab",    lazy.layout.next()),
    Key([super, shift],   "space",  lazy.layout.rotate()),
    Key([super, shift],   "Return", lazy.layout.toggle_split()),
    Key([super],          "h",      lazy.to_screen(1)),
    Key([super],          "l",      lazy.to_screen(0)),
    Key([],               "F1",     lazy.spawn(TERMINAL)),
    Key([alt],            "F2",     lazy.spawn(RUN)),
    Key([super],          "Tab",    lazy.nextlayout()),
    Key([super, shift],   "c",      lazy.window.kill()),
    Key([super],          "Escape", lazy.spawn(SUSPEND)),
]

layouts = [
    layout.Max(),
    layout.Stack(stacks=2),
    layout.Tile(ratio=0.25),
]

screens = [
    Screen(
        top=bar.Bar([
            widget.GroupBox(),
            widget.WindowName(),
            widget.Clock('%Y-%m-%d %H:%M'),
            widget.Systray(),
            widget.CPUGraph(width=200, graph_color='22FF44', fill_color='11AA11'),
            widget.MemoryGraph(width=200, graph_color='22FF44', fill_color='11AA11'),
        ], 24),
    ),
]
