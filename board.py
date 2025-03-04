from boats import Boat

class board:
    def __init__(self, rowSize, colSize):
        """
        Initialize arguments
        Args:
        rowSize (int): number of rows
        colSize (int): number of columns
        Returns:
        None
        """
        self.rowSize = rowSize
        self.colSize = colSize
        self.boardStorage = [[0 for y in range(colSize)] for x in range(rowSize)]
        self.hits = [[False for y in range(colSize)] for x in range(rowSize)]
        self.misses = [[False for y in range(colSize)] for x in range(rowSize)]

    def getSize(self):
        """
        Gets size of the board
        Args:
        None
        Returns:
        Size of the board
        """
        return(self.rowSize, self.colSize)

    def isBoat(self, xPos, yPos):
        """
        Checks if there is a boat tile at a given square
        Args:
        xPos (int): the x position for the tile to check
        yPos (int): the y position for the tile to check
        Returns:
        True if there is a boat at the given tile
        """
        if(self.boardStorage[xPos][yPos] == 1):
            return True
        return False

    def isHitt(self, xPos, yPos):
        """
        Checks if there is a hit at a given square
        Args:
        xPos (int): the x position for the tile to check
        yPos (int): the y position for the tile to check
        Returns:
        True if there is a hit
        """
        if(self.hits[xPos][yPos] == True):
            return True
        else:
            return False

    def isMiss(self, xPos, yPos):
        """
        Checks if there is a miss at a given square
        Args:
        xPos (int): the x position for the tile to check
        yPos (int): the y position for the tile to check
        Returns:
        True if there is a miss
        """
        if(self.misses[xPos][yPos] == True):
            return True
        return False

    def markHit(self, xPos, yPos):
        """
        Marks a HIT on the board
        Args:
        xPos (int): the x position for the tile to mark
        yPos (int): the y position for the tile to mark
        Returns:
        True if there is a hit to mark
        """
        self.hits[xPos][yPos] = True

    def markMiss(self, xPos, yPos):
        """
        Marks a MISS on the board
        Args:
        xPos (int): the x position for the tile to mark
        yPos (int): the y position for the tile to mark
        Returns:
        True if there is a miss to mark
        """
        self.misses[xPos][yPos] = True

    def populateBoard(self, boatlist):
        """
        Populates the board with boats
        Args:
        boatlist: list of boats to populate the board with
        Returns:
        None
        """
        for boat in boatlist:
            for coordinate in boat.getCoordinates():
                self.boardStorage[coordinate[0]][coordinate[1]] = 1

    def testBoard(self):
        """
        Prints out the board for testing purposes
        Args:
        None
        Returns:
        None
        """
        for x in range(self.rowSize):
            print(self.boardStorage[x])
        for x in range(self.rowSize):
            print(self.misses[x])
        for x in range(self.rowSize):
            print(self.hits[x])
