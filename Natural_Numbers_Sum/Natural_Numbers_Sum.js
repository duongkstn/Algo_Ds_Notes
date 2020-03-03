/*
    Sum of First N Natural Numbers

    The task is to find sum of first n natural numbers, where n is 
    the number input to us. We use the well known formula,
    sum = n * (n + 1)/2 to compute the sum
*/

num = parseInt(window.prompt("Enter N: ", ""));
ans = num * (num + 1) / 2
console.log("The sum of first", num, "natural numbers is :", ans)

/*
    Input : num = 6
    Output : The sum of first 6 natural numbers is : 21
*/
