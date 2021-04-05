#노래는 고유번호로 구분한다
#속한 노래가 많이 장르를 먼저 수록
#장르 내에서 많이 재생된 노래를 먼저 수록
#장르 내에서 재생횟수가 같은 노래는 고유번호가 낮은거를 먼저 수록
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 800, 150, 800, 2500]


from collections import defaultdict
def solution(genres, plays):
    # defaultdict 생성 
    playList = defaultdict(list)
    for i in range(len(plays)):
        playList[genres[i]].append((i,plays[i]))
   
    album = []

    # 각 장르마다 재생된 노래 수를 딕셔너리 마지막에 삽입
    for key in playList.keys():
        playNumber = 0
        for v in playList[key]:
            playNumber += v[1]
        playList[key].append(playNumber)

    # 노래가 많이 재생된 순 내림차순 정렬
    playList = sorted(playList.items(), key = lambda x : x[-1][-1], reverse = True)
   
    # 각 장르에서 최대 두곡씩 많이 불린 순 내림차순, 고유번호 오름차순으로 정렬
    for v in playList:
        for idx, number in sorted(v[1][:-1], key = lambda x: (-x[1],x[0]))[:2]:
            album.append(idx)
    return album
print(solution(genres,plays))
