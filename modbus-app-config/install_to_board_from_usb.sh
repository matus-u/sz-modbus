#!/bin/bash

#TODO INSTALL STEPS

apt-get install \
    python3 \
    python3-pip \
    bc \
    python3-serial \
    python3-pyqt5  \
    pyqt5-dev-tools \
    qtvirtualkeyboard-plugin \
    qml-module-qtquick-virtualkeyboard \
    qml-module-qt-labs-folderlistmodel \
    qml-module-qtquick2 \
    qml-module-qtquick-layouts \
    qml-module-qtquick-window2 \
    qtdeclarative5-dev \
    qml-module-qtquick-controls2 \
    libqt53dquick5 \
    qml-module-qtquick-dialogs \
    qml-module-qt-labs-settings \
    qtvirtualkeyboard-plugin \
    qml-module-qtquick-virtualkeyboard \
    qml-module-qt-labs-folderlistmodel \
    bash \
    python3-pyqt5.qtwebsockets \
    python3-setuptools \
    net-tools

pip3 install --upgrade OPi.GPIO
pip3 install umodbus

cp start_usbstick.sh /opt/start_usbstick.sh
cp usb_start.desktop $(find /home -maxdepth 1 -mindepth 1 -type d  | tail -1)/.config/autostart/

cp time-configs/rtc-clock /etc/init.d/
cp time-configs/set-time-to-rtc.sh /opt/set-time-to-rtc.sh
cp time-configs/set-system-time-from-rtc.sh /opt/set-system-time-from-rtc.sh
cp time-configs/rtc-manipulate.py /opt/rtc-manipulate.py

pushd /etc/rc5.d/
ln -sf ../init.d/rtc-clock S02rtc-clock
popd

pushd /etc/rc6.d/
ln -sf ../init.d/rtc-clock K00rtc-clock
popd

#COMMENT LINE:
#modapp ALL=(ALL) NOPASSWD: /usr/bin/psd-overlay-helper
#ADD LINE:
#modapp ALL=(ALL) NOPASSWD: ALL


