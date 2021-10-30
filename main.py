#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 03:20:10 2021

@author: yaroslav
"""

from tkinter import Tk, ttk
import tkinter as tk
#from fpdf import FPDF
from PIL import Image,ImageTk
#from pdf2image import convert_from_path
from reportlab.pdfgen.canvas import Canvas
#import subprocess
#from wand.image import Image
#from pdf2jpg import pdf2jpg
#import GhostScript
from tkPDFViewer import tkPDFViewer as pdf

from iact_tab import IACT_tab
from hiscore_tab import HiScore_tab
from grande_tab import Grande_tab
from weather_date_tab import Weather_Date_tab
from taiga_muon_tab import Taiga_muon_tab
from tunka133_grande_tab import Tunka133_grande_tab

REPORT_EMAIL = "yaroslav_sagan@mail.ru"

class ReportWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.parent.title('Report Page')

        self.init_ui()

    def init_ui(self):
        self.parent['padx'] = 10
        self.parent['pady'] = 10

        self.notebook = ttk.Notebook(self, width=1100, height=1000)

        weather_tab = Weather_Date_tab(self.notebook)
        iact_tab = IACT_tab(self.notebook)
        hiscore_tab = HiScore_tab(self.notebook)
        grande_tab = Grande_tab(self.notebook)
        taiga_muon_tab = Taiga_muon_tab(self.notebook)
        tunka133_grande_tab = Tunka133_grande_tab(self.notebook)

        self.notebook.add(weather_tab, text="Weather & Date")
        self.notebook.add(iact_tab, text="IACTs")
        self.notebook.add(hiscore_tab, text="HiScore")
        self.notebook.add(grande_tab, text="Grande")
        self.notebook.add(taiga_muon_tab, text="TAIGA-Muon")
        self.notebook.add(tunka133_grande_tab, text="Tunka133 + Grande")

        self.notebook.pack(side=tk.LEFT)
        self.pack(side=tk.LEFT, fill=tk.BOTH)

class PrewievWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.parent.title('Prewiev Page')

        self.init_ui()
        
    def init_ui(self):
        self.parent['padx'] = 10
        self.parent['pady'] = 10

        self.send_frame = ttk.Frame(self)
        self.send_frame.pack(fill=tk.BOTH)

        self.preview_frame = tk.Frame(self.send_frame, relief=tk.GROOVE, borderwidth=1)
        self.preview_frame.pack(side=tk.TOP, fill=tk.BOTH)
        
        self.send_send_frame = tk.Frame(self.send_frame, relief=tk.GROOVE, borderwidth=1)
        self.send_send_frame.pack(side=tk.TOP, fill=tk.BOTH)
        
        self.update_button = tk.Button(self.send_send_frame, text="Update report")
        self.update_button.pack(side=tk.LEFT, fill=tk.X, expand=1, ipadx=4, padx=4)
        self.send_button = tk.Button(self.send_send_frame, text="Send report")
        self.send_button.pack(side=tk.LEFT, fill=tk.X, expand=1, ipadx=4, padx=4)
        self.email_entry = tk.Entry(self.send_send_frame)
        self.email_entry.insert(tk.END, REPORT_EMAIL)
        self.email_entry.configure(state=tk.DISABLED)
        self.email_entry.pack(side=tk.LEFT, fill=tk.X, expand=1, ipadx=4, padx=4)
        self.email_entry.bind("<Return>", self.change_email)
        self.change_email_button = tk.Button(self.send_send_frame, text="Change e-mail", command=self.enable_new_email)
        self.change_email_button.pack(side=tk.LEFT, fill=tk.X, expand=1, ipadx=4, padx=4)

        self.canvas = Canvas("Report - Name [Date].pdf")
        self.canvas.setFont("Helvetica-Bold", 10)
        for i in range(0, 1000, 5):
            self.canvas.drawString(0, i, "x")
        for j in range(0, 1000, 5):
            self.canvas.drawString(j, 0, "x")
#        self.canvas.drawString(72, 795.68, "Veterinary Office")
        
#        self.canvas.setFont("Helvetica", 24)
#        self.canvas.drawString(20, 400, "Hello")
#        self.canvas.drawString(40, 360, "World")
        
#        self.canvas.setFont("Courier", 16)
#        self.canvas.drawString(60, 300, "How are you?")
        
        
        self.canvas.showPage()
        self.canvas.save()        
        self.report_field = pdf.ShowPdf()
        self.report = self.report_field.pdf_view(self.preview_frame, pdf_location = r"Report - Name [Date].pdf", width=110, height=85)  
        self.report.pack(side=tk.TOP, fill=tk.BOTH)
        

        self.pack(side=tk.LEFT, fill=tk.BOTH)


    def enable_new_email(self):
        if self.email_entry['state'] == tk.DISABLED:
            self.email_entry.configure(state=tk.NORMAL)
            self.email_entry.update()
        elif self.email_entry['state'] == tk.NORMAL:
            self.email_entry.configure(state=tk.DISABLED)
            self.email_entry.update()
    def change_email(self, event):
        global REPORT_EMAIL
        REPORT_EMAIL = self.email_entry.get()
        self.email_entry.configure(state=tk.DISABLED)
        self.email_entry.update()

 

if __name__ == '__main__':
    root = Tk()
    root.title('TAIGA shift reporter')
    ex = ReportWindow(root)
    ex = PrewievWindow(root)
    root.geometry("1900x1000")
    root.mainloop()