from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        # Mapeia cada parada para as linhas que a servem
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        visited_stops = set()
        visited_routes = set()
        queue = deque()

        # Começamos pelas rotas que passam pela source
        for route in stop_to_routes[source]:
            queue.append((route, 1))  # (linha, número de ônibus pegos)
            visited_routes.add(route)

        while queue:
            route, buses = queue.popleft()
            for stop in routes[route]:
                if stop == target:
                    return buses
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_route in stop_to_routes[stop]:
                        if next_route not in visited_routes:
                            visited_routes.add(next_route)
                            queue.append((next_route, buses + 1))

        return -1
