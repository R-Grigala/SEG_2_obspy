import obspy
import matplotlib as plt

st = obspy.read("data_OYO_fixed.dat")
print("start")
st[0].plot()
print("finish")