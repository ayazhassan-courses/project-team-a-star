class Node():
    
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

maze = [["_", "_", "_", "_", "|", "_", "_", "_", "_", "_"],
        ["_", "_", "_", '_', "|", '_', "_", "_", "_", "_"],
        ["_", "_", "_", "_", "|", "_", "_", "_", "_", '_'],
        ["_", "_", '_', "_", "|", "_", "_", '_', "_", '_'],
        ["_", '_', '_', "_", "|", "_", "_", "_", "_", "_"],
        ["_", '_', '_', "_", "_", "_", "_", "_", "_", "_"],
        ["_", "_", '_', "_", "|", "_", "_", "_", "_", "_"],
        ["_", "_", "_", "_", "|", "_", "_", "_", "_", "_"],
        ["_", "_", '_', "_", "|", "_", "_", "_", "_", "_"],
        ["_", "_", '_', "_", "|", "_", "_", "_", "_", "_"]]
start = (0, 0)
end = (7, 6)        
def astar(maze, start, end):

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

