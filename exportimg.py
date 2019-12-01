import glob, os

f = open("shoebox.html","a+")
f.write("""<html>
<head>
    <title>Python IMG Export</title>  
    <style>  
        img { 
            width: 200px; 
            height: 200px; 
            object-fit: contain; 
        } 
    </style>  
</head>  
<body>""")

# set up variables and path
fileCount = 0
dirCount = 0
# use the current directory
PATH="."

for root, dirs, files in os.walk(PATH):
    #print('Looking in:',root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

print('Number of files',fileCount)
f.write('Number of files %d' % fileCount)
f.write("<table><tr> \r\n")


os.chdir(".")
lst = glob.glob('**/**/*.jpeg')
for ind, smb in enumerate(lst):
    print(smb, end='')
    f.write("<td><img src='%s' /></td> \r\n" % smb)
    if ind%5 == 4: 
        print('\n')
        f.write('</tr><tr> \r\n')
        
        
f.write('</table></body></html>')
f.close()
