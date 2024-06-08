from Node import Node
from Solve import UCS, A_star
from Heuristic import Heuristic
import argparse


def read_maze(maze_file):
    with open(maze_file, "r") as f:
        maze = [[char for char in line.strip()] for line in f]
    return maze


h1 = Heuristic.distanceOfTwoFood
h2 = Heuristic.minEuclideanDistance

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--maze', metavar='MAZESIZE',
                    type=str, help='Size of maze')
parser.add_argument('-s', '--searchStrategy',
                    metavar='SEARCHSTRATEGY', type=str, help='Search strategy')
parser.add_argument('-hf', '--heuristic', metavar='HEURISTIC',
                    type=str, help='Heuristic function')

args = parser.parse_args()

if args.maze:
    mazeSize = args.maze
if args.searchStrategy:
    searchStrategy = args.searchStrategy
if args.heuristic:
    heuristic = args.heuristic


path = f"layouts\\{mazeSize}.lay"
if searchStrategy.upper() == 'UCS':
    problem = Node(read_maze(path))
    ucs = UCS()
    path = ucs.search(problem)

elif searchStrategy.upper() == 'ASTAR':
    problem = Node(read_maze(path))

    astar = A_star()

    if heuristic == 'h1':
        path = astar.search(problem, h1)
    elif heuristic == 'h2':
        path = astar.search(problem, h2)


problem.visualize(path, sleepTime=0.1)
print(f'\n{searchStrategy.upper()} - {mazeSize}')
print("Total Cost:", len(path))
print("Path:\n", path)
