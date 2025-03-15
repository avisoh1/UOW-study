# Design pattern
# Strategy pattern

class ToyMachine:
    OUT_OF_STOCK = 0
    IDLE = 1
    HAS_COIN = 2

    def __init__(self,amount = 0):
        self.__state = type(self).OUT_OF_STOCK
        self.__stock = amount
        if self.__stock > 0:
            self.__state = type(self).IDLE
    
    @property
    def stock(self):
        return self.__stock
    
    @property
    def state(self):
        return self.__state
    
    def dispense(self,qty=1):
        self.__stock -= 1

    def insertCoin(self):
        if self.__state == type(self).OUT_OF_STOCK:
            print("You can't insert coin, machine is out of stock!")
        elif self.__state == type(self).IDLE:
            print("You inserted a coin.")
            self.__state = type(self).HAS_COIN
        elif self.__state == type(self).HAS_COIN:
            print("You can't insert another coin!")

    def ejectCoin(self):
        if self.__state == type(self).OUT_OF_STOCK:
            print("You can't eject your coin, you haven't inserted one yet!")
        elif self.__state == type(self).IDLE:
            print("You can't eject your coin, you haven't inserted one yet!")
        elif self.__state == type(self).HAS_COIN:
            print("Coin returned")
            self.__state == type(self).IDLE

    def turnCrank(self):
        if self.__state == type(self).OUT_OF_STOCK:
            print(".....")
        elif self.__state == type(self).IDLE:
            print(".....")
        elif self.__state == type(self).HAS_COIN:
            self.dispense()         # default is 1
            print("Toy dispensed. Enjoy")
            if self.__stock > 0:
                self.__state = type(self).IDLE
            else:
                self.__state = type(self).OUT_OF_STOCK
    
    def restock(self,amount):
        if self.__state == type(self).OUT_OF_STOCK:
            self.__stock = amount
            if self.__stock > 0:
                self.__state = type(self).IDLE
        elif self.__state == type(self).IDLE:
            self.__stock += amount
        elif self.__state == type(self).HAS_COIN:
            print("You can't restock while a customer is buying a toy!")

def main():
    tm = ToyMachine(10)
    print(tm.state,tm.stock)        # 1     10
    tm.insertCoin()
    print(tm.state,tm.stock)        # 2     10
    tm.turnCrank()
    print(tm.state,tm.stock)        # 1     9
    tm.insertCoin()
    print(tm.state,tm.stock)        # 2     9
    tm.turnCrank()
    print(tm.state,tm.stock)        # 1     8
    tm.restock(10)
    print(tm.state,tm.stock)        # 1     18
    tm.insertCoin()
    print(tm.state,tm.stock)        # 2     18
    tm.ejectCoin()                  # 1     18
    tm.turnCrank()                  # cannot!!
    print(tm.state,tm.stock)        # 1     18


# Strategy Pattern with WINNER
from random import randint

