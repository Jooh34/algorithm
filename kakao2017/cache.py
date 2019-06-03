def solution(cacheSize, cities):
    def insert(city):
        cache.append(city)
        if len(cache) > cacheSize:
            cache.pop(0)

    def getCache(city):
        l = len(cache)
        for i in range(l):
            if cache[i] == city:
                for j in range(i, l-1):
                    cache[j] = cache[j+1]

                cache[l-1] = city
                return True
        return False

    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    cache = []
    answer = 0

    for city in cities:
        if getCache(city):
            answer = answer + 1
        else:
            answer = answer + 5
            insert(city)

    return answer


cacheSize = 2
cities = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
print(solution(cacheSize, cities))
