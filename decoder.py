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
            print(current.element, ' |--> ', current.ZeroAdd.element, ': ', current.zeroAddElement, ' ', current.OneAdd.element, ': ', current.oneAddElement)
            current = current.next_element
        print(current.element, ' |--> ', current.ZeroAdd.element, ': ', current.zeroAddElement, ' ', current.OneAdd.element, ': ', current.oneAddElement)

    def AskElement(self, element):
        current = self.head 
        while current.element != element:
            current = current.next_element
        return current

    def MakeChaine(self, element, ZeroChain, OneChain, ZeroElement = None, OneElement = None):
        current = self.AskElement(element)
        current.ZeroAdd = self.AskElement(ZeroChain)
        current.OneAdd = self.AskElement(OneChain)
        current.zeroAddElement = ZeroElement
        current.oneAddElement = OneElement

    def INowTheWay(self, way):
        current = self.head

        MyWay = ''

        i = 0

        while i < len(way):
            if way[i] == current.zeroAddElement:
                MyWay = MyWay + '0'
                current = current.ZeroAdd
            if way[i] == current.oneAddElement:
                MyWay = MyWay + '1'
                current = current.OneAdd
            i = i + 1
        return MyWay

def GenerateDecoderTab():
    return DecodTab()
def GenerateNode(List, element):
    List.addNode(element)
def ChainGenerate(List, element, ZeroChain, OneChain, ZeroElement = None, OneElement = None):
     List.MakeChaine(element, ZeroChain, OneChain, ZeroElement, OneElement)
def OutAllTabElement(List):
    List.allOut()
def OutTheTrueWay(List, way):
    return List.INowTheWay(way)

