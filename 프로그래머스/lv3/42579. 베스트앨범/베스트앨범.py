def solution(genres, plays):
    # playsMap = new Map({genre : { total_plays: number, songs: [(idx, plays)...]}, ...}...{...})
    genre_plays = dict()
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genres[i] not in genre_plays:
            genre_plays[genre] = { 'total_plays': 0, 'songs': []}
        genre_plays[genre]['total_plays'] += play
        genre_plays[genre]['songs'].append((i, play))
        
    # playsMap.sort by sum of plays in genre
    sorted_genres = sorted(genre_plays.keys(), key = lambda genre: genre_plays[genre]['total_plays'], reverse = True)
    
    # Get Value from front.
    answer = []
    for genre in sorted_genres:
        sorted_songs = sorted(genre_plays[genre]['songs'], key = lambda song: (-song[1], song[0]))
        for i in range(min(2, len(sorted_songs))):
            answer.append(sorted_songs[i][0])
    return answer