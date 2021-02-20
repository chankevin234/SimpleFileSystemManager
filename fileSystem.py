class Block: #1 1KB Block
    def __init__(self, dataval=str, size=int): #constructor 
        self.dataval = dataval
        self.size = size
        self.nextval = None
        
    def validate(self):
        fileSize = self.size
        if (fileSize > 1024):
            print(self.dataval + " is too big")
        

class FileSystem: #file system linked list
    #default props
    storageSize = 100 #max number of nodes in file system

    def __init__(self): #constructor
        self.headval = None #set the head value of this linked list as null initially

    def printList(self): #prints out the list of nodes in linkedList
        printval = self.headval #checks for whether head of linked list is null
        while printval is not None:
            print (printval.dataval, printval.size) #print node
            printval = printval.nextval #print block connected to head

    def count_nodes(self, head):
        # assuming that head != None
        count = 1
        current = head
        while current.nextval is not None:
            current = current.nextval
            count += 1
        return count

if __name__ == "__main__": #main method
    blockList = FileSystem() #instant the filesystem as an object containing x block (STEP1)
    blockList.headval = Block("System Data -- defaultNode", 10) #set the head value
    e2 = Block("Node2", 10000) #set node 2 as Tue
    e3 = Block("Node3", 10) #set node 3 as Wed

    # Link first Node to second node
    blockList.headval.nextval = e2

    # Link second Node to third node
    e2.nextval = e3

    #print out all blocks
    blockList.printList()
    e2.validate()
    # #user input
    # inp = input("Type anything") 

    # # prints inp 
    # print(inp) 


    try:
        nodeNumber = blockList.count_nodes(blockList.headval) #takes in headval of linkedlist
        print(nodeNumber)
    except Exception as e:
        print(e)
    