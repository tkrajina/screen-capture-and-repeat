#!/usr/bin/env python3

import datetime
import math
import os
import subprocess
import sys
import time
from typing import *

import pyautogui  # type: ignore
from PIL import Image, ImageDraw, ImageFont  # type: ignore

from screens.img import *
from screens.utils import *

seconds = 2
time.sleep(2)
print(f"Screenshow in {seconds}s")
tmp_filename = "__tmp.png"
img = pyautogui.screenshot()
coef = 3
img = img.resize((int(img.width / coef), int(img.height / coef)))
img.save(tmp_filename)
print(f"Saving screenshot {tmp_filename}")

coordinates: List[Tuple[int, int]] = []

while True:
	# Open window and wait for upper left click
	print("Click on upper-left part of the screenshot area")
	x, y = show_image(tmp_filename, img.width, img.height)
	print(x, y)
	if x < 0 or y < 0:
		sys.exit(0)
	coordinates.append([x, y])
	for c in coordinates:
		x, y = c[0], c[1]
		txt = f"({int(x)},{int(y)})"
		print(txt)
		draw = ImageDraw.Draw(img)
		draw.line((x-5, y, x+5, y), fill="orange")
		draw.text((x+2, y+2), txt)
		draw.line((x, y - 5, x, y + 5), fill="orange")
	print()

	img.save(tmp_filename)