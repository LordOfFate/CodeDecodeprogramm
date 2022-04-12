from tkinter import *
import coder
import decoder
import EncodTab

def DecodIt():
    Tab = decoder.GenerateDecoderTab()

    decoder.GenerateNode(Tab, '000')
    decoder.GenerateNode(Tab, '001')
    decoder.GenerateNode(Tab, '010')
    decoder.GenerateNode(Tab, '011')
    decoder.GenerateNode(Tab, '100')
    decoder.GenerateNode(Tab, '101')
    decoder.GenerateNode(Tab, '110')
    decoder.GenerateNode(Tab, '111')
    decoder.ChainGenerate(Tab, '000', '000', '100', AskForValue(False, False, False, False), AskForValue(True, False, False, False))
    decoder.ChainGenerate(Tab, '001', '000', '100', AskForValue(False, False, False, True), AskForValue(True, False, False, True))
    decoder.ChainGenerate(Tab, '010', '001', '101', AskForValue(False, False, True, False), AskForValue(True, False, True, False))
    decoder.ChainGenerate(Tab, '011', '001', '101', AskForValue(False, False, True, True), AskForValue(True, False, True, True))
    decoder.ChainGenerate(Tab, '100', '010', '110', AskForValue(False, True, False, False), AskForValue(True, True, False, False))
    decoder.ChainGenerate(Tab, '101', '010', '110', AskForValue(False, True, False, True), AskForValue(True, True, False, True))
    decoder.ChainGenerate(Tab, '110', '011', '111', AskForValue(False, True, True, False), AskForValue(True, True, True, False))
    decoder.ChainGenerate(Tab, '111', '011', '111', AskForValue(False, True, True, True), AskForValue(True, True, True, True))
    decoder.OutAllTabElement(Tab)

    InputData = DecodInputTxt.get()
    StepSize = coder.size_Out(sos)
    TheWay = []

    i = 0
    while i < len(InputData):
        TheWay.append(InputData[i:i+StepSize])
        i = i + StepSize

    CompliteText = decoder.OutTheTrueWay(Tab, TheWay)

    print(CompliteText)

    i = 0
    Plus = ''
    ComplitOutputMesseg = ''

    while i < len(CompliteText):
        Plus = EncodTab.decode(CompliteText[i:i + 8])
        ComplitOutputMesseg = ComplitOutputMesseg + Plus
        i = i + 8

    OutputDecodDataLbl.configure(text = ComplitOutputMesseg)

def AskForValue(firstRegester, secondRegester, therdRegester, forthRegester):

    Chank = ''

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

    return Chank

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
    OutLbl.configure(text = ComtliteText)

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
addButtonLbl = Label(window, text="Добавить сумматор")
addButtonLbl.grid(column=0, row=1)
first_bitlb = Label(window, text="Первый бит:")
first_bitlb.grid(column=0, row=2)
second_bitlb = Label(window, text="Второй бит:")
second_bitlb.grid(column=0, row=3)
third_bitlb = Label(window, text="Третий бит:")
third_bitlb.grid(column=0, row=4)
forth_bitlb = Label(window, text="Четвертый бит:")
forth_bitlb.grid(column=0, row=5)
OutLblLbl = Label(window, text="Свёрнутый код:")
OutLblLbl.grid(column=0, row=6)
OutLbl = Label(window)
OutLbl.grid(column=1, row=6)
InputDecodDataLbl = Label(window, text="Введите декодируемыйтекст:")
InputDecodDataLbl.grid(column=0, row=7)
OutputDecodDataLblLbl = Label(window, text="Декодированный текст:")
OutputDecodDataLblLbl.grid(column=0, row=8)
OutputDecodDataLbl = Label(window)
OutputDecodDataLbl.grid(column=1, row=8)

#Ввод данных
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
DecodInputTxt = Entry(window,width=10) 
DecodInputTxt.grid(column=1, row=7)

#Кнопки
butn = Button(window, text="Подтвердить", command = Pressed)
butn.grid(column=2, row=0)
add_butn = Button(window, text="Добавить сумматор", command = AddButonPress)
add_butn.grid(column=2, row=1)
DecodeBtn = Button(window, text="Декодировать", command = DecodIt)
DecodeBtn.grid(column=2, row=7)

window.mainloop()
