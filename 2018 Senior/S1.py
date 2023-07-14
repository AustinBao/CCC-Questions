
# Submitted on DMOJ (Fully accepted)

N = int(input())

unsorted_road = []
for i in range(N):
    unsorted_road.append(int(input()))

# could have used .sort() function but wanted to make it myself
sorted_road = []
while len(unsorted_road) != 0:
    minimum = unsorted_road[0]
    for cities_i in unsorted_road:
        if cities_i < minimum:
            minimum = cities_i
    sorted_road.append(minimum)
    unsorted_road.remove(minimum)

neighborhoods = []
for cities_i in range(1, len(sorted_road) - 1):
    left = abs(sorted_road[cities_i] - sorted_road[cities_i - 1]) / 2
    right = abs(sorted_road[cities_i] - sorted_road[cities_i + 1]) / 2
    neighborhoods.append(left + right)

print(min(neighborhoods))
