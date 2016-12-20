#!/usr/bin/pyhton3
#-*- coding: utf-8 -*-

"""
This is a prototype of agent window system.
This has three parts.
1. agent's status window
2. message log window
3. input form

"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QInputDialog, QApplication)

class proto1:

    def __init__(self):
        super().__init__()

        self.initUI()

    # format
    def initUI(self):

