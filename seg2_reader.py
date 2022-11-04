import obspy

st = obspy.read("seg2_seismic.sgy")
print("start")
tr = st[0]
print(tr)
print("finish")