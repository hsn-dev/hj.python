import csv 
from datetime import datetime
import os 

traffic_data = '11.41G'
time = datetime.now().strftime("%H:%M:%S")
date = datetime.now().date().strftime("%B %d, %Y")
print("Date: ", date)
print("Time: ", time)


# with open(r'C:\Users\Hasan\Desktop\New folder\DataUsage1.csv', 'a', newline='') as csvfile:
    
#     fieldnames = ['Date', 'Time', 'Usage']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')

#     writer.writeheader()
#     writer.writerow({'Date': date, 'Time': time, 'Usage': traffic_data})


with open(r'C:\Users\Hasan\Desktop\New folder\DataUsage2.txt', 'a') as f:
	filesize = os.path.getsize(r'C:\Users\Hasan\Desktop\New folder\DataUsage2.txt')
	if filesize == 0:
		f.write("Date\t\tTime\t\tUsage\n")
	f.write(date + "\t")
	f.write(time + "\t")
	f.write(traffic_data + "\n")