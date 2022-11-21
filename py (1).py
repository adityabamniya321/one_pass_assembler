opTable={'START':99,'STL':1,'JSUB':2,'LDA':3,'COMP':4,'JEQ':5,
         '+JSUB':6,'J':7,'LDX':8,'TD':9,'JEQ':10,'RD':11,'STCH':12,'TIX':13,
         'CLEAR':14,'WD':15,'JLT':16,'LDB':17,'BASE':18,'LDT':19,'+LDT':20,'RD':21,
         'COMPR':22,'TIXR':23,'STX':24,'LDCH':25,'RSUB':26 }

i=1
symbolTable={}
OPCODE=''
#fimction to return Opcode 
def getOpcode(line):
    if(len(line)==3):
        OPCODE=line[1]
    if(len(line)==2):
        OPCODE=line[0] 
    return OPCODE

file = open("assembly.txt")
 # Splitting all columns and rows of paragraph  
content = file.readlines()
line=content[0].split()
OPCODE=getOpcode(line)

if OPCODE=='START':
    address=int(line[2])
    locCtr=address
    # write line to intermediate file
    
    nextLine = content[1].split()
else:
    locCtr=0
    
for i in range(2,len(content)):
    if OPCODE=='END':
        break
    if(nextLine[0]!='.'):
        if(nextLine[0] in symbolTable.keys()):
                print("Duplication find !!")
                break
        else:
            if(len(nextLine)>2):
                symbolTable.update({nextLine[0]: locCtr})
        
        if(OPCODE in opTable.keys()):
            locCtr+=3
        elif OPCODE=='WORD':
            locCtr+=3
        elif OPCODE=='RESW':
            locCtr=locCtr+int(3*nextLine[2])
        elif OPCODE=='RESB':
            locCtr+=int(nextLine[2])
        elif OPCODE=='BYTE':
            #add len to LOCCTR
            # length=len(line[2])-3
            locCtr+=1
        else:
            print("Invalid Opearion Code",OPCODE)
            exit()
    
    nextLine=content[i]
    nextLine=nextLine.split()
programLen=locCtr-address

print("Program Length: "+str(programLen))
print("Symbol Table is : ",symbolTable)