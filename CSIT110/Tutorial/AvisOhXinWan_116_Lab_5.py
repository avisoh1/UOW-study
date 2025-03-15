# Full Name: Avis Oh Xin Wan
# Tutorial Group: 1 (116)
# Objective: This is lab 5.
# File name: AvisOhXinWan_116_lab_5.py
#
# Declarations: This is my own program. I gave not passed my program to anyone in this class. If I do so, I accept any penalty of mark.

class PetrolPurchase:
    # Instance methods
    def __init__(self,station_location,quantity_purchase,petrol_type,price,percentage_discount):
        self.station_location = station_location
        self.quantity_purchase = quantity_purchase
        self.petrol_type = petrol_type
        self.price = price
        self.percentage_discount = percentage_discount

        # Other instance variables not in argument
        self.total_cost = self.get_total_cost ()
        self.total_discount = self.get_total_discount ()
        self.final_payment = self.get_final_payment ()

    # Accessor methods (getters)
    def get_station_location(self):
        return self.station_location

    def get_quantity_purchase(self):
        return self.quantity_purchase

    def get_petrol_type(self):
        return self.petrol_type

    def get_price(self):
        return self.price

    def get_percentage_discount(self):
        return self.percentage_discount

    # Mutator methods (setters)
    def set_station_location(self, station_location):
        self.station_location = station_location

    def set_quantity_purchase(self, quantity_purchase):
        self.quantity_purchase = quantity_purchase
        
    def set_petrol_type(self, petrol_type):
        self.petrol_type = petrol_type

    def set_price(self, price):
        self.price = price

    def set_percentage_discount(self, percentage_discount):
        self.percentage_discount = percentage_discount

    # This functions help to calculate the costs
    def get_total_cost(self):
        return self.quantity_purchase * self.price
    
    def get_total_discount(self):
        return self.get_total_cost() * (self.percentage_discount / 100)
    
    def get_final_payment(self):
        return self.get_total_cost() - self.get_total_discount()
    
    # Payment method
    def payment(self):
        # Recalculate the dependent values
        self.total_cost = self.get_total_cost()
        self.total_discount = self.get_total_discount()
        self.final_payment = self.get_final_payment()

    # str-method returns the information of instance variable
    def __str__ (self):
        s = "\tStation: {0}\n".format (self.station_location)
        s += "\tQuantity: {0:.2f}\n".format (self.quantity_purchase)
        s += "\tPetrol type: {0}\n".format (self.petrol_type)
        s += "\tUnit price: {0:.2f}\n".format(self.price)
        s += "\tDiscount: {0:.2f}%\n".format(self.percentage_discount)
        s += "\tTotal cost: ${0:.2f}\n".format(self.total_cost)
        s += "\tTotal discount ({0:.2f} %): $ {1:.2f}\n".format(self.percentage_discount,self.total_discount)
        s += "\tFinal payment: $ {0:.2f}\n".format(self.final_payment)
        return s

    # repr-method indicates how an object can be created
    def __repr__ (self):
        s = "\tPetrolPurchase (\"{0}\", {1:.1f}, \"{2}\", {3:.1f}, {4:.1f})".format (\
            self.station_location, self.quantity_purchase, self.petrol_type, self.price, self.percentage_discount)
        return  s

# This function helps to collect info from users
def inputInfo():
    station_location = input("Enter the station: ")
    quantity_purchase = float(input("Enter quantities in litres: "))
    petrol_type = input("Enter type of petrol: ")
    price = float(input("Enter price of petrol: "))
    percentage_discount = float(input("Enter discount: "))

    return station_location, quantity_purchase, petrol_type, price, percentage_discount

def main():
    # Collect all necessary information
    station_location, quantity_purchase, petrol_type, price, percentage_discount = inputInfo()

    s = PetrolPurchase(station_location, quantity_purchase, petrol_type, price, percentage_discount)

    # Print the summary of purchase
    print("\nSummary of purchase")
    print(s)

    # Add the quantity need to be added and print the final summary of purchase
    quantity = int(input("Enter additional quantity: "))
    s.quantity_purchase = s.quantity_purchase + quantity
    s.payment()
    print("\nFinal Summary of purchase")
    print(s)

    # Print how the object was constructed
    print("\nThe object was constructed according to:")
    print(repr(s))

    # The last statement
    input("\nPlease press any key to terminate")

if __name__ == '__main__':
    main()
    