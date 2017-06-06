import math as m

def valleyToStandard(kos, bans):
	eastKm  = 0.2*bans*m.cos(m.pi/18) + 15*kos*m.cos(19*m.pi/36)
	northKm = 0.2*bans*m.cos(5*m.pi/9) + 15*kos*m.cos(m.pi/36)
	return {"eastKm": eastKm,"northKm": northKm}

def standardToValley(eastKm, northKm):
	bans = 5*(eastKm*m.cos(m.pi/36)+northKm*m.cos(5*m.pi/9))
	kos  = 1/15.0*(eastKm*m.cos(19*m.pi/36)+northKm*m.cos(m.pi/36))
	print kos
	return {"kos": kos, "bans": bans}


val = int(input('Select the conversion type(1 for valley to standard, 2 for standard to valley):'))

if val==1:
	kos = float(input("Enter the number of kos: "))
	bans = float(input("Enter the number of bans: "))
	kmData = valleyToStandard(kos,bans)
	print "Distance along east: " + str(kmData["eastKm"])+ ", Distance along north: "+ str(kmData["northKm"])

elif val==2:
	eastKm = float(input("Enter the number of Kilometer in East: "))
	northKm = float(input("Enter the number of Kilometer in North: "))
	valleyData = standardToValley(eastKm,northKm)
	print "Number of kos: " + str(valleyData["kos"])+ ", Number of Bans: "+ str(valleyData["bans"])

else:
	print "Please enter either 1 or 2"