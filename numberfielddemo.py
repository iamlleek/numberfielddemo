"""
Program: textfielddemo.py
Author: Nylek 10/14/2020
example from page 264 - 265

Simple python GUI window with a basic label
"""

from breezypythongui import EasyFrame
import math

class NumberFieldDemo(EasyFrame):
	"""Computes and displays the square root of an input number."""

	def __init__(self):
		"""Sets up the window and the label."""
		EasyFrame.__init__(self, title = "Number field Demo")

		# Label and field for the input
		self.addLabel(text = "An integer", row = 0, column = 0)
		self.inputField = self.addIntegerField(value = 0, row = 0, column = 1, width = 10)
		# Blind the Enter key to the inputField
		self.inputField.bind("Return>", lambda event: self.computeSqrt())

		# Label and field for the output
		self.addLabel(text = "Square root", row = 1, column = 0)
		self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, state = "readonly", width = 8, precision = 2)

		# The command button
		self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.computeSqrt)

	# The event handling method for the button
	def computeSqrt(self):
		"""Inputs the integer, computes the square root and outputs the results."""
		try:
			number = self.inputField.getNumber()
			result = math.sqrt(number)
			self.outputField.setNumber(result)
		except ValueError:
			self.messageBox(title = "ERROR", message = "Input must be an integer >= 0")
				
def main():
		"""Instantiates and pops up the window."""
		NumberFieldDemo().mainloop()

# Global call to the main() function
main()