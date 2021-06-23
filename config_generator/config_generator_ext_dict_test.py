#imports
import sys
import csv

# Ask for the switch details and set it as the hostname variable.
hostname = input("Enter the switch name: ")
swbrand = input("cisco or cruba switch? ")
swtype = input("Switch type: L2 or sub? ")
trunk1 = input("Primary trunk interface name? ")
trunk2 = input("Secondary trunk interface name? ")
if ((swtype == 'sub') and (swbrand == 'cisco')):
	templateFile = "cisco-subswitch_template.txt"
elif ((swtype == 'L2') and (swbrand == 'cisco')):
	templateFile = "cisco-L2switch_template.txt"
elif ((swtype == 'sub') and (swbrand == 'aruba')):
	templateFile = "aruba-subswitch_template.txt"
elif ((swtype == 'L2') and (swbrand == 'aruba')):
	templateFile = "aruba-L2switch_template.txt"

print("Writing configuration for " + hostname)

#Initate the CSV connection.  Set the row number for future use.  
#with open('L2_switchconfig.csv') as csvfile:
	#readCSV = csv.reader(csvfile, delimiter=',')
	#switchnameRow = []
	#gatewayRow = []
	#switch_ipRow = []
	#for row in readCSV:
		#switchname = row[0]
		#gateway = row[1]
		#switch_ip = row[2]
		##to add a new variable, specify its column number here.
		
		#switchnameRow.append(switchname)
		#gatewayRow.append(gateway)
		#switch_ipRow.append(switch_ip)
		#print(row)
	##This is where you tell it what to search for.
	#coldex = switchname.index(switchname)
	#Ogateway = gateway[coldex]
	#Oswitch_ip = switch_ip[coldex]
	#print("Switch name = " + switchname)
	#print("Gateway = " + gateway)
	#print("Switch IP = " + switch_ip)
	
final_dict = {}
with open('L2_switchconfig.csv', mode='r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		final_dict = dict((rows[0],rows[1]) for rows in reader)
		
		Print(row)

		
		

# Here we take the switch config template file, replace the hostname, and create a new hostname.txt file.
fin = open(templateFile, "rt")
fout = open(hostname + ".txt", "wt")

for line in fin:
	fout.write(line.replace('$hostname$', hostname))

fin.close()
fout.close()

#Here we edit the hostname.txt file and replace the other variables from the CSV.

fin = open((hostname + ".txt"),"rt")
data = fin.read()
data = data.replace('$gateway$',final_row[hostname],'gateway')
data = data.replace('$switch_ip$',final_row[hostname],'switch_ip')
data = data.replace('$trunk1',trunk1)
data = data.replace('$trunk2',trunk2)
#If you want to add a new variable, just make a new column for it in the csv, place it in the template, call it in the row function, and copy the line above here.
fin.close()

fin = open((hostname + ".txt"), "wt")
fin.write(data)
fin.close()


