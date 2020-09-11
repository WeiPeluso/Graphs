from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "projects/adventure/maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"å
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

opposite_direction = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}


def traversal_the_map():
    visited_rooms = set()
    moves = Stack()

    while len(visited_rooms) < len(room_graph):
        available_directions = []

        visited_rooms.add(player.current_room)

        exits = player.current_room.get_exits()

        for exit in exits:
            if exit is not None:
                if player.current_room.get_room_in_direction(exit) not in visited_rooms:
                    available_directions.append(exit)

        if len(available_directions) > 0:
            direction = available_directions[random.randint(
                0, len(available_directions)-1)]
            traversal_path.append(direction)
            moves.push(direction)
            player.travel(direction)
        else:
            last_move = moves.pop()
            traversal_path.append(opposite_direction[last_move])
            player.travel(opposite_direction[last_move])


traversal_the_map()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
