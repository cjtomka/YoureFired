class Boat:
    def __init__(self, size = 1, coordinates = []):
        self.size = size
        self.coordinates = coordinates
        self.destroyed = False
        self.hitlist = []
    def validPlace(self, coordinates):
        """Checks to see if boat is in a valid place and if each part of the boat is at consecutive indexes

        Args:
        coordinates - array of coordinate that the opponent wants to hit

        Returns:
        Returns a bool if the boat is in a valid place, prevents being place diagonally
        """
        if len(coordinates) != 1:
            for i in range(0, len(coordinates)):
                check = False #if true, program won't accidentally check the second condition
                if i != (len(coordinates) - 1):
                    if (coordinates[i][0] != coordinates[i + 1][0]):
                        print(1, coordinates[i][0], coordinates[i + 1][0])
                        if (coordinates[i][1] != coordinates[i + 1][1]):
                            print(2, coordinates[i][1], coordinates[i + 1][1])
                            return False
                else:
                    if (coordinates[i][0] != coordinates[i - 1][0]):
                        print(3, coordinates[i][0], coordinates[i - 1][0])
                        if (coordinates[i][1] != coordinates[i - 1][1]):
                            print(4, coordinates[i][1], coordinates[i - 1][1])
                            return False
            print("k") #WHAT IS THIS FOR?
            if coordinates[0][0] == coordinates[1][0]:
                for i in range(len(coordinates)):
                    if i != len(coordinates) - 1:
                        if abs(coordinates[i + 1][1] - coordinates[i][1]) != 1:
                            return False
                    else:
                        if abs(coordinates[i][1] - coordinates[i - 1][1]) != 1:
                            return False
            elif coordinates[0][1] == coordinates[1][1]:
                for i in range(len(coordinates)):
                    if i != len(coordinates) - 1:
                        if abs(coordinates[i + 1][0] - coordinates[i][0]) != 1:
                            return False
                    else:
                        if abs(coordinates[i][0] - coordinates[i - 1][0]) != 1:
                            return False
        else:
            if coordinates[0][0] < 0 or coordinates[0][0] >= 8 or coordinates[0][1] < 0 or coordinates[0][1] >= 8:
                return False
        self.setCoordinates(coordinates)
        self.size = len(coordinates)
        return True

    def checkDestroyed(self):
        """Checks to see if boat is destroyed

        Returns:
        Returns a bool if the boat is destroyed (True) or not (False)
        """
        if(len(self.hitlist) == self.size):
            self.destroyed = True
            return True
        else:
            self.destroyed = False
            return False
    def hit(self, coordinate):
        """Adds coordinate to hitlist array and checks if it is alread hit

        Args:
        coordinates - array of coordinate that the opponent wants to hit

        Returns:
        Returns a string to let the player know if it was a hit or not
        """
        if coordinate not in self.coordinates:
            return "Miss!"
        else:
            if self.destroyed == False and coordinate not in self.hitlist:
                self.hitlist.append(coordinate)
            check = self.checkDestroyed()
            if check == True:
                return "Hit Confirmed & Boat is Destroyed!"
            else:
                return "Hit Confirmed!"
    def getCoordinates(self):
        """gives user coordinates of the boat

        Returns:
        Returns an array of tuples of the coordinates
        """
        return self.coordinates
    def getSize(self):
        """Returns size of the boat

        Returns:
        Returns int of the size of the boat
        """
        return self.size

    def setCoordinates(self, coordinates):
        """Sets coordinates of the boat

        Args:
        coordinates - array of tuples of coordinates

        Returns:
        None
        """
        self.coordinates = coordinates
