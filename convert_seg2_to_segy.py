# ბიბლიოთეკების ინიციალიზაცია
import obspy
from obspy import read

# პირველი ჩანაწერის წაკითხვა
first_data_stream = read("./Data/101.dat")
# print(first_data_stream)

# მეორე ჩანაწერის წაკითხვა
second_data_stream = read('./Data/102.dat')
# print(second_data_stream)

# ორი ჩანაწერის გადასაბმელად საჭიროა მეორე ჩანაწერის დაწყების დრო ემთხვეოდეს 
# პირველი ჩანაწერის დასრულების დროს
for i in range(len(second_data_stream)):
    second_data_stream[i].stats['starttime'] = first_data_stream[0].stats['endtime']

# ორი ჩანაწერის გაერთიანება: Trace მონაცემებით
both_stream = first_data_stream + second_data_stream
# print(both_stream[45].stats)
# both_stream.plot()

# გაერთიანებული მონაცემების ფაილში ჩაწერა
both_stream.write("both_stream.sgy", format="SEGY")