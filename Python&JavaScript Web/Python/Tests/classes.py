class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassager(self, name):
        if not self.openSeats():
            return False
        
        self.passengers.append(name)
        return True

    def openSeats(self):
        return self.capacity - len(self.passengers)

flight = Flight(2)

people = ["Harry", "Hop", "Jory"]

for person in people:
    success = flight.addPassager(person)

    if success:
        print(f"Added {person}")
    else:
        print(f"No available seats on the board for {person}")

print(flight.passengers)
