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
            print(current.element, ' |--> ', current.ZeroAdd.element, ' ', current.OneAdd.element)
            current = current.next_element
        print(current.element, ' |--> ', current.ZeroAdd.element, ' ', current.OneAdd.element)

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

def GenerateDecoderTab():
    return DecodTab()
def GenerateNode(List, element):
    List.addNode(element)
def ChainGenerate(List, element, ZeroChain, OneChain, ZeroElement = None, OneElement = None):
     List.MakeChaine(element, ZeroChain, OneChain, ZeroElement, OneElement)
def OutAllTabElement(List):
    List.allOut()

Tab = GenerateDecoderTab()
GenerateNode(Tab, '000')
GenerateNode(Tab, '001')
GenerateNode(Tab, '010')
GenerateNode(Tab, '011')
GenerateNode(Tab, '100')
GenerateNode(Tab, '101')
GenerateNode(Tab, '110')
GenerateNode(Tab, '111')
ChainGenerate(Tab, '000', '000', '100')
ChainGenerate(Tab, '001', '000', '100')
ChainGenerate(Tab, '010', '001', '101')
ChainGenerate(Tab, '011', '001', '101')
ChainGenerate(Tab, '100', '010', '110')
ChainGenerate(Tab, '101', '010', '110')
ChainGenerate(Tab, '110', '011', '111')
ChainGenerate(Tab, '111', '011', '111')
OutAllTabElement(Tab)