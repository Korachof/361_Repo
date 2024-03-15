import tkinter as tk
from tkinter import *
import deck_build_algo
import staples_client
import sys


class WindowScreen(tk.Tk):
	"""Class to create the window and control the frames"""
	def __init__(self):
		super().__init__()
		
		self.title("MTG Deck Building Companion App")
		self.geometry("1280x720")
		
		Grid.rowconfigure(self,0,weight=1)
		Grid.columnconfigure(self,0,weight=1)
		self.frame_hash = {0: StartPage, 1: LandCountPage, 2: ColorSelectPage, 3: HelpPage, 4: ColorSelectResultsPage}
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
			self.label = tk.Label(self, text="Main")
			
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
																		text="Calculate Land Count", 
																		bg="#2f9fd6", 
																		fg="white", 
																		activebackground="#146d99", 
																		activeforeground="white",
																		width=30, 
																		font=("Garamond", 14),
																		command=lambda: self.mainWindow.create_frame(1))
			
			self.color_select = tk.Button(self.options_frame,
								 										text="Find Deck Staples",
																		bg="#2f9fd6", 
																		fg="white", 
																		activebackground="#146d99", 
																		activeforeground="white",
																		width=30, 
																		font=("Garamond", 14),
																		command=lambda: self.mainWindow.create_frame(2))
			
			self.help_button = tk.Button(self.options_frame, 
																		text="Help", 
																		bg="#2f9fd6", 
																		fg="white", 
																		activebackground="#146d99", 
																		activeforeground="white", 
																		font=("Garamond", 14),
																		command=lambda: self.mainWindow.create_frame(3))
			
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
			self.blank_space_label.grid(row=2, column=2, padx=1, pady=15)
			
			# self.start.grid(row=2, column=2, padx=1, pady=1)
			# self.color_choice.grid(row=0, column=2, padx=1, pady=2, sticky="WES")
			self.lands_algorithm.grid(row=0, column=2, padx=1, pady=2, sticky="WES")
			self.color_select.grid(row=1, column=2, padx=1, pady=2, sticky="WESN")
			self.help_button.grid(row=2, column=2, padx=1, pady=2, sticky="WESN")
			self.exit_button.grid(row=3, column=2, padx=1, pady=2, sticky="WEN")

			# allow for exiting without the mouse
			self.mainWindow.bind("<Escape>", lambda x: sys.exit())


class LandCountPage(tk.Frame):
	def __init__(self, frameHash, mainWindow):
			super().__init__()
			self.frameHash = frameHash
			self.mainWindow = mainWindow
			self.label = tk.Label(self, text="Land Count")
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
			self.text_input_avg_mana = tk.Entry(self,
																		bg="#f0b49a", 
																		fg="#060606",
																		width=6,
																		font=("Garamond", 14))
			self.text_input_draw_ramp = tk.Entry(self,
																		bg="#f0b49a", 
																		fg="#060606",
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
																		self.find_land_count(self.text_input_avg_mana.get(),
																									 self.text_input_draw_ramp.get()))
			
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
			self.draw_ramp_text.grid(row=11, column=1, padx=1, pady=1)
			self.draw_ramp_text2.grid(row=12, column=1, padx=1, pady=1)
			self.text_input_draw_ramp.grid(row=13, column=1, padx=0, pady=10)
			self.blank_space_label2.grid(row=14, column=1, padx=1, pady=8)
			self.land_count_button.grid(row=15, column=1, padx=0, pady=2, sticky="WE")
			self.return_to_start_button.grid(row=16, column=1, padx=1, pady=2, sticky="WESN")
			self.exit_button.grid(row=17, column=1, pady=2, sticky="WEN")

			# set the focus to the first text box so a mouse isn't required

			self.text_input_avg_mana.focus_set()

			# add ability to use arrow keys to jump between text fields

			self.mainWindow.bind("<Up>", lambda y: self.text_input_avg_mana.focus_set())
			self.mainWindow.bind("<Down>", lambda y: self.text_input_draw_ramp.focus_set())

			# set it so the enter button will also work with calculating land count

			self.text_input_avg_mana.bind("<Return>", lambda e: self.text_input_draw_ramp.focus_set())

			self.text_input_draw_ramp.bind("<Return>", lambda e: self.find_land_count(self.text_input_avg_mana.get(),
																			 		  self.text_input_draw_ramp.get()))
			# allow for exiting without the mouse
			self.mainWindow.bind("<Escape>", lambda x: sys.exit())


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


