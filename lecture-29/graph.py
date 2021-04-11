import math

class Vertex:
    def __init__(self):
        self.nbrs = {}
        # [String, Integer]

class Pair:
    def __init__(self, vname, psf):
        self.vname = vname
        self.psf = psf

class PrimsPair:
    def __init__(self, vname, acqvname, cost):
        self.vname = vname
        self.acqvname = aqcvname
        self.cost = cost

    def __lt__(self, other):
        return other.cost - self.cost

class DijsktraPair:
    def __init__(self, vname, psf, cost):
        self.vname = vname
        self.acqvname = aqcvname
        self.cost = cost

    def __lt__(self, other):
        return other.cost - self.cost

class Graph:
    def __init__(self):
        self.vtces = {}
        # key: vertexName String, value: reference

    def numVertex(self):
        return len(self.vtces)

    def containsVertex(vname):
        return vname in self.vtces

    def addVertex(self, value):
        vertex = Vertex()
        self.vtces[value] = vertex

    def removeVertex(self, vname):
        vertex = self.vtces[vname]

        keyS = list(vertex.nbrs.keys())

        for key in keyS:
            neighbour = vtces.get(key)
            del neighbour.nbrs[vname]

        del self.vtces[vname]

    def display(self):

        keyS = list(self.vtces.keys())

        for key in keyS:
            vertex = self.vtces[key]
            print(key, " -> ", vertex.nbrs)

    def numEdges(self):
        keyS = list(self.vtces.keys())

        count = 0

        for key in keyS:
            vertex = self.vtces[key]
            count += len(vertex.nbrs)

        return count // 2

    def containsEdge(self, A, B):
        f = self.vtces[A]
        s = self.vtces[B]

        if f == None || s == None || B not in f.nbrs:
            return False

        return True

    def addEdge(self, first, second, weight):
        f = self.vtces[first]
        s = self.vtces[second]

        if f == None || s == None || second in f.nbrs:
            return

        f.nbrs[second] = weight
        s.nbrs[first] = weight

    def hasPath(self, first, second, visited):

        # MAP
        visited[first] = True

        if self.containsEdge(first, second):
            return True

        vertex = self.vtces[first]
        keyS = list(vertex.nbrs.keys())

        for key in keyS:
            if key not in visited and self.hasPath(key, second, visited):
                return True

        return False

    def bfs(self, source, destination):
        # hashmap
        processed = {}
        queue = Queue() # this is the one we created, please update code accordingly.

        sp = Pair(source, source)

        queue.insert(sp)

        while not queue.isEmpty():
            rp = queue.remove()

            if rp.vname in processed:
                continue

            processed[rp.vname] = True

            if self.containsEdge(rp.vname, destination):
                print(rp.psf, destination)
                return True

            # neighbours
            rpvtx = self.vtces[rp.vname]
            nbrs = list(rpvtx.nbrs.keys()) # list of string

            for nbr in nbrs:
                # process only unprocessed neighbours
                if nbr not in processed:
                    np = Pair(nbr, rp.psf + nbr)
                    queue.insert(np)

        return False

    def dfs(self, source, destination):
        # hashmap
        processed = {}
        stack = Stack() # this is the one we created, please update code accordingly.

        sp = Pair(source, source)

        stack.insert(sp)

        while not stack.isEmpty():
            rp = stack.remove()

            if rp.vname in processed:
                continue

            processed[rp.vname] = True

            if self.containsEdge(rp.vname, destination):
                print(rp.psf, destination)
                return True

            # neighbours
            rpvtx = self.vtces[rp.vname]
            nbrs = list(rpvtx.nbrs.keys()) # list of string

            for nbr in nbrs:
                # process only unprocessed neighbours
                if nbr not in processed:
                    np = Pair(nbr, rp.psf + nbr)
                    stack.insert(np)

        return False

    def isCyclic(self):
        processed = {} # hashmap
        queue = Queue()
        keyS = list(self.vtces.keys())

        for key in keyS:
            if key in processed:
                continue

            sp = Pair(key, key)

            queue.insert(sp)

            while not queue.isEmpty():
                rp = queue.remove()

                if rp.vname in processed:
                    return True

                # neighbours
                rpvtx = self.vtces[rp.vname]
                nbrs = list(rpvtx.nbrs.keys()) # list of string

                for nbr in nbrs:
                    # process only unprocessed neighbours
                    if nbr not in processed:
                        np = Pair(nbr, rp.psf + nbr)
                        queue.insert(np)

        return False

    def isConnected(self):
        flag = 0
        processed = {} # hashmap
        queue = Queue()
        keyS = list(self.vtces.keys())

        for key in keyS:
            if key in processed:
                continue

            flag += 1
            sp = Pair(key, key)

            queue.insert(sp)

            while not queue.isEmpty():
                rp = queue.remove()

                if rp.vname in processed:
                    continue

                # neighbours
                rpvtx = self.vtces[rp.vname]
                nbrs = list(rpvtx.nbrs.keys()) # list of string

                for nbr in nbrs:
                    # process only unprocessed neighbours
                    if nbr not in processed:
                        np = Pair(nbr, rp.psf + nbr)
                        queue.insert(np)

        if flag >= 2:
            return False

        return True

    def isTree(self):
        return not self.isCyclic() and self.isConnected()




    def prims(self): # return a graph (MST)

        mst = Graph()

        # use hashmap to get neighbours in constant time
        hashMap = {} # String, PrimsPair

        heap = Heap() # use custom one

        for key in self.vtces.keys():
            np = PrimsPair(key, None, math.inf)
            heap.add(np)
            hashMap[key] = np

        while not heap.isEmpty():
            rp = heap.remove()
            del hashMap[rp.vname]

            if rp.acqvname == None:
                mst.addVertex(rp.vname)
            else:
                mst.addVertex(rp.vname)
                mst.addEdge(rp.vname, rp.aqvname, rp.cost)

            # check neighbours of rp
            for nbr in self.vtces[rp.vname].nbrs.keys():

                # work for nbrs which are in map
                if nbr in hashMap:
                    # old cost and new cost
                    oc = hashMap[nbr].cost
                    nc = self.vtces[rp.vname].nbrs[nbr]

                    if nc < oc:
                        gp = hashMap[nbr]

                        # this is same object as in heap, hence updating this will update heap too.
                        # this is why we are using hashmaps

                        gp.acqvname = rp.vname
                        gp.cost = nc

                        heap.updatePriority(gp) # custom one: you just need to fo UPHEAP now

        return mst

    def dijkstra(self, src):
        ans = {} # <String, Integer>

        hashMap = {}

        heap = Heap()

        for key in self.vtces.keys():
            np = DijkstraPair(key, "", math.inf)

            if key == src:
                np.cost = 0
                np.psf = key

            heap.add(np)
            hashMap[key] = np

        while not heap.isEmpty():
            # remove a pair
            rp = heap.remove()
            del hashMap[rp.vname]

            ans.put(rp.vname, rp.cost)

            # check neighbours
            for nbr in self.vtces[rp.vname].nbrs.keys():
                if nbr in hashMap:
                    oc = hashMap[nbr].cost
                    nc = rp.cost + self.vtces[rp.vname].nbrs[nbr]

                    if nc < oc:
                        gp = hashMap[nbr]
                        gp.psf = rp.psf + nbr
                        gp.cost = nc

                        # do upheap
                        heap.updatePriority(gp) # this is just upheap
        return ans
