#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 03:20:10 2021

@author: yaroslav
"""

import tkinter as tk    
from tkinter import ttk
from tkinter import messagebox

class IACT_run:
    
    list_of_runs = []
    
    def __init__(self, iact_number="", run_number="", status="", target="", start_time="", stop_time="", av_count_rate="", comments="", problems=""):
        
        self.iact_number = iact_number
        self.run_number = run_number
        self.status = status
        self.target = target
        self.start_time = start_time
        self.stop_time = stop_time
        self.av_count_rate = av_count_rate
        self.comments = comments
        self.problems = problems
        self.list_of_runs.append (self)
        
    def show_item (self):
        print("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}".format(
                "iact_number:", self.iact_number, # 1
                "run_number:", self.run_number, # 2
                "status:", self.status,
                "target:", self.target, # 3
                "start_time:", self.start_time, # 4
                "stop_time:", self.stop_time, # 5
                "av_count_rate:", self.av_count_rate, # 6
                "comments:", self.comments, # 7
                "problems:", self.problems, # 8
                ))


class IACT_tab(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        
        self.pack(fill=tk.BOTH, expand=1)
        
########################################################################################################
########################################################################################################     

        self.top_frame = tk.Frame(self, relief=tk.GROOVE, borderwidth=1)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
########################################################################################################
########################################################################################################  
        self.entry_windows_frame = tk.Frame(self.top_frame, relief=tk.GROOVE, borderwidth=1)
        self.entry_windows_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
########################################################################################################        
        self.iact_number_text_label = ttk.Label(self.entry_windows_frame, text="Choose IACT")
        self.iact_number_text_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.iact_number_combobox = ttk.Combobox(self.entry_windows_frame, values=["IACT_01", "IACT_02"])
        self.iact_number_combobox.pack(side=tk.TOP, ipadx=4, padx=4)
        self.status_text_label = ttk.Label(self.entry_windows_frame, text="Enter IACT Status")
        self.status_text_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.status_entry = ttk.Entry(self.entry_windows_frame)
        self.status_entry.pack(side=tk.TOP, ipadx=4, padx=4)
        self.run_number_text_label = ttk.Label(self.entry_windows_frame, text="Enter RUN number")
        self.run_number_text_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.run_number_entry = ttk.Entry(self.entry_windows_frame)
        self.run_number_entry.pack(side=tk.TOP, ipadx=4, padx=4)
        self.target_text_label = ttk.Label(self.entry_windows_frame, text="Enter target name")
        self.target_text_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.target_entry = ttk.Entry(self.entry_windows_frame)
        self.target_entry.pack(side=tk.TOP, ipadx=4, padx=4)
        self.start_time_text_label = ttk.Label(self.entry_windows_frame, text="Enter start time")
        self.start_time_text_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.start_time_entry = ttk.Entry(self.entry_windows_frame)
        self.start_time_entry.pack(side=tk.TOP, ipadx=4, padx=4)
        self.stop_time_text_label = ttk.Label(self.entry_windows_frame, text="Enter stop time")
        self.stop_time_text_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.stop_time_entry = ttk.Entry(self.entry_windows_frame)
        self.stop_time_entry.pack(side=tk.TOP, ipadx=4, padx=4)
        self.average_count_rate_text_label = ttk.Label(self.entry_windows_frame, text="Enter average count rate")
        self.average_count_rate_text_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.average_count_rate_entry = ttk.Entry(self.entry_windows_frame)
        self.average_count_rate_entry.pack(side=tk.TOP, ipadx=4, padx=4)
        self.comments_text_label = ttk.Label(self.entry_windows_frame, text="Comments")
        self.comments_text_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.comments_text = tk.Text(self.entry_windows_frame, height=10)
        self.comments_text.pack(side=tk.TOP, ipadx=4, padx=4)       
        self.comments_submit_button = tk.Button(
                self.entry_windows_frame, text="Submit comments", command=lambda:self.SubmitText(
                        self.comments_text, self.comments_label))
        self.comments_submit_button.pack(side=tk.TOP, ipadx=4, padx=4)
        self.problems_text_label = ttk.Label(self.entry_windows_frame, text="Problems")
        self.problems_text_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.problems_text = tk.Text(self.entry_windows_frame, height=10)
        self.problems_text.pack(side=tk.TOP, ipadx=4, padx=4)
        self.problems_submit_button = tk.Button(
                self.entry_windows_frame, text="Submit problems", command=lambda:self.SubmitText(
                        self.problems_text, self.problems_label))
        self.problems_submit_button.pack(side=tk.TOP, ipadx=4, padx=4)

########################################################################################################
########################################################################################################
        
        self.run_info_frame = tk.Frame(self.top_frame, relief=tk.GROOVE, borderwidth=1)
        self.run_info_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
########################################################################################################
        
        self.iact_number_label = tk.Label(self.run_info_frame, text="IACT_01")
        self.iact_number_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.iact_number_combobox.current(0)
        self.iact_number_combobox.bind("<<ComboboxSelected>>", self.on_iact_number_selection)
        self.status_text_1_label = ttk.Label(self.run_info_frame, text="IACT Status:")
        self.status_text_1_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.status_label = tk.Label(self.run_info_frame, text="")
        self.status_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.status_entry.bind("<Return>", lambda event: self.return_Entry(self.status_entry, self.status_label))
        self.run_number_text_1_label = ttk.Label(self.run_info_frame, text="RUN number:")
        self.run_number_text_1_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.run_number_label = tk.Label(self.run_info_frame, text="")
        self.run_number_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.run_number_entry.bind("<Return>", lambda event: self.return_Entry(self.run_number_entry, self.run_number_label))
        self.target_text_1_label = ttk.Label(self.run_info_frame, text="Target:")
        self.target_text_1_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.target_label = tk.Label(self.run_info_frame, text="")
        self.target_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.target_entry.bind("<Return>", lambda event: self.return_Entry(self.target_entry, self.target_label))
        self.start_time_text_1_label = ttk.Label(self.run_info_frame, text="Start time:")
        self.start_time_text_1_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.start_time_label = tk.Label(self.run_info_frame, text="")
        self.start_time_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.start_time_entry.bind("<Return>", lambda event: self.return_Entry(self.start_time_entry, self.start_time_label))
        self.stop_time_text_1_label = ttk.Label(self.run_info_frame, text="Stop time:")
        self.stop_time_text_1_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.stop_time_label = tk.Label(self.run_info_frame, text="")
        self.stop_time_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.stop_time_entry.bind("<Return>", lambda event: self.return_Entry(self.stop_time_entry, self.stop_time_label))
        self.average_count_rate_text_1_label = ttk.Label(self.run_info_frame, text="Average count rate:")
        self.average_count_rate_text_1_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.average_count_rate_label = tk.Label(self.run_info_frame, text="")
        self.average_count_rate_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.average_count_rate_entry.bind("<Return>", lambda event: self.return_Entry(
                self.average_count_rate_entry, self.average_count_rate_label))
        self.comments_text_1_label = ttk.Label(self.run_info_frame, text="Comments:")
        self.comments_text_1_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.comments_label = tk.Label(self.run_info_frame, text="")
        self.comments_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.problems_text_1_label = ttk.Label(self.run_info_frame, text="Problems:")
        self.problems_text_1_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.problems_label = tk.Label(self.run_info_frame, text="")
        self.problems_label.pack(side=tk.TOP, ipadx=4, padx=4)
        self.run_submit_button = tk.Button(self.run_info_frame, text="Submit run", command=lambda:self.init_run_prepare())
        self.run_submit_button.pack(side=tk.BOTTOM, ipadx=4, padx=4)
########################################################################################################    
        

########################################################################################################        
        self.bottom_frame = tk.Frame(self, relief=tk.GROOVE, borderwidth=1)
        self.bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        

        self.subbottom_frame_1 = tk.Frame(self.bottom_frame, relief=tk.GROOVE, borderwidth=1)
        self.subbottom_frame_1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        self.submitted_runs_text_label = tk.Label(self.subbottom_frame_1, text="      Submitted runs")
        self.submitted_runs_text_label.pack(side=tk.TOP, anchor='w', fill=tk.X, ipadx=4, padx=4)        
        self.run_listbox = tk.Listbox(self.subbottom_frame_1, selectmode = "single")
        self.run_listbox.pack(side=tk.TOP, anchor='w', fill=tk.X, ipadx=4, padx=4)
        self.run_listbox.bind('<<ListboxSelect>>', lambda event: self.return_selected_from_listbox(self.run_listbox))
        
        self.subbottom_frame_2 = tk.Frame(self.bottom_frame, relief=tk.GROOVE, borderwidth=1)
        self.subbottom_frame_2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)        
        
        self.iact_number_for_edit_combobox = ttk.Combobox(self.subbottom_frame_2, values=["IACT_01", "IACT_02", "All IACTs"])
        self.iact_number_for_edit_combobox.pack(side=tk.TOP, anchor='w', fill=tk.X, ipadx=4, padx=4)
        self.iact_number_for_edit_combobox.current(2)
        self.iact_number_for_edit_combobox.bind("<<ComboboxSelected>>", self.on_iact_number_selection_for_edit)
        self.run_edit_button = tk.Button(self.subbottom_frame_2, text="Edit selected run", command=lambda:self.edit_run(self.run_listbox))
        self.run_edit_button.pack(side=tk.TOP, anchor='w', fill=tk.X, ipadx=4, padx=4)
        self.run_delete_button = tk.Button(self.subbottom_frame_2, text="Delete selected run", command=lambda:self.delete_run(self.run_listbox))
        self.run_delete_button.pack(side=tk.TOP, anchor='w', fill=tk.X, ipadx=4, padx=4)
        
        self.iact_report_update_button = tk.Button(self.subbottom_frame_2, text="Update IACT report block\n&\nPrewiev")
        self.iact_report_update_button.pack(side=tk.BOTTOM, anchor='w', fill=tk.X, pady=4, ipady=4, ipadx=4, padx=4)
   
        self.pack()

    def on_iact_number_selection(self, *args):
        iact_number_selected = self.iact_number_combobox.get()
        self.iact_number_label['text'] = iact_number_selected
        
    def on_iact_number_selection_for_edit(self, *args):
        iact_number_selected = self.iact_number_for_edit_combobox.get()
        self.run_listbox.delete(0, tk.END)
        if IACT_run.list_of_runs:
            if iact_number_selected != "All IACTs":
                for run_item in IACT_run.list_of_runs:
                    if run_item.iact_number == iact_number_selected:
                        self.run_listbox.insert(
                                tk.END, "{}    {}    {}    {}    {}    {}Hz".format(
                                        run_item.iact_number, run_item.run_number,
                                        run_item.target, run_item.start_time,
                                        run_item.stop_time, run_item.av_count_rate))
            elif iact_number_selected == "All IACTs":
                for run_item in IACT_run.list_of_runs:
                         self.run_listbox.insert(
                                tk.END, "{}    {}    {}    {}    {}    {}Hz".format(
                                        run_item.iact_number, run_item.run_number,
                                        run_item.target, run_item.start_time,
                                        run_item.stop_time, run_item.av_count_rate))
                         
    def return_Entry(self, source, label):
        label['text'] = source.get()

    def SubmitText(self, source, label):
        label['text'] = source.get(1.0, tk.END)
        
    def init_run_prepare(self):

        iact_number = self.iact_number_label['text']
        run_number = self.run_number_label['text']
        target = self.target_label['text']
        start_time = self.start_time_label['text']
        stop_time = self.stop_time_label['text']
        av_count_rate = self.average_count_rate_label['text']
        comments = self.comments_label['text']
        problems = self.problems_label['text']
        
        if ((not iact_number) or (not run_number) or (not target) or (not start_time) or (not stop_time)):
            messagebox.showerror(
                title="Submit error", 
                message="Fill the  Run number / Target / Start time / Stop time  information")           
        elif (not av_count_rate) or (not comments) or (not problems):
            answer = messagebox.askyesno(
                title="Submit error",
                message="You missed  Average count rates / Comments / Problems  fields. It's ok?")
            if answer: self.init_run()
        else: self.init_run()
        
    def init_run(self):
        
        iact_number = self.iact_number_label['text']
        run_number = self.run_number_label['text']
        target = self.target_label['text']
        start_time = self.start_time_label['text']
        stop_time = self.stop_time_label['text']
        av_count_rate = self.average_count_rate_label['text']
        
        IACT_run(
                iact_number = iact_number,
                run_number = run_number,
                target = target,
                status = self.status_label['text'],
                start_time = start_time,
                stop_time = stop_time,
                av_count_rate = av_count_rate,
                comments = self.comments_label['text'],
                problems = self.problems_label['text']
                )
        self.run_listbox.insert(tk.END, "{}    {}    {}    {}    {}    {}Hz".format(iact_number, run_number, target, start_time, stop_time, av_count_rate))
        
    def return_selected_from_listbox(self, listbox):
        selected = listbox.curselection()
        if selected != ():
            iact_number_selected, run_number_selected = listbox.get(selected).split("    ")[:2]
        return iact_number_selected, run_number_selected


    def delete_run(self, listbox):
        
        selected = listbox.curselection()
        if selected != ():
            iact_number_for_delete, run_number_for_delete = listbox.get(selected).split("    ")[:2]

        answer = messagebox.askyesno(
                title="Deletie run!".format(),
                message="Delete run {} for {}".format(iact_number_for_delete, run_number_for_delete))
        if answer:
            for item in IACT_run.list_of_runs:
                if (item.iact_number == iact_number_for_delete) and (item.run_number == run_number_for_delete):
                    del item
        listbox.delete(selected)
        
    def edit_run(self, listbox):
        
        selected = listbox.curselection()
        if selected != ():
            iact_number_for_delete, run_number_for_delete = listbox.get(selected).split("    ")[:2]
            
        answer = messagebox.askyesno(
                title="Edit run!".format(),
                message="All unsaved changes will be lost!\nFirst be sure that you will not lost something important!")
        if answer:
            for item in IACT_run.list_of_runs:
                if (item.iact_number == iact_number_for_delete) and (item.run_number == run_number_for_delete):
                    self.iact_number_label['text'] = item.iact_number
                    self.status_label['text'] = item.status
                    self.run_number_label['text'] = item.run_number
                    self.target_label['text'] = item.target
                    self.start_time_label['text'] = item.start_time
                    self.stop_time_label['text'] = item.stop_time
                    self.average_count_rate_label['text'] = item.av_count_rate
                    self.comments_label['text'] = item.comments
                    self.problems_label['text'] = item.problems