class ColorSelectPage(tk.Frame):
	""""Class to create the frame for the Color Select Page"""
	def __init__(self, frameHash, mainWindow):
		super().__init__()
		self.frameHash = frameHash
		self.mainWindow = mainWindow
		self.label = tk.Label(self, text="Color Select")
		self.staples_list_string = None

		# Configure the row and 5 columns for the buttons. 
		Grid.rowconfigure(self,0,weight=1)
		Grid.rowconfigure(self,1,weight=1)
		Grid.rowconfigure(self,2,weight=1)
		Grid.rowconfigure(self,3,weight=1)
		Grid.rowconfigure(self,4,weight=1)
		Grid.rowconfigure(self,5,weight=1)
		Grid.rowconfigure(self,6,weight=1)
		Grid.rowconfigure(self,7,weight=1)
		Grid.columnconfigure(self,0,weight=1)
		Grid.columnconfigure(self,1,weight=1)
		Grid.columnconfigure(self,2,weight=1)
		Grid.columnconfigure(self,3,weight=1)
		Grid.columnconfigure(self,4,weight=1)

		# text label
		self.directions_label = tk.Label(self, text="Please select each button that represents your commander's color identity below.", font=("Garamond", 14))
		self.directions_label2 = tk.Label(self, text="Once you have selected your deck's colors, press Find Staples Now", font=("Garamond", 14))
		self.directions_label3 = tk.Label(self, text="When a color is selected, the button will turn grey.", font=("Garamond", 13))
		self.directions_label4= tk.Label(self, text="Click a button a second time to unselect that color.", font=("Garamond", 13))
									
		
		# "Please select which colors are included in your deck below"
		self.white_button = PhotoImage(file="button_images/white.png")
		self.blue_button = PhotoImage(file="button_images/blue.png")
		self.black_button = PhotoImage(file="button_images/black.png")
		self.red_button = PhotoImage(file="button_images/red.png")
		self.green_button = PhotoImage(file="button_images/green.png")

		# check button variables
		self.white_var = 0
		self.blue_var = 0
		self.black_var = 0
		self.red_var = 0
		self.green_var = 0

		self.options_frame = tk.Frame(self)
		self.options_frame.grid(row=4, column=2, padx=1, pady=30, sticky="S")

		# Set the MTG color buttons
		self.white = Button(self.options_frame,
						 image=self.white_button,
						 command=lambda: self.color_choice("w"))
		self.blue = Button(self.options_frame,
						 image=self.blue_button,
						 command=lambda: self.color_choice("u"))
		self.black = Button(self.options_frame,
						 image=self.black_button,
						 command=lambda: self.color_choice("b"))
		self.red = Button(self.options_frame,
						 image=self.red_button,
						 command=lambda: self.color_choice("r"))
		self.green = Button(self.options_frame,
						 image=self.green_button,
						 command=lambda: self.color_choice("g"))
		
		# set menu option buttons 

		self.find_staples_button= tk.Button(self,
									 			text="Find Staples Now",
												bg="#D6662F",
												fg="white", 
												width=30,
												activebackground="#146d99", 
												activeforeground="white",
												font=("Garamond", 14),
												command=lambda: self.find_color_staples())

		self.return_to_start_button = tk.Button(self,
												text="Return to the Main Menu",
												bg="#2f9fd6",
												fg="white", 
												width=30,
												activebackground="#146d99", 
												activeforeground="white",
												font=("Garamond", 14),
												command=lambda: self.mainWindow.create_frame(0))

		self.exit_button = tk.Button(self,
									 text="Exit",
									 bg="#2f9fd6",
									 fg="white", 
									 width=30,
									 activebackground="#146d99", 
									 activeforeground="white",
									 font=("Garamond", 14), 
									 command=sys.exit)
		
		# Set the grid for the instructions
		self.directions_label.grid(row=0, column=2, columnspan=5, padx=1, pady=1)
		self.directions_label2.grid(row=1, column=2, columnspan=5, padx=1, pady=1)
		self.directions_label3.grid(row=2, column=2, columnspan=5, padx=1, pady=1)
		self.directions_label4.grid(row=3, column=2, columnspan=5, padx=1, pady=1)
		
		# Set the grid for each of the MTG color buttons
		self.white.grid(row=1,
						column=0,
						padx=2)
		self.blue.grid(row=1,
						column=1,
						padx=2)
		self.black.grid(row=1,
						column=2,
						padx=2)
		self.red.grid(row=1,
						column=3,
						padx=2)
		self.green.grid(row=1,
						column=4,
						padx=2)
		
		# set the grid for the start button
		self.find_staples_button.grid(row=5,
									  column=2,
									  padx=1,
									  pady=2,
									  sticky="S")

		
		# Set the grid for the Return to Main Menu button
		self.return_to_start_button.grid(row=6,
										 column=2,
										 padx=1,
										 pady=2,
										 sticky="S")

		# Set the grid for the exit button
		self.exit_button.grid(row=7,
				   column=2,
				   padx=1,
				   pady=2,
				   sticky="N")
		
	def color_choice(self, choice):
		"""Function that takes user button selects and changes the color + relief state of those buttons
		based on whether they've been clicked or not."""
		if choice == "w":
			if self.white_var == 0:
				self.white_var += 1
				self.white.config(relief=SUNKEN, bg="grey")
			
			else:
				self.white_var -= 1
				self.white.config(relief=RAISED, bg="white")
	
		elif choice == "u":
			if self.blue_var == 0:
				self.blue_var += 1
				self.blue.config(relief=SUNKEN, bg="grey")
			
			else:
				self.blue_var -= 1
				self.blue.config(relief=RAISED, bg="white")
			
		elif choice == "b":
			if self.black_var == 0:
				self.black_var += 1
				self.black.config(relief=SUNKEN, bg="grey")
			
			else:
				self.black_var -= 1
				self.black.config(relief=RAISED, bg="white")
			
		elif choice == "r":
			if self.red_var == 0:
				self.red_var += 1
				self.red.config(relief=SUNKEN, bg="grey")
			
			else:
				self.red_var -= 1
				self.red.config(relief=RAISED, bg="white")
		
		elif choice == "g":
			if self.green_var == 0:
				self.green_var += 1
				self.green.config(relief=SUNKEN, bg="grey")
			
			else:
				self.green_var -= 1
				self.green.config(relief=RAISED, bg="white")

	def find_color_staples(self):
		"""Function that takes the selected colors from the buttons and connects to a microservice to return a list with
		all staples of those selected colors."""

		# initialize color_list with just colorless
		color_list = "c"

		if self.white_var > 0:
			color_list = color_list + " w"

		if self.blue_var > 0:
			color_list = color_list + " u"

		if self.black_var > 0:
			color_list = color_list + " b"

		if self.red_var > 0:
			color_list = color_list + " r"

		if self.green_var > 0:
			color_list = color_list + " g"

		self.staples_list_string = staples_client.clientInput(color_list)

		# Display the Results Page Frame
		self.mainWindow.create_frame(4)

