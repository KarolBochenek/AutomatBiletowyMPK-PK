

from tkinter import messagebox
from src.PrzechowywaczMonet import PrzechowywaczMonet
from exception.BrakWybranegoBiletu import BrakWybranegoBiletu
from exception import BrakMonetDoWydania
from exception.NiewlasciwaIloscBiletow import NiewlasciwaIloscBiletow
from exception import NiewlasciwaIloscMonet
from src.Automat import Automat
from tkinter import *
from decimal import *


def showFrame(frame):
    frame.tkraise()


def resetState():
    '''method that prepares the program after someone bought the ticket it checks that user list of coins is empty after
    it was added to the ticket machine'''
    userCoinContainer.lista_monet = []
    ticketMachine.ticketsPrice = 0


class StartPage(Frame):
    '''class that starts the program gives some coins to the ticket machine so its not empty it initiates the other classes '''
    global userCoinContainer
    global ticketMachine
    userCoinContainer = PrzechowywaczMonet()
    ticketMachine = Automat()

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        additionalCoins = ["0.01", "0.01", "0.02", "0.05", "0.1", "0.1", "0.1", "0.1", "0.1", "0.1", "0.2", "0.5", "1",
                           "2",
                           "5"]
        ticketMachine.lista_monet += list(map(Decimal, additionalCoins))  # STARTOWE MONETY DLA AUTOMATU
        global pageOne
        pageOne = PageOne()


class PageOne(Frame):
    '''first page of ticket machine conatain buttons entries ,methods connected with adding tickets '''

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        '''mesh ,entries configuration '''
        self.grid(row=0, column=0, sticky="NSEW")
        entries = []
        entry1 = StringVar()
        entry2 = StringVar()
        entry3 = StringVar()
        entry4 = StringVar()
        entry5 = StringVar()
        entry6 = StringVar()
        entry1.set(0)
        entry2.set(0)
        entry3.set(0)
        entry4.set(0)
        entry5.set(0)
        entry6.set(0)
        E1 = Entry(self, bd=5, textvariable=entry1)
        E1.grid(row=0, column=1)
        E2 = Entry(self, bd=5, textvariable=entry2)
        E2.grid(row=1, column=1)
        E3 = Entry(self, bd=5, textvariable=entry3)
        E3.grid(row=2, column=1)
        E4 = Entry(self, bd=5, textvariable=entry4)
        E4.grid(row=3, column=1)
        E5 = Entry(self, bd=5, textvariable=entry5)
        E5.grid(row=4, column=1)
        E6 = Entry(self, bd=5, textvariable=entry6)
        E6.grid(row=5, column=1)

        entries.append(E1)
        entries.append(E2)
        entries.append(E3)
        entries.append(E4)
        entries.append(E5)
        entries.append(E6)
        entries.append(entry1)
        entries.append(entry2)
        entries.append(entry3)
        entries.append(entry4)
        entries.append(entry5)
        entries.append(entry6)

        def ticketsAdder():
            '''Method that is checking for proper amount of tickets,adds the tickets to the record starts the process of migration to the second page '''
            i = 0
            for ticket in ticketMachine.avaiableTickets:
                try:
                    amount = int(entries[i].get())
                    if amount > 0:
                        ticketMachine.addTicket(ticket, amount)
                    elif amount < 0:
                        # ticketMachine.ticketsPrice = 0
                        entries[6 + i].set("0")
                        raise NiewlasciwaIloscBiletow()
                except ValueError:
                    # ticketMachine.ticketsPrice = 0
                    raise NiewlasciwaIloscBiletow()
                entries[6 + i].set("0")
                i += 1

            if ticketMachine.ticketsPrice == 0:
                raise BrakWybranegoBiletu()
            ticketMachine.showCostOfTickets()
            pageTwo = PageTwo()
            showFrame(pageTwo)

        i = 0
        for ticket in ticketMachine.avaiableTickets:
            Label(self, text=str(ticket) + "   cena  " + str(ticketMachine.avaiableTickets[str(ticket)]), height=1,
                  width=30, font=10) \
                .grid(row=i, column=0)

            Button(self, text="dodaj", command=ticketsAdder, height=1, width=10, font="16") \
                .grid(row=i, column=2)

            i += 1


class PageTwo(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        '''mesh setup ,entry setup'''
        self.grid(row=0, column=0, sticky="NSEW")

        amountOfCoins = StringVar()
        entryAmountOfCoins = Entry(self, bd=5, textvariable=amountOfCoins, width=5, font=16)
        entryAmountOfCoins.grid(row=3, column=4, columnspan=4, sticky="nsew")
        amountOfCoins.set(1)
        '''button and labels placement '''
        i = 0
        for coin in userCoinContainer._monety_dostepne_lista:
            Button(self, text=coin,
                   command=lambda coin=coin: userCoinContainer.addCoin(coin, userCoinContainer.potwierdzIlosc(
                       entryAmountOfCoins.get())),
                   height=2, width=4, font=16) \
                .grid(row=1, column=i, sticky="nsew")
            i += 1
        addTxt = "dodaj monete klikając , do zapłaty " + str(
            (ticketMachine.ticketsPrice - userCoinContainer.sumaMonet()))
        labelDodaj = Label(self, text=addTxt, height=2, width=30, font=16) \
            .grid(row=0, column=2, columnspan=8, sticky="nsew")

        labelDodaj = Label(self, text="ilość", height=0, width=6, font=10) \
            .grid(row=3, column=2, columnspan=2, sticky="nsew")

        Button(self, text="czy chcesz dodać kolejne bilety?", command=lambda: showFrame(pageOne), height=2, width=20) \
            .grid(row=5, column=4, columnspan=4, sticky="nsew")

        Button(self, text="Zakończ transakcje", command=lambda: finishTransaction(), height=2, width=10). \
            grid(row=6, column=4, columnspan=4, sticky="nsew")

        def finishTransaction():
            '''method that  passes the amount of coins and checks for the remainder'''
            returnList = ticketMachine.remainderCalculator(userCoinContainer)
            if returnList is None:
                return
            elif sum(returnList) == 0:
                info = "Dziękujemy za transakcję"
            elif returnList == userCoinContainer.lista_monet:
                info = "Tylko odliczona kwota \n" + str(
                    ",".join([str(float(x)) for x in returnList]))
            else:
                info = "Reszta \n" + str(
                    ",".join([str(float(x)) for x in returnList]))
            printChange(info)

        def printChange(info):
            '''prints info after program calculated change and resets its state'''
            messagebox.showinfo("", info)
            showFrame(pageOne)
            resetState()
