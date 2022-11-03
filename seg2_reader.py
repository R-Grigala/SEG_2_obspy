import obspy

st = obspy.read("data_OYO_fixed.sg2")
print("start")
tr = st[0]
print(tr)
print("finish")