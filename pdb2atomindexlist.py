#pdb2atomindexlist script
#Specifying a .pdb protein database file and path
#Write the Atom you want when asked (e.g.: O)
#Get a printed List of atom indexes and also a 
#plain text .txt file with all of them.




import os

#1
#Use one of the options to specify the folder of the files/proyect folder
#The first one refers to the home folder of LINUX.
#home=os.environ['HOME']
home='G:/MD/VMD'

#2
#specify the pdb file to read and the txt file to write
FILETOREAD="protein_ions.pdb"
FILENAMETOWRITE="atomlist.txt"

#3
#Use this folder variable to build your own path.
folder=home + '/KBP_K_1M_pullslow/md/'



pdb=tuple(open(folder+FILETOREAD))
atom_start=0
atom_end=0
linecontent=[]
global atom_coordinates
linestoExport=[]

atom_counter=0
atom_index_matrix=[]

atom_selected=raw_input("Which ATOM do you want to extract?:")

print 'ATOM selected: ' + str(atom_selected)

for i in range(0,len(pdb)):
    linecontent=pdb[i]
    if linecontent[:4]=="ATOM":
        if atom_start==0:
            atom_start=i+1
        atom_end=i+1
        linecontent=[]
        linecontent=pdb[i].split()
        if atom_selected in linecontent[2]:
            atom_index_matrix.append(linecontent[1])
            atom_counter+=1
            #print i, pdb[i]
            # Get the bounds +2 length
            
    if linecontent[:3]=="TER":
        break

print atom_index_matrix
print atom_counter

atomfile=open(folder+FILENAMETOWRITE,"w")

for i in range(0,len(atom_index_matrix)):
        atomfile.write(atom_index_matrix[i]+" ")

atomfile.write("\n"+str(atom_counter))

atomfile.close()

