const array = [12,23,34,1,13]
const filter = array.filter((i) => i>20)
console.log(filter)

const names = ["sujal", "anjali", "preetam"]
const result = names.filter((name) => name.length<7)
console.log(result)

const product = [
    {Name :"sujal", expense: "1000"},
    {Name :"anjali", expense: "3000"},
    {Name :"preetam", expense: "90000"}
]
const expenses = product.filter(
    (exp) => exp.expense<2000
)
console.log(expenses)