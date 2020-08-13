from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
total_rooms = len(room_graph)
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

compass = {"n": "s", "e": "w", "w": "e", "s": "n"}


def dfs_recursive(player, prev_room=None, direction=None, visited=None, path=None):
    if visited is None:
        visited = {}
    if path is None:
        path = []

    # move in the direction given in the variable "direction" if not first move
    if prev_room != None:
        path.append(direction)
        player.travel(direction)
        current_room = player.current_room.id
    current_room = player.current_room.id
    print(f"Current room: {current_room}")
    # Initialize values for the directions of the current room
    if current_room not in visited:
        visited[current_room] = {}
        adjacent_rooms = player.current_room.get_exits()
        for room in adjacent_rooms:
            visited[current_room][room] = "?"

    # Add the prev_room at the return direction and the current room at the cooresponding direction of the prev_room
    if prev_room != None:
        visited[prev_room][direction] = current_room
        visited[current_room][compass[direction]] = prev_room

    # depth first traversal method, should continue traveling until dead end is hit
    # recursion allows for not having to waste moves returning to fork in the road
    for direction in visited[current_room]:
        if visited[current_room][direction] == "?":
            dfs_recursive(player, current_room, direction, visited, path)
            if total_rooms != len(visited.keys()):
                path.append(compass[direction])
                player.travel(compass[direction])
    return path


traversal_path = dfs_recursive(player)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
