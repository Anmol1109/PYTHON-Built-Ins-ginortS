# Enter your code here. Read input from STDIN. Print output to STDOUT
print(*sorted(input(), key = lambda i : (i.isdigit() - i.islower(), i in '02468',i)),sep = '')
