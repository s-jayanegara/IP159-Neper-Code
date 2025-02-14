grainid = open("cellid4.txt","r+")
colour = open("graincoloursim4","w")

'''
for n in range(1,90):
    # large grains
    if n in (1,22,53,73,89):
        colour.writelines(["80\n"])
    else:
        # small grains
        colour.writelines(["66\n"])
colour.close()
'''

# get second column values from grain id file
idvalues = []
for line in grainid:
    columns = line.split()
    idvalues.append(columns[1])

# assign colour to large and small grains
# small grains = 66, large grains = 80
# small grains = 1, large grains = 80
# small grains = 4, large grains = 66
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