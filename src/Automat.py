from PrzechowywaczMonet import PrzechowywaczMonet
from decimal import *

getcontext().prec = 3


class Automat(PrzechowywaczMonet):
    '''Class that helps me to do everyting around tickets'''
    avaiableTickets = {
        "Bilet ulgowy20m": 2.20,
        "Bilet ulgowy40m": 4.70,
        "Bilet ulgowy60m": 7.50,
        "Bilet 20m": 3.70,
        "Bilet 40m": 6.20,
        "Bilet 60m": 10.2
    }

    ticketsPrice = 0

    def __init__(self):
        super().__init__()

    def addTicket(self, ticket, amount=1):
        self.ticketsPrice = Decimal(self.ticketsPrice + Decimal(self.avaiableTickets[str(ticket)]) * amount)

    def showCostOfTickets(self):
        print("total cost of tickets :", self.ticketsPrice)

    def remainderCalculator(self, userCoinContainer):
        '''Method that calculates the change when user paid more than he should for a ticket'''
        getcontext().prec = 3
        self.ticketsPrice = Decimal(self.ticketsPrice)
        sumOfUsersCoins = userCoinContainer.sumaMonet()
        returnList = []
        if self.ticketsPrice > sumOfUsersCoins:
            return None
        if self.ticketsPrice == sumOfUsersCoins:
            self.lista_monet = self.lista_monet + userCoinContainer.lista_monet
            return returnList

        elif self.ticketsPrice < sumOfUsersCoins:
            self.lista_monet = self.lista_monet + userCoinContainer.lista_monet
            remainder = userCoinContainer.sumaMonet() - self.ticketsPrice
            self.lista_monet.sort(reverse=True)
            for value in self.lista_monet:
                value = Decimal(value)
                remainder = Decimal(remainder)
                if value == remainder:
                    remainder -= value
                    returnList.append(value)
                elif remainder - value > 0:
                    remainder = Decimal(remainder - value)
                    returnList.append(value)
                if remainder == 0:
                    return returnList

            if Decimal(sum(returnList)) != Decimal(sumOfUsersCoins - self.ticketsPrice):
                for coin in userCoinContainer.lista_monet:
                    if coin in self.lista_monet:
                        self.lista_monet.remove(coin)
                return userCoinContainer.lista_monet