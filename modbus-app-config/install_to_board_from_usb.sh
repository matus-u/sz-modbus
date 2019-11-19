#!/bin/bash

#TODO INSTALL STEPS

apt-get install \
    python3 \
    python3-pip \
    bc \
    python3-serial \ 
    python3-pyside2.qtqml \
    python3-pyside2.qtnetwork \
    python3-pyside2.qtquick \
    python3-pyside2.qtquickwidgets \
    qtdeclarative5-dev \
    qml-module-qtquick-controls2 \
    python-pyside2.qtquick libqt53dquick5 \
    qml-module-qtquick-dialogs \
    qml-module-qt-labs-settings
    pyside2-tools \
    python3-pyside2.qtwebsockets \
    python3-pyside2.qtcore \
    python3-pyside2.qtwidgets \
    python3-pyside2.qtgui \
    qtvirtualkeyboard-plugin \
    qml-module-qtquick-virtualkeyboard \
    qml-module-qt-labs-folderlistmodel \
    bash \
    python3-setup-tools \
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


