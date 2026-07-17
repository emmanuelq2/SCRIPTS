def array_hopping_road(roadA, roadB):
    n = len(roadA)
    results = []

    for startA in range(n):
        visitedA = {startA}
        visitedB = set()

        on_road_a = True
        index = startA
        distance = 0

        while True:
            if on_road_a:
                index = roadA[index]
                distance += 1

                if index in visitedB:
                    break
                visitedB.add(index)
            else:
                index = roadB[index]
                distance += 1

                if index in visitedA:
                    break
                visitedA.add(index)

            on_road_a = not on_road_a

        results.append(distance)

    return results