class ToyMachine:
    OUT_OF_STOCK = 0
    IDLE = 1
    HAS_COIN = 2
    WINNER = 3

    def __init__(self,amount = 0):
        self.__state = type(self).OUT_OF_STOCK
        self.__stock = amount
        if self.__stock > 0:
            self.__state = type(self).IDLE
    
    @property
    def stock(self):
        return self.__stock
    
    @property
    def state(self):
        return self.__state
    
    def dispense(self,qty=1):
        self.__stock -= qty

    def getWinner(self):
        return (randint(1,5)==1)  # 20% chance

    def insertCoin(self):
        if self.__state == type(self).OUT_OF_STOCK:
            print("You can't insert coin, machine is out of stock!")
        elif self.__state == type(self).IDLE:
            print("You inserted a coin.")
            if self.getWinner() and self.__stock >= 2:
                self.__state = type(self).WINNER
            else:
                self.__state = type(self).HAS_COIN
        elif self.__state == type(self).HAS_COIN or \
            self.__state == type(self).WINNER:
            print("You can't insert another coin!")

    def ejectCoin(self):
        if self.__state == type(self).OUT_OF_STOCK:
            print("You can't eject your coin, you haven't inserted one yet!")
        elif self.__state == type(self).IDLE:
            print("You can't eject your coin, you haven't inserted one yet!")
        elif self.__state == type(self).HAS_COIN or \
            self.__state == type(self).WINNER:
            print("Coin returned")
            self.__state == type(self).IDLE

    def turnCrank(self):
        if self.__state == type(self).OUT_OF_STOCK:
            print(".....")
        elif self.__state == type(self).IDLE:
            print(".....")
        elif self.__state == type(self).HAS_COIN:
            self.dispense()         # default is 1
            print("Toy dispensed. Enjoy")
            if self.__stock > 0:
                self.__state = type(self).IDLE
            else:
                self.__state = type(self).OUT_OF_STOCK
    
    def restock(self,amount):
        if self.__state == type(self).OUT_OF_STOCK:
            self.__stock = amount
            if self.__stock > 0:
                self.__state = type(self).IDLE
        elif self.__state == type(self).IDLE:
            self.__stock += amount
        elif self.__state == type(self).HAS_COIN or \
            self.__state == type(self).WINNER:
            print("You can't restock while a customer is buying a toy!")

def main():
    tm = ToyMachine(10)
    print(tm.state,tm.stock)        # 1     10
    tm.insertCoin()
    print(tm.state,tm.stock)        # 2     10
    tm.turnCrank()
    print(tm.state,tm.stock)        # 1     9
    tm.insertCoin()
    print(tm.state,tm.stock)        # 2     9
    tm.turnCrank()
    print(tm.state,tm.stock)        # 1     8
    tm.restock(10)
    print(tm.state,tm.stock)        # 1     18
    tm.insertCoin()
    print(tm.state,tm.stock)        # 2     18
    tm.ejectCoin()                  # 1     18
    tm.turnCrank()                  # cannot!!
    print(tm.state,tm.stock)        # 1     18

# State Pattern
from abc import ABC, abstractmethod

class TMState(ABC):
    def __init__(self,context):
        self.__context = context    # the toy machine
    
    @property
    def context(self):
        return self.__context
    
    @context.setter
    def context(self,newcontext):
        self.__context = newcontext
    
    @abstractmethod
    def insertCoin(self):
        pass

    @abstractmethod
    def ejectCoin(self):
        pass

    @abstractmethod
    def turnCrank(self):
        pass

    @abstractmethod
    def restock(self):
        pass

class IdleState(TMState):
    def __init__(self,context):
        super().__init__(context)
    
    def insertCoin(self):
        print("You inserted a coin.")
        self.context.state = HasCoinState(self.context)
        return self.context.state
    
    def ejectCoin(self):
        print("You can't eject your coin, you haven't inserted one yet!")
        return self.context.state
    
    def turnCrank(self):
        print("You can't turn the crank, you haven't inserted a coin yet!")
        return self.context.state
    
    def restock(self):
        self.context.addStock(amount)
        return self.context.state

class HasCoinState(TMState):
    def __init__(self, context):
        super().__init__(context)
    
    def insertCoin(self):
        print("You can't inserted another coin!")
        return self.context.state
    
    def ejectCoin(self):
        print("Coin returned")
        self.context.state = IdleState(self.context)
        return self.context.state
    
    def turnCrank(self):
        self.context.dispense(1)
        print("Toy dispensed. Enjoy!")
        if self.context.stock > 0:
            self.context.state = IdleState(self.context)
        else:
            self.context.state = OutOfStockState(self.context)
        return self.context.state
    
    def restock(self,amount):
        print("You can't restock while a customer is buying a toy.")
        return self.context.state

class OutOfStockState(TMState):
    def __init__(self, context):
        super().__init__(context)
    
    def insertCoin(self):
        print("You can't insert another coin, machine is out of stock!")
        return self.context.state
    
    def ejectCoin(self):
        print("You can't eject your coin, you haven't inserted one yet!")
        return self.context.state
    
    def turnCrank(self):
        print("You can't turn the crank, the machine is empty.")
        return self.context.state
    
    def restock(self,amount):
        self.context.addStock(amount)       
        if self.context.stock > 0:
            self.context.state = IdleState(self.context)
        return self.context.state

