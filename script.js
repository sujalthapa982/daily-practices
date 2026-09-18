console.log("hey")
let array = ["apple", "banana", "mango"]
console.log(array[0]);
console.log(array[1]);
console.log(array[2]);


console.log()
array.push("orange");
for(let i=0; i<array.length; i++){
    console.log(array[i])
}

array.pop();
console.log(array);
array.unshift("banana");
console.log(array);
console.log(array.length);
const data = [{name: "sujal", age: 20},
                                        {name: "anjali", age: 19}]
console.log(data)
console.log(data[1])
console.log(data[1].age)
console.log(data[1].name)


