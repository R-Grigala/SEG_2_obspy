import obspy

st = obspy.read("data_OYO_fixed.sgy")
print("start")
tr = st[0]
print(tr)
print("finish")