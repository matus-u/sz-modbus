FROM ubuntu:18.04

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
    python3-pyqt5 \
    pyqt5-dev-tools \
    qtcreator \
    qt5-default \
    python3-pyqt5.qtwebsockets \
    net-tools \
    qtvirtualkeyboard-plugin \
    python3-pyqt5.qtquick \
    qml-module-qtquick-virtualkeyboard \
    qtdeclarative5-dev \
    qml-module-qtquick-controls2 \
    libqt53dquick5 \
    qml-module-qtquick-dialogs \
    qml-module-qt-labs-settings \
    qml-module-qt-labs-folderlistmodel

RUN apt-get update \
    && apt-get install -y \
    python3-setuptools

RUN apt-get update \
    && apt-get install -y \
    qt5-style-plugins \
    locales

RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

RUN pip3 install umodbus

