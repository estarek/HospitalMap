class Room:

    def __init__(self, ID, roomName, neighbours, description, category):
        self.ID = ID
        self.nodeName = roomName
        self.neighbours = neighbours
        self.description = description
        self.category = category

    def DisplayRoom(self):
        pass


if __name__ == '__main__':
    r0 = Room(0, "entrance", [1, 9], "Hall 1 enterance", "utility")
    print(r0)
