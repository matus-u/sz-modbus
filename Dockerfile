FROM debian:buster

RUN apt-get update \
    && apt-get install -y \
      python3 \
      python3-pip \
      vim \
      bc \
      bash

WORKDIR /src

ENV RUN_FROM_DOCKER TRUE

RUN apt-get update \
    && apt-get install -y \
    qt5-default \
    qtcreator \
    pyside2-tools \
    python3-pyside2.qtwebsockets \
    python3-pyside2.qtcore \
    python3-pyside2.qtwidgets \
    python3-pyside2.qtgui \
    qtvirtualkeyboard-plugin \
    qml-module-qtquick-virtualkeyboard \
    qml-module-qt-labs-folderlistmodel \
    net-tools

RUN pip3 install umodbus

RUN apt-get update \
    && apt-get install -y \
    python3-pyside2.qtqml \
    python3-pyside2.qtnetwork \
    python3-pyside2.qtquick \
    python3-pyside2.qtquickwidgets \
    qtdeclarative5-dev \
    qml-module-qtquick-controls2 \
    python-pyside2.qtquick libqt53dquick5 \
    qml-module-qtquick-dialogs \
    qml-module-qt-labs-settings

