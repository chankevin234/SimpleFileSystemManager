#imported libraries
import sys
import math

class File: #1 1KB Block
    def __init__(self, fileName=str): #constructor "", size=int" 
        self.fileName = fileName # the name data
        # self.size = size
        self.nextval = None # the reference to the next node
        
    # def validate(self):
    #     fileSize = self.size
    #     if (fileSize > 1024):
    #         print(self.fileName + " is too big for 1 block")
    #         blocks = math.ceil(fileSize / 1024)
    #         print("OS needs to use these many blocks: {}".format(blocks))

class FileSystem: #file system linked list
    
    def __init__(self): #constructor
        self.headval = None #set the head value of this linked list as null initially
    
    def countNodes(self, head): #counts the # of nodes in the list takes in the head value of blockList
        count = 1 # assuming that head != None
        current = head
        while current.nextval is not None: #keep printing if there exists another following block
            current = current.nextval
            count += 1
        return count

    def printAllFiles(self): #prints out the list of nodes in linkedList
        printval = self.headval #checks for whether head of linked list is null
        while printval is not None: #iterates through list
            print (printval.fileName) #print node
            printval = printval.nextval #append block connected to head
    
    def saveFile(self, newFile): #saves a file to end of the linked list , size=int
        newBlock = File(newFile) #sets value for newBlock
        newBlock.nextval = self.headval #sets the following block to be the head (adds to front of the list)
        self.headval = newBlock #sets the new head value of the linked list to newBlock
        return

    def deleteFile(self, removeKey): #removes file based on the removekey
        temp = self.headval 
        prev = self.headval 
        if temp.fileName == removeKey: 
            if temp.nextval is None or temp.fileName == 'defaultHeadNode': 
                print("Can't delete the node as it has only one node") #prevents user from deleting all nodes in the linked list
            else: 
                temp.fileName = temp.nextval.fileName 
                temp.nextval = temp.nextval.nextval
            return
        while temp.nextval is not None and temp.fileName != removeKey: 
            prev = temp 
            temp = temp.nextval
        if temp.nextval is None and temp.fileName != removeKey: 
            print("Can't delete the node as it doesn't exist") 
         # If node is last node of the linked list 
        elif temp.nextval is None and temp.fileName == removeKey: 
            prev.nextval = None
        else: 
            prev.nextval = temp.nextval

    def readFile(self, name):
        printval = self.headval #checks for whether head of linked list is null

        while (printval.fileName != name): #iterates through list
            print ("Searching...") #print node's data
            printval = printval.nextval
            if printval.nextval is None: 
                print("Can't delete the node as it doesn't exist")
                return
        print(printval.fileName)
        return 
        

if __name__ == "__main__": #main method
    #user input
    inp = input("Type anything: leave empty for default 100 blocks \n")
    if (inp): 
        storageSize = inp #max number of nodes in file system
    else:
        storageSize = 100 #max number of nodes in file system
        
    blockList = FileSystem() #instantiate the filesystem as an object containing x block (STEP1)
    print("creating default storage block")
    blockList.headval = File("defaultHeadNode") #set the HEAD value
    # e2 = File("Node2") #set node 2 as Tue, 1000 bytes
    # e3 = File("Node3") #set node 3 as Wed, 10 bytes
    # blockList.headval.nextval = e2 # appends first Node to second node
    # e2.nextval = e3 # appends second Node to third node
    print("creating first 7 Nodes")
    blockList.saveFile("Node2")
    blockList.saveFile("Node3")
    blockList.saveFile("Node4")
    blockList.saveFile("Node5")
    blockList.saveFile("Node6")
    blockList.saveFile("Node7")
    print("deleting default storage block")
    blockList.deleteFile("defaultHeadNode")
    print("deleting node5")
    blockList.deleteFile("Node5")
    print("deleting node7")
    blockList.deleteFile("Node7")

    #print out all existing files
    blockList.printAllFiles()
    # e2.validate()
    blockList.readFile("Node7")
    
    #prints number of used nodes currently in the linkedlist
    try:
        nodeNumber = blockList.countNodes(blockList.headval) #takes in headval of linkedlist
    except:
        nodeNumber = 100        
    print("{} out of {} used".format(nodeNumber, storageSize)) #how many nodes are in use 
    
   
    