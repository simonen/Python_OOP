from project.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)

    def drive(self):
        return "driving..."
