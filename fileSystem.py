#imported libraries
import math

class Block: #1 1KB Block
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
        while current.nextval is not None:
            current = current.nextval
            count += 1
        return count

    def printList(self): #prints out the list of nodes in linkedList
        printval = self.headval #checks for whether head of linked list is null
        while printval is not None: #iterates through list
            print (printval.fileName) #print node
            printval = printval.nextval #append block connected to head
    
    def saveFile(self, newName): #saves a file to end of the linked list , size=int
        newBlock = Block(newName) #sets value for newBlock
        if self.headval is None: #checks to see if head value exists in the linked list; if not, make the newblock the new head
            self.headval = newBlock
            return

        current = self.headval # sets the head as new lastBlock
        while(current.nextval): # iterates through linked list and assigns last block to following node until there is a node with no following node 
            current = current.nextval # sets this empty spot after current node as the new last block
        current.nextval = newBlock # creates a new block in the empty spot
    
    def deleteFile(self, removeName):
        HeadVal = self.headval

        if (HeadVal is not None):
            if (HeadVal.fileName == removeName):
                self.head = HeadVal.nextval
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.fileName == removeName:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if (HeadVal == None):
            return

        prev.next = HeadVal.nextval

        HeadVal = None


if __name__ == "__main__": #main method
    
    #user input
    inp = input("Type anything: leave empty for default 100 \n")
    if (inp): 
        storageSize = inp #max number of nodes in file system
    else:
        storageSize = 100 #max number of nodes in file system
        
    blockList = FileSystem() #instant the filesystem as an object containing x block (STEP1)
    blockList.headval = Block("defaultHeadNode") #set the HEAD value
    e2 = Block("Node2") #set node 2 as Tue, 1000 bytes
    e3 = Block("Node3") #set node 3 as Wed, 10 bytes

    
    blockList.headval.nextval = e2 # appends first Node to second node
    e2.nextval = e3 # appends second Node to third node
    blockList.saveFile("Node4")
    blockList.deleteFile("Node2")
    #print out all blocks
    blockList.printList()
    # e2.validate()
    
    #prints number of used nodes in the list
    try:
        nodeNumber = blockList.countNodes(blockList.headval) #takes in headval of linkedlist
    except:
        nodeNumber = 100        
    print("{} out of {} used".format(nodeNumber, storageSize)) #how many nodes are in use 
    
   
    