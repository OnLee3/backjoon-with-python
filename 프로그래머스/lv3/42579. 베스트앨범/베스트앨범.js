function solution(genres, plays) {
    let genrePlays = {};

    for (let i = 0; i < genres.length; i++) {
        let genre = genres[i];
        let play = plays[i];

        if (!genrePlays[genre]) {
            genrePlays[genre] = {totalPlays: 0, songs: []};
        }

        genrePlays[genre].totalPlays += play;
        genrePlays[genre].songs.push({index: i, play: play});
    }

    let sortedGenres = Object.keys(genrePlays).sort((a, b) => genrePlays[b].totalPlays - genrePlays[a].totalPlays);

    let result = [];
    for (let genre of sortedGenres) {
        let sortedSongs = genrePlays[genre].songs.sort((a, b) => (b.play - a.play) || (a.index - b.index));

        for (let i = 0; i < Math.min(2, sortedSongs.length); i++) {
            result.push(sortedSongs[i].index);
        }
    }

    return result;
}
