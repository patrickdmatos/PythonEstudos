var = input('Digite algo: ');

print('O tipo primitivo desse valor é ', type(var));
print('só tem espaços? ',var.isspace());
print('é um numero? ', var.isnumeric());
print('é afabético? ', var.isalpha());
print('é alfanumerico? ', var.isalnum());
print('esta em maiusculo? ', var.isupper());
print('esta em minusculo? ', var.islower());
print('Está capitalizado? ', var.istitle());