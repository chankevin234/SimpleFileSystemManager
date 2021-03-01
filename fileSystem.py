#imported libraries
import sys
import math
from os import system, name 

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 

class File: #1 1KB Block
    def __init__(self, giveID=str, size=int): #constructor
        self.giveID = giveID # the name data
        self.size = size # size in bytes
        self.nextval = None # the reference to the next node
        
    def blockNumber(self): #checks for how many blocks to allocate file
        fileSize = self.size
        if (fileSize > 1024):
            # print(self.giveID + " is too big for 1 block")
            blocks = math.ceil(fileSize / 1024)
            # print("OS needs to use these many blocks: {}".format(blocks))
        else:
            blocks = 1
            # print("OS needs to use these many blocks: 1")
        return blocks

class FileSystem: #file system linked list
    
    def __init__(self, remaining=int): #constructor
        self.headval = None #set the head value of this linked list as null initially
        self.remaining = remaining #set size of filesystem
    
    def countNodes(self, head): #counts the # of nodes in the list takes in the head value of blockList
        count = 1 # assuming that head != None
        current = head
        while current.nextval is not None: #keep printing if there exists another following block
            current = current.nextval
            count += 1
        return count

    def printAllFiles(self): #prints out the list of nodes in linkedList
        printval = self.headval #checks for whether head of linked list is null
        
        print("FileName/GiveID      Size        Blocks Used")
        while (printval is not None): #iterates through list
            print ("{}        {}        {}".format(printval.giveID, printval.size, printval.blockNumber())) #print nodes
            printval = printval.nextval #append block connected to head
        
    
    def saveFile(self, newFile, size=int): #saves a file to beg of the linked list 
        if (newFile == "defaultHeadNode"):
            print("You can't create more default memory... file not added")
            return
        
        newBlock = File(newFile, size) #sets value for newBlock
        remainingBlocks = self.remaining #checking for remaining memory
        fileBlockNum = newBlock.blockNumber() #num of blocks needed for this file

        if(fileBlockNum > remainingBlocks):
            print("No more room... file not added")
            return
        
        newBlock.nextval = self.headval #sets the following block to be the new head (adds to front of the list)
        self.headval = newBlock #sets the new head value of the linked list to newBlock
        self.remaining -= fileBlockNum #subtracting from total memory
        print("OS needs to use these many blocks: {}".format(fileBlockNum))
        return 

    def deleteFile(self, removeKey): #removes file based on the removekey
        if (removeKey == "defaultHeadNode"): #prevents removal of defaultHeadNode
            print("Can't delete default memory")
            return
        temp = self.headval 
        prev = self.headval 
        if (temp.giveID == removeKey): 
            self.remaining += temp.blockNumber()
            temp.giveID = temp.nextval.giveID 
            temp.nextval = temp.nextval.nextval #removes the desired node right away 
            return
        while (temp.nextval is not None and temp.giveID != removeKey): 
            prev = temp 
            temp = temp.nextval
        if (temp.nextval is None and temp.giveID != removeKey): 
            # print("Can't delete the file as it doesn't exist") 
            return False
        # If node is last node of the linked list 
        elif (temp.nextval is None and temp.giveID == removeKey): 
            prev.nextval = None
        else: 
            prev.nextval = temp.nextval
        
    
    def readFile(self, name):
        printval = self.headval #checks for whether head of linked list is null
        while (printval.giveID != name): #iterates through list
            print ("Searching...") #print node's data
            printval = printval.nextval

            if (printval.nextval is None): 
                print("Can't find the file as it doesn't exist")
                return
        return printval
        
if __name__ == "__main__": #main method
    #user input
    inp = input("Type in storageDevice's size in MB. Leave empty for default (1MB or 1024 blocks of 1KB)...if 1 or 0 is entered, it will default to 1MB \n")
    if (int(inp) > 1):
        storageSize = int(inp) * 1024 - 1 #max number of blocks in file system
    else:
        storageSize = 1023 #max number of blocks in file system
        
    blockList = FileSystem() #instantiate the filesystem as an object containing x block (STEP1)
    
    blockList.remaining = storageSize #instants size of filesystem
    print("Total Storage in 1 KB blocks: {}".format(storageSize+1))
    print("creating default memory...using up 1 block automatically") #creates default undeletable storage block
    blockList.headval = File("defaultHeadNode", 1024) #set the defaultHEAD value
    print("Available 1KB Blocks: {}".format(blockList.remaining))
    
    print("Select 1 for SaveFile \nSelect 2 for DeleteFile \nSelect 3 for ReadFile \nSelect 4 for PrintAllFiles")
    inpMenu = input("(Type 'Exit' to Exit)")
    clear()
    while (inpMenu != "Exit"):
        clear() 

        if (inpMenu == "1"):
            #save
            while True:
                inpFileName = input("Please input Filename (it will be your giveID) \n**Typing the Name of Existing File will Overwrite it!** \n(Type 'No' to Stop Saving)")
                if (inpFileName == "No"):
                    break

                inpByte = input("Please input the file's size in Bytes (Int Only) \n")
                clear() 

                if(inpByte == "0"):
                    print("Since size was not selected, default saving to 1KB block")
                    inpByte = 1024
                
                blockList.deleteFile(inpFileName) # deletes if the node already exists else prints node doesn't exist
                blockList.saveFile(inpFileName, int(inpByte))
                print("Update: Available Blocks: {}".format(blockList.remaining))
            clear() 
                
        elif (inpMenu == "2"):
            #delete
            while True:
                inpFileName = input("Please input the giveID) to Delete \n(Type 'No' to Exit)")
                if (inpFileName == "No"):
                    break
                delete = blockList.deleteFile(inpFileName)
                if (delete == False):
                    print("Can't delete the file as it doesn't exist") 
                
                print("File deleted") 
                print("Update: Available Blocks: {}".format(blockList.remaining))
            clear() 
    
        elif (inpMenu == "3"):
            #read
            while True:
                print("Available Blocks: {}".format(blockList.remaining))
                inpFileName = input("Please input the giveID/filename to view its data \n(Type 'No' to Exit)")
                if (inpFileName == "No"):
                    break
                selectFile = blockList.readFile(inpFileName)
                if (selectFile != None):
                    print("FileName/GiveID      Size        Blocks Used")
                    print("{}           {}           {}".format(selectFile.giveID, selectFile.size, selectFile.blockNumber()))
            clear() 

        elif (inpMenu == "4"):
            #printAll   
            while True:    
                blockList.printAllFiles() #print out all existing files
                inpFileName = input("(Type 'No' to Exit)")
                if (inpFileName == "No"):
                    clear() 
                    break
                #prints number of used nodes currently in the linkedlist
                nodeNumber = blockList.countNodes(blockList.headval) #takes in headval of linkedlist
                        
                print("Number of Files in the System: {}".format(nodeNumber)) #how many nodes are in use 
                clear() 
            
        else:
            clear()
            print("Incorrect Input dummy ;P")
            
        print("Select 1 for SaveFile \nSelect 2 for DeleteFile \nSelect 3 for ReadFile \nSelect 4 for PrintAllFiles")
        inpMenu = input("(Type Exit to Exit)")

    print("End...")
   
    