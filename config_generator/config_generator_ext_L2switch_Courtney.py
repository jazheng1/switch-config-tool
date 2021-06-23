import sys
import csv

# Ask for the switch name and set it as the hostname variable.
hostname = input("Enter the switch name: ")
# ensure the host name is in capital letters to match CSV format
hostname.upper()
hostname = hostname.upper()

swbrand = input("Cisco or Aruba switch? ")
# ensure user input matches if statements below
swbrand.lower()
swbrand = swbrand.lower()

swtype = input("Switch type: L2 or sub? ")
# is the switch type valid?
if (swtype != "L2") and (swtype != "sub"):
	swtype = input("Please input a valid switch type: L2 or sub ")

trunk1 = input("Primary trunk interface name? ")
trunk2 = input("Secondary trunk interface name? ")

if ((swtype == 'sub') and (swbrand == 'cisco')):
	templateFile = "cisco-subswitch_template.txt"
	switchname = hostname + "-subswitch"
elif ((swtype == 'L2') and (swbrand == 'cisco')):
	templateFile = "cisco-L2switch_template.txt"
	switchname = hostname + "-switch"
elif ((swtype == 'sub') and (swbrand == 'aruba')):
	templateFile = "aruba-subswitch_template.txt"
	switchname = hostname + "-subswitch"
elif ((swtype == 'L2') and (swbrand == 'aruba')):
	templateFile = "aruba-L2switch_template.txt"
	switchname = hostname + "-switch"

	
print("Writing configuration for " + hostname + "  " + swtype) 

#Initate the CSV connection.  Set the row number for future use.  Declare empty variables.

with open("L2_switchconfig.csv") as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')

#designate the location of values in csv
	for row in readCSV:
		if row[0] == hostname: 
			hostname = row[0]
			gateway = row[1]
			switch_ip = row[2]
			guest1VLAN = row[3]
			hibandguestVLAN = row[4]
			studentVLAN = row[5]
			labsVLAN = row[6]
			employeeVLAN = row[7]
			netadminVLAN = row[8]
			wapvendVLAN = row[9]
			phonesVLAN = row[10]
			doodadsVLAN = row[11]			

			#to add a new variable, specify its column number here.

			#if the vlan is blank, set the subswitch vlan value

			if guest1VLAN == "":
				guest1VLAN = "10"
			if hibandguestVLAN == "":
				hibandguestVLAN = "11"
			if studentVLAN == "":
				studentVLAN = "20"
			if labsVLAN == "":
				labsVLAN = "21"
			if employeeVLAN == "":
				employeeVLAN = "30"
			if netadminVLAN == "":
				netadminVLAN = "31"
			if wapvendVLAN == "":
				wapvendVLAN = "40"
			if phonesVLAN == "":
				phonesVLAN = "50"
			if doodadsVLAN == "":
				doodadsVLAN = "60"
				
				
			


	#This is where you tell it what to search for.
	coldex = switchname.index(switchname)
	Ogateway = gateway[coldex]
	Oswitch_ip = switch_ip[coldex]
	
	#print the key variables for error checking
	print("Switch name = " + switchname)
	print("Gateway = " + gateway)
	print("Switch IP = " + switch_ip)
		
		

# Here we take the switch config template file, replace the hostname, and create a new hostname.txt file.

fin = open(templateFile, "rt")
##outfile = "/generated/" + switchname + ".txt"
fout = open(switchname + ".txt", "wt")
for line in fin:
	fout.write(line.replace('$hostname$', switchname))
fin.close()
fout.close()	
		


#Here we edit the hostname.txt file and replace the other variables from the CSV.

fin = open((switchname + ".txt"),"rt")
##fin = open((outfile),"rt")  <-failure to use relative path
data = fin.read()
data = data.replace('$gateway$',gateway)
data = data.replace('$switch_ip$',switch_ip)
data = data.replace('$guest1VLAN$',guest1VLAN)
data = data.replace('$hibandguestVLAN$',hibandguestVLAN)
data = data.replace('$studentVLAN$',studentVLAN)
data = data.replace('$labsVLAN$',labsVLAN)
data = data.replace('$employeeVLAN$',employeeVLAN)
data = data.replace('$netadminVLAN$',netadminVLAN)
data = data.replace('$wapvendVLAN$',wapvendVLAN)
data = data.replace('$phonesVLAN$',phonesVLAN)
data = data.replace('$doodadsVLAN$',doodadsVLAN)
data = data.replace('$trunk1$',trunk1)
data = data.replace('$trunk2$',trunk2)



#If you want to add a new variable, just make a new column for it in the csv, place it in the template, call it in the row function, and copy the line above here.
fin.close()

fin = open((switchname + ".txt"), "wt")
fin.write(data)
fin.close()


