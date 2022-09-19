infile = open('info_security.txt', 'r')
outfile = open('encrypted.txt', 'w')

codes = {'A' : '%', 'a' : '9', 'B' : '@', 'b' : '3', 'C' : '!', 'c' : '8', 'D' : '$', 
'd' : '7', 'E' : '*', 'e' : '4', 'F' : '#', 'f' : '6', 'G' : '&', 'g' : '2', 'H' : '^', 
'h' : '1', 'I' : '=', 'i' : '2', 'J' : '+', 'j' : '5', 'K' : '~', 'k' : '0', 'L' : '-', 
'l' : '?', 'M' : '/', 'm' : '"', 'N' : '|', 'n' : '{', 'O' : '}', 'o' : '[', 'P' : ']', 
'p' : '<', 'Q' : '//', 'q' : '~~', 'R' : '_', 'r' : '>', 'S' : ':', 's' : ';', 'T' : '(', 
't' : ')', 'U' : '&&', 'u' : '$$', 'V' : '**', 'v' : '##', 'W' : '_-', 'w' : '-_', 'X' : '@@', 
'x' : '!!', 'Y' : '??', 'y' : '::', 'Z' : '++', 'z' : '=='} 

for line in infile:
    encrypted = ''.join(codes.get(c, c) for c in line)
    outfile.write(encrypted)
outfile.close()