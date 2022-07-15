from manim import *
from typing import Union, Optional
from colour import Color
from contextlib import contextmanager

#Background color: 8C8984
#Main color: FF8000
#Dark Main Color: B36212
#Secondary color: 5E19FF
#Dark Secondary color: 3C09B3
#Tertiary color: 19FF34

BG_COLOR = Color("#0c1b31")#color.Color("#002365")#color.Color("#333333")
BG_COLOR_DARK = Color("#222222")
MAIN_COLOR = Color("#FF8000")
MAIN_COLOR_DARK = Color("#B36212")
SECOND_COLOR = Color("#59DEC9")#color.Color("#5E19FF")
SECOND_COLOR_DARK = Color("#3C09B3")
TERTIARY_COLOR = Color("#19FF34")
FOURTH_COLOR = YELLOW

class Colors:
	class Main:
		Background = Color("#0c1b31")
		Foreground = None

	class Dark:
		Background = None
		Foreground = None

	class Bright:
		Background = None
		Foreground = None

class ColorPalette:
	_parent: Optional["ColorPalette"]
	_foreground: Optional[Color]
	_background: Optional[Color]

	def __init__(self,
		parent: Optional["ColorPalette"] = None,
		foreground: Union[Color, str, None] = None,
		background: Union[Color, str, None] = None,
	) -> None:
		self._parent = parent
		if isinstance(foreground, str):
			self._foreground = Color(foreground)
		else:
			self._foreground = foreground
		
		if isinstance(background, str):
			self._background = Color(background)
		else:
			self._background = background
	
	def get_foreground(self) -> Optional[Color]:
		if self._foreground is not None:
			return self._foreground
		if self._parent is not None:
			return self._parent.get_foreground()
		return None
	
	def get_background(self) -> Optional[Color]:
		if self._background is not None:
			return self._background
		if self._parent is not None:
			return self._parent.get_background()
		return None

PRIMARY_PALETTE = ColorPalette(foreground="#FF8000", background="#0c1b31")

def apply_global_palette(palette: ColorPalette):
	pass

@contextmanager
def set_palette(palette: ColorPalette):
	try:
		# Set the provided color palette
		yield None
	finally:
		# Reset the color palette
		pass