#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Space: the only space taken up is the variable a which is just continually reassigned
therefore there is a space complexity of O(c)

Time: n*n must be added together n times to be equal to n*n*n, therefore there is a time
complexity of O(n)

b) space: the only space taken up by the function is for sum and j. Both of these values
are simply updated and therefore there is a space complexity of O(n).

Time: There is a nested set of loops, and the inner loop will run for the same number of
iterations every time therefore there is an O(n^2)


c) Space: The function works recursively meaning that it has to establish itself for each
iteration and therefore there is an space complexity of O(bunnies)

Time: The recursive iterations are simply -1 each time meaning that the function will run
for 'bunnies' iterations. Therefore it has a time complexity of O(bunnies)

## Exercise II
A building and floors are like a pre-sorted list, therefore we can use an equivalent of
the binary search to find which floor will not break the egg:

Drop an egg from the middle floor, if it breaks move halfway to the bottom, if it
doesn't move halfway to the top. Keep repeating this pattern (replacing bottom and
top with the previous bounds) until you've gotten to just moving up or down one between
a floor that the egg breaks on and a floor that it doesn't. The floor where it doesn't
is the highest possible floor.

this should take log(n) drops on average where n is the height of the building.

For example in a seven story building where the egg breaks on anything higher than 6
(therefore the answer is 5) first drop from the fourth floor, the egg won't break, so
move up to the 6th floor and drop another egg, this time it will break so you move back down
to floor five, and drop the egg. This time it doesn't break, but since we've already checked
six we know this is the highest possible floor 
