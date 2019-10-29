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

