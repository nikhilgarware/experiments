let data = [5, 8, 6, 7, 2, 6, 9];
let average;
let whole = 0;
console.log(data.keys());
for (let i = 0; i < data.keys(); i++) {
  whole = whole + data[i];
}
console.log(whole / data.keys());
