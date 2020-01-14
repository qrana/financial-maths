TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    stockdynamics.cpp \
    plot.cpp

HEADERS += \
    stockdynamics.hh \
    plot.hh
