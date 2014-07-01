def dijkstra(graph, source, target):
    nodes = {}
    unvisited = set()
    previous = {}
    for node in graph.nodes():
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
            neighbors = set(graph.neighbors(current))
            if neighbors == set():
                done = True
            # min_ = 'node', float('infinity')
            print 'unvisited {}'.format(unvisited)
            for neighbor in neighbors.intersection(unvisited):
                print nodes[neighbor]
                if nodes[neighbor] != float('infinity'):
                    print 'not infinity'
                    dist = nodes[current] + graph.edgeWeights[(current, neighbor)]
                else:
                    dist = graph.edgeWeights[(current, neighbor)]
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
