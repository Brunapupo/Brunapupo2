dias = int ( input (" "))
km = int ( input ( " " ))
if (km / dias) >= 60:
    km = km - (60 * dias)
    total = dias * 45 + km * 0.50
    print (total)
else:
    km = 0
    total = dias * 45 + km * 0.50
    print (total)