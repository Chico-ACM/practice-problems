import sys, math, heapq
from collections import namedtuple

def getline():
    return sys.stdin.readline().strip()

Wormhole = namedtuple("Wormhole", "entry exit")

class Planet():
    def __init__(self, name, x, y, z):
        self.name = name # will make debugging easier
        self.x = x
        self.y = y
        self.z = z
        self.explored = False
        self.cost = float("inf")

def dist(a, b):
    dx, dy, dz = (a.x - b.x), (a.y - b.y), (a.z - b.z)
    return math.sqrt((dx ** 2) + (dy ** 2) + (dz ** 2))

def min_dist(planets, wormholes, start, finish):
    # initialize graph
    for name, p in planets.iteritems():
        p.explored = False

    # routes are tuples of (cost, dest)
    routes = [] # minheap

    def enqueue(cost, dest):
        heapq.heappush(routes, (cost, dest)) # heapq orders by first element in tuple

    def dequeue():
        return heapq.heappop(routes) # returns item with lowest cost

    # add initial routes
    start.explored = True
    start.cost = 0
    heapq.heappush(routes, (dist(start, finish), finish)) # heapq orders by first element in tuple
    for w in wormholes:
        heapq.heappush(routes, (dist(start, w.entry), w.exit))

    while routes:
        cost, dest = dequeue() # returns shortest route

        # check if done
        if dest == finish:
            return cost

        # don't from a planet more than once
        if dest.explored:
            continue
        else:
            dest.explored = True

        # add next steps
        heapq.heappush(routes, (dist(dest, finish), finish)) # direct route
        for w in wormholes:
            next_cost = cost + dist(dest, w.entry)
            next_dest = w.exit

            # don't enqueue routes to places already explored, or with known shorter paths
            if next_dest.explored or next_dest.cost < next_cost:
                continue
            else:
                next_dest.cost = next_cost

            # enqueue route
            heapq.heappush(routes, (next_cost, next_dest))

num_testcases = int(getline())
for i in range(num_testcases):
    print("Case {}:".format(i + 1))

    # initalize graph
    planets = {} # (empty) dictionary literal
    wormholes = [] # (empty) array literal

    # read planets
    num_planets = int(getline())
    for i in range(num_planets):
        name, x, y, z = getline().split(" ")
        planets[name] = Planet(name, int(x), int(y), int(z))

    # read wormholes
    for _ in range(int(getline())):
        entry, exit = [planets[name] for name in getline().split(" ")]
        wormholes.append(Wormhole(entry, exit))

    # read queries
    for _ in range(int(getline())):
        start, finish = [planets[name] for name in getline().split(" ")]

        # perform query
        distance = min_dist(planets, wormholes, start, finish)

        # print answer
        output_template = "The distance from {} to {} is {} parsecs."
        print(output_template.format(start.name, finish.name, int(round(distance))))
