def solution(genres, plays):
    # playsMap = new Map({genre : { total_plays: number, songs: [(idx, plays)...]}, ...}...{...})
    genresMap = dict()
    for i in range(len(genres)):
        if genres[i] not in genresMap:
            genresMap[genres[i]] = { 'total_plays': 0, 'songs': []}
        genresMap[genres[i]]['total_plays'] += plays[i]
        genresMap[genres[i]]['songs'].append((i, plays[i]))
    # playsMap.sort by sum of plays in genre
    sortedMap = sorted(genresMap.keys(), key = lambda genre: genresMap[genre]['total_plays'], reverse = True)
    # Get Value from front.
    answer = []
    for genre in sortedMap:
        sorted_songs = sorted(genresMap[genre]['songs'], key = lambda song: (-song[1], song[0]))
        for i in range(min(2, len(sorted_songs))):
            answer.append(sorted_songs[i][0])
    return answer