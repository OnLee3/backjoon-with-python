function solution(players, callings) {
  const playerIndices = {};

  for (let i = 0; i < players.length; i++) {
    playerIndices[players[i]] = i;
  }

  for (let i = 0; i < callings.length; i++) {
    const calledPlayer = callings[i];
    const calledPlayerIndex = playerIndices[calledPlayer];

    if (calledPlayerIndex > 0) {
      const prevPlayer = players[calledPlayerIndex - 1];
      players[calledPlayerIndex - 1] = calledPlayer;
      players[calledPlayerIndex] = prevPlayer;

      playerIndices[calledPlayer] = calledPlayerIndex - 1;
      playerIndices[prevPlayer] = calledPlayerIndex;
    }
  }
  return players;
}