from Graph import Graph
from PathPlanning import PathPlanning
from Room import Room

class map:
    def __init__(self):
        self.rooms = []
        self.last_id = 0
        self.graph = Graph()

    def __init__(self, rooms):
        self.rooms = rooms
        self.last_id = len(self.rooms) - 1
        self.graph = Graph()
        for r in rooms:
            self.graph.addVertex(r.ID)
            for e in r.neighbours:
                self.graph.addEdge({r.ID,e})



    def addRoom(self,ID, roomName, neighbours, description, category):
        room = Room(ID, roomName, neighbours, description, category)
        self.graph.addVertex(room.ID)
        for n in room.neighbours:
            self.graph.AddEdge(n)
        self.rooms.append(room)
        self.last_id = len(self.rooms) - 1

if __name__ == '__main__':
    rooms = []
    #(self, ID, roomName, neighbours, description, category):

    rooms.append(Room(0,"entrance",[1,9],"Hall 1 enterance","utility"))
    rooms.append(Room(1,"station" , [0,2],"Robot station"  ,"utility"))
    for i in range(2,9):
        if i==5:
            rooms.append(Room(i,"exit",[4,6],"Hall exit","utility"))
        else:
            rooms.append(Room(i,"room "+str(i), [i-1,i+1],"Patient Room","normal"))
    rooms.append(Room(9,"pharmacy",[0,8],"Hall Pharmacy","medical"))
    map = map(rooms)

    pathPlanning = PathPlanning(map)
    routs = pathPlanning.map.graph.getPathes(9,3)
    for r in routs:
        print(r)

