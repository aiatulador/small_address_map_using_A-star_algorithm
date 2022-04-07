def a_star_search(start, goal):
    open_fringe = set(start)
    close_fringe = set()
    g = {}  # store distance from starting node
    parents = {}  # parents contains an adjacency map of all nodes

    # distance of starting node from itself is zero
    g[start] = 0

    # start is root node i.e it has no parent nodes
    # so start is set to its own parent node
    parents[start] = start  # start node

    while len(open_fringe) > 0:
        n = None
        # node with lowest f() is found
        for v in open_fringe:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == goal or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # nodes 'm' not in first and last set are added to first
                # n is set its parent
                if m not in open_fringe and m not in close_fringe:
                    open_fringe.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight


# for each node m,compare its distance from start i.e g(m) to the
                # from start through n node
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n

                        # if m in closed set,remove and add to open
                        if m in close_fringe:
                            close_fringe.remove(m)
                            open_fringe.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the goal
        # then  begin reconstructing the path from it to the start
        if n == goal:
            path = []
            path_cp = []
            full = {
                'A': "Agasadek Road (Home)",
                'CHA': "Chankarpool",
                'TSC': "TSC",
                'SHA': "Shabagh",
                'PAL': "Palashi",
                'NIL': "Nilkhet",
                'SCI': "Science Lab",
                'GR': "Green Road",
                'PAN': "Panthapath",
                'ER': "Elephant Road",
                'D32': "Dhanmondi 32",
                'BM': "Banglamotor",
                'KB': "Karwan Bazar",
                'FG': "Farmgate",
                'UAP': "UAP"
            }
            while parents[n] != n:
                path.append(n)
                path_cp.append(full[n])
                n = parents[n]

            path.append(start)
            path_cp.append(full[start])
            path.reverse()
            path_cp.reverse()
            print('Path found: {}'.format(str(path_cp).replace(",", "-->")))
            return path

        open_fringe.remove(n)
        close_fringe.add(n)

    print('Path does not exist!')
    return None


def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):
    H_dist = {

        'A': 2,
        'CHA': 30,
        'PAL': 10,
        'TSC': 20,
        'SHA': 30,
        'NIL': 5,
        'SCI': 5,
        'GR': 10,
        'PAN': 10,
        'ER': 50,
        'D32': 10,
        'BM': 5,
        'KB': 5,
        'FG': 1,
        'UAP': 0
    }
    return H_dist[n]


Graph_nodes = {


    'A': [('CHA', .75)],
    'CHA': [('TSC', 1.1), ('PAL', 1.2)],
    'PAL': [('NIL', .9), ('ER', 1.7)],
    'TSC': [('SHA', .8), ('NIL', 1)],
    'SHA': [('BM', .9), ('ER', .7), ('SCI', 1)],
    'NIL': [('SCI', .9)],
    'SCI': [('GR', 1.3), ('D32', 1.6)],
    'GR':  [('PAN', .21)],
    'PAN': [('UAP', .5)],
    'ER':  [('GR', 1.7), ('KB', 1.8)],
    'D32': [('PAN', 1.1), ('UAP', 1.4)],
    'BM':  [('KB', .85)],
    'KB':  [('FG', 1.1), ('PAN', 1)],
    'FG':  [('UAP', .45)],
    'UAP': None
}

path = a_star_search('A', 'UAP')

path_cost = 0.0

for i in range(len(path) - 1):
    for key, value in Graph_nodes[path[i]]:
        if key == path[i + 1]:
            path_cost += value
            break
print("The path cost is %.2f Km" % path_cost)
