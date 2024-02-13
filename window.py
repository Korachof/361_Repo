import tkinter as tk
from tkinter import *
import deck_build_algo
import sys


class WindowScreen(tk.Tk):
	"""Class to create the window and control the frames"""
	def __init__(self):
		super().__init__()
		
		self.title("MTG Deck Building Companion App")
		self.geometry("1280x720")
		
		Grid.rowconfigure(self,0,weight=1)
		Grid.columnconfigure(self,0,weight=1)
		self.frame_hash = {0: StartPage, 1: LandCountPage, 2: HelpPage}
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
			# self.start_button = PhotoImage(file="button_images/start_button.png")   

			# create text labels 
			self.welcome_label = tk.Label(self,
																		text="Welcome to the MTG Deck Building Companion App",
																		font=("Garamond", 14))
			self.choose_label = tk.Label(self,
																	 text="Please choose from the options below",
																	 font=("Garamond", 14))
			self.blank_space_label = tk.Label(self,
																				text="")

			# set the start button with the start button image
			# self.start = tk.Button(self,
			#            image=self.start_button)

			# set the window frame to the start page frame
			self.options_frame = tk.Frame(self)

			# set the frame on the grid
			self.options_frame.grid(row=3, column=2, padx=1, pady=1)

			# Create buttons with the different options for the user
			""" self.color_choice = tk.Button(self.options_frame, 
																		text="Find Deck Staples", 
																		bg="#2f9fd6",
																		fg="white", 
																		activebackground="#146d99", 
																		activeforeground="white", 
																		font=("Garamond", 14),
																		command=lambda: self.mainWindow.create_frame(2)) """
			
			self.lands_algorithm = tk.Button(self.options_frame, 
																		text="Calculate How Many Lands Your Deck Needs", 
																		bg="#2f9fd6", 
																		fg="white", 
																		activebackground="#146d99", 
																		activeforeground="white", 
																		font=("Garamond", 14),
																		command=lambda: self.mainWindow.create_frame(1))
			
			self.help_button = tk.Button(self.options_frame, 
																		text="Help", 
																		bg="#2f9fd6", 
																		fg="white", 
																		activebackground="#146d99", 
																		activeforeground="white", 
																		font=("Garamond", 14),
																		command=lambda: self.mainWindow.create_frame(2))
			
			self.exit_button = tk.Button(self.options_frame,
																		text="Exit",
																		bg="#2f9fd6",
																		fg="white", 
																		activebackground="#146d99", 
																		activeforeground="white",
																		font=("Garamond", 14), 
																		command=sys.exit)

			#  set the buttons and labels on the grid 
			self.welcome_label.grid(row=0, column=2, padx=1, pady=1)
			self.choose_label.grid(row=1, column=2, padx=1, pady=1)
			self.blank_space_label.grid(row=2, column=2, padx=1, pady=30)
			
			# self.start.grid(row=2, column=2, padx=1, pady=1)
			# self.color_choice.grid(row=0, column=2, padx=1, pady=2, sticky="WES")
			self.lands_algorithm.grid(row=0, column=2, padx=1, pady=2, sticky="WEN")
			self.help_button.grid(row=1, column=2, padx=1, pady=2, sticky="WESN")
			self.exit_button.grid(row=2, column=2, padx=1, pady=2, sticky="WEN")


