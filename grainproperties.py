grainid = open("cellid4.txt","r+")
colour = open("graincoloursim4","w")

# get second column values from grain id file
idvalues = []
for line in grainid:
    columns = line.split()
    idvalues.append(columns[1])

# assign colour to large and small grains
# small grains = 2, large grains = 35
for i in range(0, len(idvalues)):    
    if i == 0:
        if idvalues[i] == idvalues[i+1]:
            colour.writelines(["2\n"])
        else:
            colour.writelines(["35\n"])
    elif i == (len(idvalues)-1):
        if idvalues[i] == idvalues[i-1]:
            colour.writelines(["2\n"])
        else:
            colour.writelines(["35\n"])
    else:
        if idvalues[i] == idvalues[i+1]:
            colour.writelines(["2\n"])
        elif idvalues[i] == idvalues[i-1]:
            colour.writelines(["2\n"])
        else:
            colour.writelines(["35\n"])

colour.close()
grainid.close()