class ColorSelectResultsPage(tk.Frame):
	"""Class to create the frame that will display the results from the Color Select Page"""
	def __init__(self, frameHash, mainWindow):
			super().__init__()
			self.frameHash = frameHash
			self.mainWindow = mainWindow
			self.label = tk.Label(self, text="Deck Staples Results")

			self.page_text_label = tk.Label(self,
								   			text="The Results Containing Your Deck's Staples are Below",
											font = ("Garamond", 14))
			
			self.page_instructions_label = tk.Label(self,
										   			text="To scroll through the list, click inside of the text box and either use",
													font= ("Garamond", 13))
			
			self.page_instructions2_label = tk.Label(self,
										   			text="the scroll wheel on your mouse or the arrow keys on your keyboard.",
													font= ("Garamond", 13))
			

			# text box set to width of 32 since longest card name is 31 characters
			self.staples_output = Text(self, height=10, width=32)
			self.staples_output.tag_configure("center", justify="center")

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

			# open the text file and display its contents 
			with open("staples_file.txt", "r") as staples_list_display:
				self.staples_output.insert(INSERT, staples_list_display.read())

			self.staples_output.tag_add("center", "1.0", "end")


			# Make the Menu buttons
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

			# set the labels on the grid 
			self.page_text_label.grid(row=0, column=1, padx=1, pady=1, sticky="S")
			self.page_instructions_label.grid(row=1, column=1, padx=1, pady=1, sticky="NS")
			self.page_instructions2_label.grid(row=2, column=1, padx=1, pady=1, sticky="N")
			self.staples_output.grid(row=3, column=1, padx=1, pady=40)
			self.return_to_start_button.grid(row=4, column=1, padx=1, pady=1, sticky="S")
			self.exit_button.grid(row=5, column=1, padx=1, pady=1, sticky="N")


class HelpPage(tk.Frame):
	"""Class to create the frame for the Help Page"""
	def __init__(self, frameHash, mainWindow):
			super().__init__()
			self.frameHash = frameHash
			self.mainWindow = mainWindow
			self.label = tk.Label(self, text="Help")
			
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

		# allow for exiting without the mouse
			self.mainWindow.bind("<Escape>", lambda x: sys.exit())


if __name__ == "__main__":
		testObj = WindowScreen()
		testObj.mainloop()