class LandCountPage(tk.Frame):
	def __init__(self, frameHash, mainWindow):
			super().__init__()
			self.frameHash = frameHash
			self.mainWindow = mainWindow
			self.label = tk.Label(self, text="Color Select Page")
			# create the button images 
			# self.start_button = PhotoImage(file="button_images/start_button.png")

			# Configure the row and 5 columns for the buttons. 
			# Configure the row and 5 columns for the buttons. 
			Grid.rowconfigure(self,0,weight=1)
			Grid.rowconfigure(self,1,weight=1)
			Grid.rowconfigure(self,2,weight=1)
			Grid.rowconfigure(self,3,weight=1)
			Grid.rowconfigure(self,4,weight=1)
			Grid.rowconfigure(self,5,weight=1)
			Grid.rowconfigure(self,6,weight=1)
			Grid.rowconfigure(self,7,weight=1)
			Grid.rowconfigure(self,8,weight=1)
			Grid.rowconfigure(self,9,weight=1)
			Grid.rowconfigure(self,10,weight=1)
			Grid.rowconfigure(self,11,weight=1)
			Grid.rowconfigure(self,12,weight=1)
			Grid.rowconfigure(self,13,weight=1)
			Grid.rowconfigure(self,14,weight=1)
			Grid.rowconfigure(self,15,weight=1)
			Grid.rowconfigure(self,16,weight=1)
			Grid.rowconfigure(self,17,weight=1)
			Grid.columnconfigure(self,0,weight=0)
			Grid.columnconfigure(self,1,weight=1)
			Grid.columnconfigure(self,2,weight=0)
			Grid.columnconfigure(self,3,weight=1)
			Grid.columnconfigure(self,4,weight=1)

			self.test_grid_label = tk.Label(self,
																			text="Mana Source Calculator",
																			font=("Garamond", 14))
			self.select_color_label = tk.Label(self,
																				 text="Please enter the information in the fields below",
																				 font=("Garamond", 14))
			self.instructions2 = tk.Label(self,
																		text="* Please count each card only once.",
																		font=("Garamond", 11))
			self.instructions3 = tk.Label(self,
																	 text="* If I card is both draw and ramp, count it as card draw",
																	 font=("Garamond", 11))
			self.draw_ramp_text3 = tk.Label(self,
																			text="* Card Draw: Draws at least one card",
																			font=("Garamond", 11))
			self.draw_ramp_text4 = tk.Label(self,
																			text="* Mana Ramp: adds mana or searches for land",
																			font=("Garamond", 11))
			self.avg_mana_text= tk.Label(self,
																	 text="Type the Average Mana Value",
																	 font=("Garamond", 14))
			self.avg_mana_text2 = tk.Label(self,
																		 text="(Round to Two Decimal Places)",
																		 font=("Garamond", 14))
			self.draw_ramp_text = tk.Label(self,
																		 text="Type the Total Number of Card Draw and Ramp",
																		 font=("Garamond", 14))
			self.draw_ramp_text2 = tk.Label(self,
																			text="of Mana Value of 2 or less",
																			font=("Garamond", 11))
			
			self.blank_space_label = tk.Label(self,
																			 text="")
			self.blank_space_label2 = tk.Label(self,
																			 text="",
																			 font=("Garamond", 16))
			self.text_input_avg_mana = tk.Text(self,
																	bg="#f0b49a", 
																	fg="#060606",
																	height=1,
																	width=6,
																	font=("Garamond", 14))
			self.text_input_draw_ramp = tk.Text(self,
																	bg="#f0b49a", 
																	fg="#060606",
																	height=1,
																	width=6,
																	font=("Garamond", 14))

			self.land_count_button = tk.Button(self,
																				text="Calculate Your Land Count",
																				bg="#D6662F",
																				fg="white", 
																				activebackground="#146d99", 
																				activeforeground="white",
																				font=("Garamond", 14),
																				command=lambda: 
																				self.find_land_count(self.text_input_avg_mana.get(1.0, "end-1c"),
																															 self.text_input_draw_ramp.get(1.0, "end-1c"))
																				)
			
			self.return_to_start_button = tk.Button(self,
																							text="Return to Main Menu",
																							bg="#2f9fd6",
																							fg="white", 
																							activebackground="#146d99", 
																							activeforeground="white",
																							font=("Garamond", 14),
																							command=lambda: self.mainWindow.create_frame(0))
																				
			self.exit_button = tk.Button(self,
																		text="Exit",
																		bg="#2f9fd6",
																		fg="white", 
																		activebackground="#146d99", 
																		activeforeground="white",
																		font=("Garamond", 14), 
																		command=sys.exit)

			self.test_grid_label.grid(row=1, column=1, padx=1, pady=(10, 1))
			self.select_color_label.grid(row=2, column=1, padx=1, pady=(1, 30))
			self.instructions2.grid(row=3, column=1, padx=1, pady=1)
			self.instructions3.grid(row=4, column=1, padx=1, pady=1)
			self.draw_ramp_text3.grid(row=5, column=1, padx=1, pady=1)
			self.draw_ramp_text4.grid(row=6, column=1, padx=1, pady=1)
			self.blank_space_label.grid(row=7, column=2, padx=1, pady=8)
			self.avg_mana_text.grid(row=8, column=1, padx=1, pady=1)
			self.avg_mana_text2.grid(row=9, column=1, padx=1, pady=1)
			self.text_input_avg_mana.grid(row=10, column=1, padx=0, pady=10)
			self.draw_ramp_text.grid(row=11, column=1, padx=0, pady=1)
			self.draw_ramp_text2.grid(row=12, column=1, padx=1, pady=1)
			self.text_input_draw_ramp.grid(row=13, column=1, padx=0, pady=10)
			self.blank_space_label2.grid(row=14, column=1, padx=1, pady=8)
			self.land_count_button.grid(row=15, column=1, padx=0, pady=2, sticky="WE")
			self.return_to_start_button.grid(row=16, column=1, padx=1, pady=2, sticky="WESN")
			self.exit_button.grid(row=17, column=1, pady=2, sticky="WEN")


	def find_land_count(self, mana_avg, ramp_draw):
		"""Uses the Calculate Your Land Count button to calculate the avg number of lands the deck needs
		"""

		# try to convert mana_avg from str to float. If error, return error message
		try: 
			avg = float(mana_avg)
			
		except ValueError:
			self.blank_space_label2["text"] = "Error: Please type an integer or decimal for average mana value"
			self.blank_space_label2["fg"] = "#F05039"
			return

		# try to convert ramp_draw from str to int. If error, return error message
		try: 
			dr = int(ramp_draw)

		except ValueError:
			self.blank_space_label2["text"] = "Error: Please type an integer for number of card draw and ramp"
			self.blank_space_label2["fg"] = "#F05039"
			return

		# no errors, so set text color to a pleasant color and use the land_count formula to calculate and display
		self.blank_space_label2["fg"] = "#148899"

		land_count = deck_build_algo.land_count(avg, dr)
		
		self.blank_space_label2["text"] = "Number of Lands Your Deck Needs: " + str(land_count)


