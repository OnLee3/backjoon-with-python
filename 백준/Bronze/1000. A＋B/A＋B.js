const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on("line", (input) => {
    let arr = input.split(" "),
    a = parseInt(arr[0]),
    b = parseInt(arr[1]);

    console.log(a + b);

    rl.close();
})