#!/bin/sh
# Configure gnome-session to use Qtile as window manager.

mkdir -pv ~/.config/qtile
ln -sv "$PWD/config.py" ~/.config/qtile

mkdir -pv ~/.local/share/applications
ln -sv "$PWD/qtile.desktop" ~/.local/share/applications
ln -sv "$PWD/notify-osd.desktop" ~/.local/share/applications

mkdir -pv ~/.config/gnome-session/sessions
ln -sv "$PWD/qtile.session" ~/.config/gnome-session/sessions

# Set it as the default session.  Set it to "default" to revert this.
gsettings set org.gnome.desktop.session session-name qtile
