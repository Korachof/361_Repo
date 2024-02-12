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

class StartPage(tk.Frame):
  """Class to create the frame for the start/home page"""
    def __init__(self, frameHash, mainWindow):
        super().__init__()
        self.frameHash = frameHash
        self.mainWindow = mainWindow
        self.label = tk.Label(self, text="Main Page")
        
        # Configure the row and 5 columns for the buttons. 
        Grid.rowconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)
        Grid.rowconfigure(self,5,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)
        Grid.columnconfigure(self,3,weight=1)
        Grid.columnconfigure(self,4,weight=1)

      
        # create the button images 
        self.start_button = PhotoImage(file="button_images/start_button.png")   

        # create text labels 
        self.welcome_label = tk.Label(self, text="Welcome to the MTG Staple Compiler")
        self.choose_label = tk.Label(self, text="Please choose from the options below")

        # set the start button with the start button image
        self.start = tk.Button(self,
                    image=self.start_button)

        # set the window frame to the start page frame
        self.options_frame = tk.Frame(self)

        # set the frame on the grid
        self.options_frame.grid(row=3, column=2, padx=1, pady=1)

        # Create buttons with the different options for the user
        self.color_choice = tk.Button(self.options_frame, 
                                      text="Find Deck Staples", 
                                      bg="#2f9fd6",
                                      fg="white", 
                                      activebackground="#146d99", 
                                      activeforeground="white", 
                                      font="Garamond",
                                      command=lambda: self.mainWindow.create_frame(1))
        
        self.lands_algorithm = tk.Button(self.options_frame, 
                                     text="Calculate How Many Lands Your Deck Needs", 
                                     bg="#2f9fd6", 
                                     fg="white", 
                                     activebackground="#146d99", 
                                     activeforeground="white", 
                                     font="Garamond",
                                     command=lambda: self.mainWindow.create_frame(2))
        
        self.exit_button = tk.Button(self.options_frame,
                                     text="Exit",
                                     bg="#2f9fd6",
                                     fg="white", 
                                     activebackground="#146d99", 
                                     activeforeground="white",
                                     font="Garamond", 
                                     command=sys.exit)

        #  set the buttons and labels on the grid 
        self.welcome_label.grid(row=0, column=2, padx=1, pady=1)
        self.choose_label.grid(row=1, column=2, padx=1, pady=1)
        self.start.grid(row=2, column=2, padx=1, pady=1)
        self.color_choice.grid(row=0, column=0, padx=1, pady=2, sticky="WES")
        self.lands_algorithm.grid(row=1, column=0, padx=1, pady=2, sticky="WEN")
        self.exit_button.grid(row=2, column=0, padx=1, pady=2, sticky="WEN")


class ResultsPage(tk.Frame):
    def __init__(self, frameHash, mainWindow):
        super().__init__()
        self.frameHash = frameHash
        self.mainWindow = mainWindow
        self.label = tk.Label(self, text="Color Select Page")
        # create the button images 
        self.start_button = PhotoImage(file="button_images/start_button.png")

        # Configure the row and 5 columns for the buttons. 
        # Configure the row and 5 columns for the buttons. 
        Grid.rowconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)
        Grid.rowconfigure(self,5,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)
        Grid.columnconfigure(self,3,weight=1)
        Grid.columnconfigure(self,4,weight=1)

        self.select_color_label = tk.Label(self, text="Please follow these instructions")
        self.test_grid_label = tk.Label(self, text="testing testing testing instruction dialogue label")
        self.text_input_cmc = Text(self,
                                   activebackground="#146d99", 
                                   activeforeground="white",
                                   height=2,
                                   width=2
                                   font="Garamond")
        self.text_input_symbols = Text(self,
                                   activebackground="#146d99", 
                                   activeforeground="white",
                                   height=2,
                                   width=2
                                   font="Garamond")
                                   
        self.exit_button = tk.Button(self,
                                     text="Exit",
                                     bg="#2f9fd6",
                                     fg="white", 
                                     activebackground="#146d99", 
                                     activeforeground="white",
                                     font="Garamond", 
                                     command=sys.exit)

        self.test_grid_label.grid(row=1, column=1)
        self.select_color_label.grid(row=2, column=2, padx=1, pady=1)
        self.exit_button.grid(row=5, column=2)
        


