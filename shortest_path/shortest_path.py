def dijkstra(wg, source, target):
    nodes = {}
    unvisited = set()
    previous = {}
    for node in wg.nodes():
        unvisited.add(node)
        if node == source:
            nodes[node] = 0
            current = node
        else:
            nodes[node] = float('infinity')
    done = False
    while unvisited:
        print 'current: {}'.format(current)
        done = False
        while not done:
            neighbors = set(wg.neighbors(current))
            if neighbors == set():
                done = True
            # min_ = 'node', float('infinity')
            print 'unvisited {}'.format(unvisited)
            for neighbor in neighbors.intersection(unvisited):
                print nodes[neighbor]
                if nodes[neighbor] != float('infinity'):
                    print 'not infinity'
                    dist = nodes[current] + wg.edgeWeights[(current, neighbor)]
                else:
                    dist = wg.edgeWeights[(current, neighbor)]
                if dist < nodes[neighbor]:
                    nodes[neighbor] = dist
                    previous[neighbor] = current
            done = True
                # if dist < min_[1]:
                #     min_ == neighbor, dist
            # if current == target:
            #     done = True
            # current = min_[0]
        unvisited.remove(current)
        min_ = 'node', float('infinity')
        for node in unvisited:
            # import pdb; pdb.set_trace()
            if nodes[node] < min_[1]:
                min_ = node, nodes[node]
        current = min_[0]

    distance = nodes[target]
    path = [target]
    done = False
    while path[0] != source:
        target = previous[target]
        path.insert(0, target)
    return path, distance


def bellman_ford_moore(wg, source):
    weight = {}
    predecessor = {}
    for node in wg.nodes():
        if node == source:
            weight[node] = 0
        else:
            weight[node] = float('infinity')
        predecessor[node] = None

    for node in wg.nodes():
        for start, end in wg.edges():
            if weight[start] + wg.edgeWeights(node) < weight(end):
                weight[end] = weight[start] + wg.edgeWeights(node)
                predecessor[end] = start

    for start, end in wg.edges():
        if weight[start] + wg.edgeWeights(node) < weight[end]:
            return "Graph has a negative-weight cylcle!!!"

    return (weight, predecessor)