class HelpPage(tk.Frame):
	"""Class to create the frame for the Help Page"""
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
			Grid.rowconfigure(self,6,weight=1)
			Grid.rowconfigure(self,7,weight=1)
			Grid.rowconfigure(self,8,weight=1)
			Grid.rowconfigure(self,9,weight=1)
			Grid.rowconfigure(self,10,weight=1)
			Grid.rowconfigure(self,11,weight=1)
			Grid.rowconfigure(self,12,weight=1)
			Grid.rowconfigure(self,13,weight=1)
			Grid.rowconfigure(self,14,weight=1)
			Grid.columnconfigure(self,0,weight=1)
			Grid.columnconfigure(self,1,weight=1)
			Grid.columnconfigure(self,2,weight=1)
			Grid.columnconfigure(self,3,weight=1)
			Grid.columnconfigure(self,4,weight=1)

			self.welcome_help_label = tk.Label(self,
																			text="Help Page",
																			font=("Garamond", 14))
			self.greeting_label = tk.Label(self,
																				 text="Thank you so much for using the Deck Building Companion App.",
																				 font=("Garamond", 14))
			
			self.information1_label = tk.Label(self,
																				 text="This app is designed to aid you, the user, in your deck building journey.",
																				 font=("Garamond", 14))
			
			self.information2_label = tk.Label(self,
																				 text="Whether you struggle with having too many (or too few) lands, aren't sure",
																				 font=("Garamond", 14))
			
			self.information3_label = tk.Label(self,
																				 text="how many sources of a specific color you should include, or would like",
																				 font=("Garamond", 14))
			
			self.information4_label = tk.Label(self,
																				 text="recommendations for cards to play in your deck, this app is for you.",
																				 font=("Garamond", 14))
			
			self.information5_label = tk.Label(self,
																				 text="Using the app is simple, and everything you need is only a few seconds and",
																				 font=("Garamond", 14))
			
			self.information6_label = tk.Label(self,
																				 text="clicks away. Just navigate to the page with the desired feature and follow",
																				 font=("Garamond", 14))
			
			self.information7_label = tk.Label(self,
																				 text="the included directions. It's fast and easy!",
																				 font=("Garamond", 14))
			
			self.information8_label = tk.Label(self,
																				 text="To get certain information, like the average Mana Value, we recommend using a ",
																				 font=("Garamond", 14))
			
			self.information9_label = tk.Label(self,
																				 text="deck building app, such as MoxField or ManaBox.",
																				 font=("Garamond", 14))
			
			self.information10_label = tk.Label(self,
																				 text="For questions or suggested features, please email us at korachof@gmail.com",
																				 font=("Garamond", 14))
			
			self.return_to_start_button = tk.Button(self,
																							text="Return to Main Menu",
																							bg="#2f9fd6",
																							fg="white", 
																							width = 30,
																							activebackground="#146d99", 
																							activeforeground="white",
																							font=("Garamond", 14),
																							command=lambda: self.mainWindow.create_frame(0))
																				
			self.exit_button = tk.Button(self,
																		text="Exit",
																		bg="#2f9fd6",
																		fg="white",
																		width = 30,
																		activebackground="#146d99", 
																		activeforeground="white",
																		font=("Garamond", 14), 
																		command=sys.exit)
			

			self.welcome_help_label.grid(row=1, column=2, pady=30, padx=1)
			self.greeting_label.grid(row=2, column=2, pady=1, padx=1)
			self.information1_label.grid(row=3, column=2, pady=(30, 1), padx=1)
			self.information2_label.grid(row=4, column=2, pady=1, padx=1)
			self.information3_label.grid(row=5, column=2, pady=1, padx=1)
			self.information4_label.grid(row=6, column=2, pady=(1, 30), padx=1)
			self.information5_label.grid(row=7, column=2, pady=1, padx=1)
			self.information6_label.grid(row=8, column=2, pady=1, padx=1)
			self.information7_label.grid(row=9, column=2, pady=1, padx=1)
			self.information8_label.grid(row=10, column=2, pady=(30, 1), padx=1)
			self.information9_label.grid(row=11, column=2, pady=1, padx=1)
			self.information10_label.grid(row=12, column=2, pady=30, padx=1)
			self.return_to_start_button.grid(row=13, column=2, pady=2, padx=1)
			self.exit_button.grid(row=14, column=2, pady=2, padx=1)


if __name__ == "__main__":
		testObj = WindowScreen()
		testObj.mainloop()

