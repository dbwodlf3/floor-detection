# Read Image
from lib import filter_edge

filename = 'sample3.jpg'

for i in range(0, 100):
    filter_edge(filename, i, 0, 5)
