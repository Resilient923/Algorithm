def solution(cacheSize, cities):
    # 캐시사이즈가없으면 참조할게 없으니까 실행시간이 5씩 소요된다.
    if cacheSize == 0:
        return len(cities) * 5
    else:
        cache = []
        answer = 0
        for city in cities:
            # Miss!
            city = city.lower()
            if city not in cache:
                answer += 5
                if len(cache) < cacheSize:
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)
            # Hit!
            else:
                answer += 1
                cache.pop(cache.index(city))
                cache.append(city)

        return answer

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize,cities))

