const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
});

let input;

readline.on("line", function(line){
    input=line.split(' ');
    readline.close()
  }
).on("close", function(){
  const n = BigInt(input[0])
  const m = BigInt(input[1])
  solution(n, m);
  process.exit();
})

const solution = (n, m) => {
  console.log((n/m).toString());
  console.log((n%m).toString());
}