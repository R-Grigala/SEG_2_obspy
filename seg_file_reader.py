import obspy
from obspy import read

data_stream = read("./Data/101.dat")
print(data_stream)
print(data_stream.stats['seg2'])