class ToyMachine:
    def __init__(self,amount=0):                # tm = ToyMachine(10)
        self.__stock = amount
        if self.__stock > 0:
            self.__state = IdleState(self)      # pass ToyMachine object to TMState object
        else:
            self.__state = OutOfStockState(self)

    @property
    def stock(self):
        return self.__stock
    
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self,aState):
        self.__stock = aState
    
    def addStock(self,amount):
        self.__stock += amount
    
    def dispense(self,qty):
        self.__stock -= qty
    
    def insertCoin(self):
        self.__state = self.__state.insertCoin()

    def ejectCoin(self):
        self.__state = self.__state.ejectCoin()

    def turnCrank(self):
        self.__state = self.__state.turnCrank()

    def restock(self,amount):
        self.__state = self.__state.restock(amount)     

def main():
    tm = ToyMachine(5)
    print(tm.state,tm.stock)        # 1     10
    tm.insertCoin()
    print(tm.state,tm.stock)        # 2     10
    tm.turnCrank()
    print(tm.state,tm.stock)        # 1     9
    tm.insertCoin()
    print(tm.state,tm.stock)        # 2     9
    tm.turnCrank()
    print(tm.state,tm.stock)        # 1     8
    tm.restock(10)
    print(tm.state,tm.stock)        # 1     18
    tm.insertCoin()
    print(tm.state,tm.stock)        # 2     18
    tm.ejectCoin()                  # 1     18
    tm.turnCrank()                  # cannot!!
    print(tm.state,tm.stock)        # 1     18

# Obeserver Pattern
from abc import ABC,abstractmethod

class Subject(ABC):
    @abstractmethod
    def registerObserver(self,observer):
        pass

    @abstractmethod
    def removeObserver(self,observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self,dataInterested):
        pass

###############################################

class CompanyStock(Subject):
    def __init__(self,stockName,initialPrice):
        self.__observers = [] # /{}
        self.__name = stockName
        self.currentPrice = initialPrice

    @property
    def currentPrice(self):
        return self.__currentPrice
    
    @currentPrice.setter
    def currentPrice(self,newPrice):
        self.__currentPrice = newPrice
        self.notifyObservers()      # run this method to inform my followers

    def registerObserver(self,observer):
        #if observer.name not in self.__observers.keys()
        #   self.__observers[observer.name] = observer
        if observer not in self.__observers:
            self.__observers.append(observer)
    
    def removerObserver(self,name):
        #if name in self.__observers.keys():
        #del self.__observers[name]
        for obs in self.__observers:
            if obs.name == name:
                self.__observers.remove(obs)
                return
    
    def notifyObservers(self):
        #for obs in self.__observers.values():
        #   obs.update([self.__name,self.__currentPrice])
        for obs in self.__observers:
            obs.update([self.__name,self.__currentPrice])

class Customer(Observer):
    def __init__(self,name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    def update(self, dataInterested):
        print("I am {} ==> {}'s new price ${:.2f}".\
              format(self.__name,dataInterested[0],dataInterested[1]))

def main():
    aCompanyStock = CompanyStock("Apple",227.80)
    bCompanyStock = CompanyStock("Orange",10.89)
    m = Customer("Mary")
    j = Customer("John")
    c = Customer("Charlie")
    aCompanyStock.registerObserver(m)
    aCompanyStock.registerObserver(c)
    aCompanyStock.registerObserver(j)
    bCompanyStock.registerObserver(m)
    bCompanyStock.registerObserver(c)

    print("Updating apple to 237.99")
    # Using property
    aCompanyStock.currentPrice = 237.99

    print("Updating orange to 10.82")
    bCompanyStock.currentPrice = 10.82

    aCompanyStock.removeObserver(c.name)
    print("Updating apple to 217.66")
    aCompanyStock.currentPrice = 217.66

main()