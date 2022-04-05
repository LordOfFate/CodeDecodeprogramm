class DecodTab:

    class node:
        element = None
        next_element = None
        ZeroAdd = None
        OneAdd = None
        oneAddElement = None
        zeroAddElement = None

        def __init__(self, element, next_element = None):
            self.element = element
            self.next_element = next_element

    head = node

    def addNode(self, element):
        if self.head.element == None:
            self.head = self.node(element)
        else:
            current = self.head

            while current.next_element != None:
                current = current.next_element

            current.next_element = self.node(element)

    def allOut(self):
        current = self.head
        while current.next_element != None:
            print(current.element, ' |--> ', current.zeroAddElement, ' ', current.oneAddElement)
            current = current.next_element
        print(current.element, ' |--> ', current.zeroAddElement, ' ', current.oneAddElement)

    def addChain(self, element, ChainZeroElement, ChainOneElement, ZeroAddElement = None, OneAddElement = None):
        current = self.head
        currentIter = self.head
        if current != element:
            while current != element:
                print(1)
                curret = current.next_element
        if currentIter != ChainZeroElement:
            while currentIter != ChainZeroElement:
                print(2)
                curretIter = current.next_element
        current.zeroAddElement = curretIter
        if currentIter != ChainOneElement:
            while currentIter != ChainOneElement:
                print(3)
                curretIter = current.next_element
        current.oneAddElement = curretIter
        current.ZeroAdd = ZeroAddElement
        current.OneAdd = OneAddElement

def GenerateDecoderTab():
    return DecodTab()
def GenerateNode(List, element):
    List.addNode(element)
def GenerateChains(List, element, ChainZeroElement, CahinOneElement, ZeroAddElement = None, OneAddElement = None):
    List.addChain(element, ChainZeroElement, CahinOneElement, ZeroAddElement, OneAddElement)
def OutAllTabElement(List):
    List.allOut()
