#!/bin/sh

echo "Detecting distribution..."
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo "Cannot detect OS. Exiting."
    exit 1
fi

echo "Updating system and installing Python3 and pip on $DISTRO..."

case "$DISTRO" in
    ubuntu|debian|kali|linuxmint|pop)
        sudo apt update && sudo apt upgrade -y
        sudo apt install -y python3 python3-pip
        ;;

    arch|manjaro)
        sudo pacman -Syu --noconfirm
        sudo pacman -S --noconfirm python python-pip
        ;;

    fedora)
        sudo dnf upgrade -y
        sudo dnf install -y python3 python3-pip
        ;;

    alpine)
        sudo apk update
        sudo apk add python3 py3-pip
        ;;

    opensuse*|suse)
        sudo zypper refresh
        sudo zypper update -y
        sudo zypper install -y python3-pip
        ;;

    gentoo)
        sudo emerge --sync
        sudo emerge -uDN @world
        sudo emerge dev-lang/python
        sudo emerge dev-python/pip
        ;;

    void)
        sudo xbps-install -Syu
        sudo xbps-install -y python3 python3-pip
        ;;

    *)
        echo "Unsupported or unknown distribution: $DISTRO"
        exit 1
        ;;
esac

echo "Installation complete!"
python3 --version
pip3 --version
