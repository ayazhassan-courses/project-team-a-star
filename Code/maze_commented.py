class Node():
    # A Node class for A* path-finding
    def __init__(self, parent=None, position=None):  # -------------------------> O(1)
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):                         # -------------------------> O(1)
        return self.position == other.position

n = int(input("Enter maze dimesion: "))
def maze(n):
    # Generates the maze by taking dimesions of maze
    puz = []
    for i in range(0,n):                             # --------------------------> O(n); n = len(maze)
        temp = input().split(" ")
        puz.append(temp)

    return puz

maze = maze(n)
def display_maze(maze):                              # --------------------------> O(n)
    for length in maze:
        print(length)
print("") 
display_maze(maze)

print("")

# Takes tuples for starting and ending co-ordinates 
start_list = []
end_list = []
for i in range(2):                                   # ---------------------------> O(2)
    if i == 0:
        a = int(input("Enter starting column: "))
        start_list.append(a)
    else:
        a = int(input("Enter starting row: "))
        start_list.append(a)

for x in range(2):                                   # ---------------------------> O(2)
    if x == 0:
        b = int(input("Enter ending column: "))
        end_list.append(b)
    else:
        b = int(input("Enter ending row: "))
        end_list.append(b)

start = start_list[0],start_list[1]
end = end_list[0],end_list[1]        
def astar(maze, start, end):
    # Returns the list of tuples as the shortest path from start to goal

    # Create start and End node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    flag = False

    # Loop until you find the end
    while len(open_list) > 0:                       # --------------------------> O(|V|^2); V = vertice or nodes
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        Adjacent_squares = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for new_position in Adjacent_squares:            # ----------------------------> O(8)
            
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != "_":
                continue
            
            # Append
            new_node = Node(current_node, node_position)

            children.append(new_node)
        # Could not find the path
        if len(children) == 0:
            flag = True

        # Loop through children
        for child in children:                            # ---------------------------> O(8)

            # Child is on the closed list
            if child in closed_list:
                continue
            
            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = (((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2))**0.5
            child.f = child.g + child.h

            # Child is already in the open list
            if child not in open_list:
                # Add the child to the open list
                open_list.append(child)
    
    # If children is empty
    if flag == True:
        return "Blocked! Cannot find a way to the goal."

print("")
print(astar(maze, start, end))

"""
Overall time complexity of the code: O(|V|^2)
"""