const Queue = function () {
  this.storage = {};
  this.front = 0;
  this.rear = 0;
};

Queue.prototype = {
  size() {
    if (this.storage[this.rear] === undefined) {
      return 0;
    } else {
      return this.rear - this.front + 1;
    }
  },
  push(value) {
    if (this.size() === 0) this.storage["0"] = value;
    else {
      this.rear++;
      this.storage[this.rear] = value;
    }
  },
  pop() {
    let value;
    if (this.front === this.rear) {
      value = this.storage[this.rear];
      delete this.storage[this.rear];
      this.front = 0;
      this.rear = 0;
    } else {
      value = this.storage[this.rear];
      delete this.storage[this.rear];
      this.rear--;
    }
    return value;
  },
  popleft() {
    let value;
    if (this.front === this.rear) {
      value = this.storage[this.front];
      delete this.storage[this.front];
      this.front = 0;
      this.rear = 0;
    } else {
      value = this.storage[this.front];
      delete this.storage[this.front];
      this.front++;
    }
    return value;
  },
};

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let board = [];
let count = 0;

readline
  .on("line", function (line) {
    if (count === 0) {
      input.push(line.split(' '));
      count++;
    } 
    else if (0 < count && count <= parseInt(input[0][0]))   {
      input.push(line.split(' '));
      count++;
      if (count === parseInt(input[0][0])+1) readline.close();
    }
  })
  .on("close", function () {
    const n = parseInt(input[0][0]);
    const m = parseInt(input[0][1]);
    for (let i=1; i<=n; i++){
      board.push(input[i].map(el => parseInt(el)));
    }
    solution(n, m, board)
    process.exit();
  });

const solution = (n, m, board) => {
  const moveType = [[0, 1], [0, -1], [1, 0], [-1, 0]];
  const dp = [];
  const virus = [];
  const q = new Queue();
  
  for (let i=0; i<n; i++){
    const tmp = [];
    for (let j=0; j<m; j++){
      if (board[i][j] > 0) virus.push([board[i][j], i, j])
      tmp.push(0);
    }
    dp.push(tmp);
  }
  for (let x of virus) q.push(x);

  while (q.size() > 0){
    const value = q.popleft();
    const kind = value[0];
    const x = value[1];
    const y = value[2];
    
    if (board[x][y] !== 3){
      for (let i=0; i<4; i++){
        const nx = x + moveType[i][0]; 
        const ny = y + moveType[i][1];
        if ((0 <= nx && nx < n) && (0 <= ny && ny < m) && board[nx][ny] !== -1){
          if (board[nx][ny] === 0){
            board[nx][ny] = kind;
            dp[nx][ny] = dp[x][y] + 1;
            q.push([kind, nx, ny]);
          } else if (board[nx][ny] !== kind && dp[nx][ny] === dp[x][y]+1) {
            board[nx][ny] = 3;
          }
        }
      }
    }
  }
  let one=0;
  let two=0;
  let three=0;

  for (let i=0; i<n; i++){
    for (let j=0; j<m; j++){
      if (board[i][j] === 1) one++;
      else if (board[i][j] === 2) two++;
      else if (board[i][j] === 3) three++;
    }
  }
  
  console.log(one, two, three)
};