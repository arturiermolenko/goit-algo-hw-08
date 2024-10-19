import heapq


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        cable_1 = heapq.heappop(cables)
        cable_2 = heapq.heappop(cables)

        combined_length = cable_1 + cable_2
        total_cost += combined_length

        heapq.heappush(cables, combined_length)

    return total_cost


my_cables = [8, 4, 6, 12]
print(
    "Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(my_cables)
)
