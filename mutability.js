//mutability
let fruits = ["apple", "banana"]
fruits[0] = "mango"
console.log(fruits)

//immutability
const vehicles = ["car", "cycle", "train"]
const newvehicles = ["bike",...vehicles.slice(1)]
console.log(vehicles)
console.log(newvehicles)
