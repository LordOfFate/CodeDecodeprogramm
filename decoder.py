class list:

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
            self.head = self.node(elment)
        else:
            current = self.head

            while current.next_element != None:
                current = current.next_element

            current.next_element = self.node(elment)

    def allOut(self):
        current = self.head
        while current.next_element == None:
            print(current.element, ' |--> ', current.zeroAddElement, ' ', current.oneAddElement)
            current = current.next_element
        print(current.element, ' |--> ', current.zeroAddElement, ' ', current.oneAddElement)

    def addChain(self, element, ChainZeroElement, ChainOneElement, ZeroAddElement, OneAddElement):
        current = self.head
        currentIter = self.head
        while current != element:
            curret = current.next_element
        while currentIter != ChainZeroElement:
            curretIter = current.next_element
        current.zeroAddElement = curretIter
        while currentIter != ChainOneElement:
            curretIter = current.next_element
        current.oneAddElement = curretIter
        current.ZeroAdd = ZeroAddElement
        current.OneAdd = OneAddElement
