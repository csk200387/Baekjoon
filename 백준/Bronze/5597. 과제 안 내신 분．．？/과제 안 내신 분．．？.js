let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

for (let i = 1; i <= 30; i++) {
    if(!input.includes(i.toString())) {
        console.log(i);
    }
}