from tkinter import *
import coder
import decoder
import EncodTab

def convertation(inputData):
    firstRegester = False
    secondRegester = False
    therdRegester = False
    forthRegester = False

    i = 0
    Chank = ''
    ComtliteText = ''
    while i < len(inputData):

        forthRegester = therdRegester
        therdRegester = secondRegester
        secondRegester = firstRegester
        if inputData[i] == '1':
            firstRegester = True
        else:
            firstRegester = False

        j = 1

        metka = coder.size_Out(sos)
        while j <= metka:
            OneChaizSize = 0
            if coder.ask_element(sos, j, 1) == True:
                if firstRegester == True:
                    OneChaizSize = OneChaizSize + 1
            if coder.ask_element(sos, j, 2) == True:
                if secondRegester == True:
                    OneChaizSize = OneChaizSize + 1
            if coder.ask_element(sos, j, 3) == True:
                if therdRegester == True:
                    OneChaizSize = OneChaizSize + 1
            if coder.ask_element(sos, j, 4) == True:
                if forthRegester == True:
                    OneChaizSize = OneChaizSize + 1
            if OneChaizSize%2 == 0:
                Chank = Chank + '0'
            else:
                Chank = Chank + '1'

            j = j + 1
        i = i + 1
        
        ComtliteText = ComtliteText + Chank
        Chank = ''
    print('После свертки:', ComtliteText)

def Pressed():
    i = 0

    sus = txt.get()

    pir = ''

    while i < len(txt.get()):
        pir = pir + EncodTab.encode(sus[i])
        i = i + 1

    print('До свертки: ', pir)
    convertation(pir)

sos = coder.generate_list()

def AddButonPress():
    coder.add_element(sos, (coder.size(sos) + 1), first_bit.get(), second_bit.get(), third_bit.get(), forth_bit.get())
    coder.out(sos)

window = Tk()
window.title("Решатель_кодовая версия")
window.geometry('400x250')

#Подписи
textlb = Label(window, text="Введите кодируемый текст:")
textlb.grid(column=0, row=0)
addButtonLbl = Label(window, text="сумматор 1")
addButtonLbl.grid(column=0, row=1)
first_bitlb = Label(window, text="Первый бит:")
first_bitlb.grid(column=0, row=2)
second_bitlb = Label(window, text="Второй бит:")
second_bitlb.grid(column=0, row=3)
third_bitlb = Label(window, text="Третий бит:")
third_bitlb.grid(column=0, row=4)
forth_bitlb = Label(window, text="Четвертый бит:")
forth_bitlb.grid(column=0, row=5)

#Ввод дфнных
#Флажки
first_bit = BooleanVar()
second_bit = BooleanVar()
third_bit = BooleanVar()
forth_bit = BooleanVar()

first_bit_box = Checkbutton(window, variable = first_bit, onvalue = True, offvalue = False)
second_bit_box = Checkbutton(window, variable = second_bit, onvalue = True, offvalue = False)
third_bit_box = Checkbutton(window, variable = third_bit, onvalue = True, offvalue = False)
forth_bit_box = Checkbutton(window, variable = forth_bit, onvalue = True, offvalue = False)

first_bit_box.grid(column=1, row=2)
second_bit_box.grid(column=1, row=3)
third_bit_box.grid(column=1, row=4)
forth_bit_box.grid(column=1, row=5)

#Ввод текстовых данных
txt = Entry(window,width=10)  
txt.grid(column=1, row=0) 

#Кнопки
butn = Button(window, text="Подтвердить", command = Pressed)
butn.grid(column=2, row=0)
add_butn = Button(window, text="Добавить сумматор", command = AddButonPress)
add_butn.grid(column=2, row=1)

window.mainloop()
