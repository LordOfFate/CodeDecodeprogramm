class list:

    class node:
        element = None
        first_bit = False
        secnd_bit = False
        third_bit = False
        forth_bit = False
        next_node = None

        def __init__(self, element, first_bit, secnd_bit, thirst_bit, forth_bit, next_node = None):
            self.element = element
            self.first_bit = first_bit
            self.secnd_bit = secnd_bit
            self.third_bit = thirst_bit
            self.forth_bit = forth_bit
            self.next_node = next_node

    sithe = 0
    head = node

    def add_node(self, element, first_bit, secnd_bit, thirst_bit, forth_bit):
        self.sithe = self.sithe + 1
        if self.head.element == None:
            self.head = self.node(element, first_bit, secnd_bit, thirst_bit, forth_bit)
        else:
            current = self.head

            while current.next_node != None:
                current = current.next_node

            current.next_node = self.node(element, first_bit, secnd_bit, thirst_bit, forth_bit)


    def all_out(self):
        current = self.head
        while current.next_node != None:
            print(current.element, current.first_bit, current.secnd_bit, current.third_bit, current.forth_bit)
            current = current.next_node
        print(current.element, current.first_bit, current.secnd_bit, current.third_bit, current.forth_bit)

    def ask_node(self, element, bit):
        if self.head.element == element:             
             if bit == 1:
                 return self.head.first_bit
             elif bit == 2:
                 return self.head.secnd_bit
             elif bit == 3:
                 return self.head.third_bit
             elif bit == 4:
                 return self.head.forth_bit
        else:
            current = self.head

            while current.element != element:
                current = current.next_node

            if bit == 1:
                 return current.first_bit
            elif bit == 2:
                 return current.secnd_bit
            elif bit == 3:
                 return current.third_bit
            elif bit == 4:
                 return current.forth_bit
    def sizeOut(self):
        return self.sithe

def generate_list():
    return list()
def add_element(list, element, first_bit, secnd_bit, thirst_bit, forth_bit):
    list.add_node(element, first_bit, secnd_bit, thirst_bit, forth_bit)
def ask_element(list, element, bit):
    return list.ask_node(element, bit)
def size(list):
    return list.sithe
def out(list):
    list.all_out()
def size_Out(list):
    return list.sizeOut()