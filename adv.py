from room import Room
from player import Player
from world import World
from util import Stack
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
#traversal_path = []




def explore():
    visited = set()
    visited.add(0)
    bread_crumbs = []
    rooms = {}
    reverse_it = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
    rooms[player.current_room.id] = {}
    directions = player.current_room.get_exits()
    for way in directions:
        rooms[player.current_room.id][way] = '?'
    current_path = []
    while True:
        rooms_to_visit = [d for d in rooms[player.current_room.id] if rooms[player.current_room.id][d] == '?']
        if len(rooms_to_visit) > 0:
            next_path = rooms_to_visit.pop()
            if len(rooms[player.current_room.id]) == 1:
                rooms[player.current_room.id][next_path] = player.current_room.id

            last_id = player.current_room.id
            player.travel(next_path)
            current_path.append(next_path)
            bread_crumbs.append(next_path)
            if player.current_room.id not in visited:
                visited.add(player.current_room.id)
                rooms[player.current_room.id] = {}
                for way in player.current_room.get_exits():
                    rooms[player.current_room.id][way] = '?'
            rooms[last_id][next_path] = player.current_room.id
            rooms[player.current_room.id][reverse_it[next_path]] = last_id

        else:
            if len(bread_crumbs) > 0:
                back_track = reverse_it[bread_crumbs.pop()]
                current_path.append(back_track)
                player.travel(back_track)
            else:
                print(rooms)
                return current_path


traversal_path = explore()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
