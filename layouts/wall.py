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
num = 17
distance = 1
factor = 0.05
x = 0
z = 0

for strip in range(-(num/2), num/2):
	for pixel in range(-(pixels/2), pixels/2):
		lines.append('{"point": [%.2f, %.2f, %.2f]}' %
			(strip*distance, 0, pixel*factor))
print '[\n' + ',\n'.join(lines) + '\n]'
