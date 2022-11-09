#ბიბლიოთეკების ინიციალიზაცია
import obspy
from obspy import read

#პირველი ჩანაწერის წაკითხვა
first_data_stream = read("./Data/101.dat")
# print(first_data_stream)

#მეორე ჩანაწერის წაკითხვა
second_data_stream = read('./Data/102.dat')
print(second_data_stream)