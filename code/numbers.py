'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''

integers = {'odd': [], 'even': []}
while True:
    integer = int(input("Enter an integer: ", ))
    if integer == 0:
        break
    elif integer % 2 == 0:
        integers['even'].append(integer)
    else:
        integers['odd'].append(integer)
print(integers)