/*
SIMPLE INTEREST

Simple Interest in Accounting is calculated as :

S.I. = (p * r * t) / 100
where p = principal amount
      r = rate of interest
      t = time
*/

function main() 
{ 

    var p = parseFloat(window.prompt("Enter Principal: ", ""));
    var r = parseFloat(window.prompt("Enter Rate: ", ""));
    var t = parseFloat(window.prompt("Enter Time: ", ""));
    console.log("Simple Interest is:", ((p * r * t) / 100))  
} 
main();

/*
INPUT : p = 1000, r = 8, t = 2
OUTPUT : Simple Interest is: 160.00
*/
