dir = 'c:/Users/52166/Documents/Python/Files/'
fname = input('Enter the file name:')
try:
    docLink = open(dir+fname)
    print ('\n\n')
except:
    print('File doesnt exist, cannot be opened: '+fname)
    quit()

count = 0



for line in docLink:
    count = count + 1
    print(line.strip())



print('Number of lines: ' + str(count))
print('\n\nTHE END.....')