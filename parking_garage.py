"""
Create a Parking_Garage class to track the actions taken by a functioning parking garage.

Attributes
    - tickets -> list
    - parkingSpaces -> list
    - currentTicket -> dictionary

"""


class ParkingGarage():

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        
        return [self.tickets.pop(), self.parkingSpaces.pop()]

    def payForParking(self, currentTicket):
        self.currentTicket = currentTicket
        if self.currentTicket['paid'] == False:
            payment = input('Please enter payment: ')
            if payment != '':
                self.currentTicket['paid'] = True
                return 'Ticket has been paid. Please exit the garage in 15 mins.'
            else:
                return 'Payment not accepted. Please try again'
        
        if self.currentTicket['paid'] == True:
            return 'Ticket has been paid. Please exit the garage in 15 mins.'
    
    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            self.tickets.append(1)
            self.parkingSpaces.append(1)
            return 'Thank you. Have a nice day!'
        else:
            print('Ticket has not been paid.')

cltParking = ParkingGarage(['Ticket ' + str(i) for i in range(1, 701)], ['Space ' + str(i) for i in range(1, 701)], {'paid' : False,})

def run():
    while True:
        action = input('Would you like to enter, pay or exit? Enter/Pay/Exit ')

        if action.lower() == 'enter':
            print(cltParking.takeTicket())
        elif action.lower() == 'pay':
            print(cltParking.payForParking({'paid' : False}))
        elif action.lower() == 'exit' and cltParking.currentTicket['paid'] == False:
            cltParking.leaveGarage()
        elif action.lower() == 'exit' and cltParking.currentTicket['paid'] == True:
            print('Thank you. Have a nice day!')
            break
        else:
            print(f'Sorry {action} is not recgonized please try again.')

run()