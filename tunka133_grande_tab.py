#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 03:37:15 2021

@author: yaroslav
"""

import tkinter as tk

class Tunka133_grande_tab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.button = tk.Button(self, text='Append', command=self.on_click)
        self.button.pack()

        self.pack()

    def on_click(self):
        print('Hello World!')