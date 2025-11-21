console.log("Welcome to the tip calculator!");

//Ask user for bill total
const billTotal = Number(prompt("What was the total bill? $"));

//Ask user how much in tips will be paid
const tip = Number(prompt("How much tip would you like to give? 10, 12, or 15? "));

//Ask user how many people will pay
const split = Number(prompt("How many people to split the bill? "));

//produce result
let payment_due = Math.round(billTotal * (1 + tip / 100) / split * 100) / 100

console.log(`Each person should pay: ${payment_due}`)
