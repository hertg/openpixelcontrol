#!/usr/bin/env python

spacing = 0.11  # m
lines = []
#for c in range(-12, 13):
#    rs = [range(30), reversed(range(30))][c % 2]
#    for r in rs:
#        lines.append('  {"point": [%.2f, %.2f, %.2f]}' %
#                     (c*spacing, 0, (r - 24.5)*spacing))
#print '[\n' + ',\n'.join(lines) + '\n]'

pixels = 60
strips = 17
horizontal = 1
vertical = 0.05
x = 0
y = 0
z = 0

for strip in range(strips):
	if strip < 5:
		x = (3*horizontal)
		y = (5-strip)*horizontal
	elif strip > 11:
		x = -(3*horizontal)
		y = (strip-11)*horizontal
	else:
		x = 8-strip*horizontal		
#		if strip < 9:
#			x = 9-strip*horizontal
#		else:
#			x = strip-9*horizontal
		y = 0
		

	for pixel in range(pixels):
		if pixel < (pixels/2):
			z = -((pixels/2)-pixel)*vertical
		elif pixel > (pixels/2):
			z = (pixel-(pixels/2))*vertical
		else:
			z = 0

		lines.append('{"point": [%.2f, %.2f, %.2f]}' %
			(x, y, z))

# red green blue

print '[\n' + ',\n'.join(lines) + '\n]'
