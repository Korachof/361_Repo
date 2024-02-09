import tkinter as tk
from tkinter import *
import sys


class WindowScreen(tk.Tk):
  """Class to create the window and control the frames"""
    def __init__(self):
        super().__init__()
        
        self.title("MTG Staple Compiler")
        self.geometry("1280x720")
        
        Grid.rowconfigure(self,0,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        self.frame_hash = {0: StartPage, 1: ColorSelectPage, 2: ResultsPage}
        self.current_window = 0
        self.button_command = self.frame_hash[self.current_window]
        self.frame = self.create_frame(self.current_window)
        

    def create_frame(self, buttonNum):
      """A function to control the different frames/pages on the window"""
        for widgets in self.button_command.winfo_children(self):
            widgets.destroy()
        self.current_window = buttonNum
        self.button_command = self.frame_hash[buttonNum]
        self.button_command.tkraise(self)
        
        self.frame = self.button_command(self.frame_hash, self)
        
        self.frame.grid(row=0, column=0)
