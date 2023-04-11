# Define o número que queremos verificar se está na sequência de Fibonacci
numero = 21

# Inicia a sequência de Fibonacci com os primeiros dois números
fibonacci = [0, 1]

# Loop para calcular a sequência de Fibonacci até que o último número seja maior ou igual ao número informado
while fibonacci[-1] < numero:
    # Calcula o próximo número na sequência de Fibonacci como a soma dos dois números anteriores
    proximo = fibonacci[-1] + fibonacci[-2]
    # Adiciona o próximo número na sequência de Fibonacci à lista
    fibonacci.append(proximo)

# Verifica se o número informado está na sequência de Fibonacci
if numero in fibonacci:
    print(f'O número {numero} está na sequência de Fibonacci.')
else:
    print(f'O número {numero} não está na sequência de Fibonacci.')
    
   #Explicação: Neste exemplo, iniciamos definindo o número que queremos verificar se está na sequência de Fibonacci como numero = 21. Em seguida, definimos a sequência de Fibonacci inicialmente como [0, 1].

Usando um loop while, continuamos a calcular a sequência de Fibonacci até que o último número na lista seja maior ou igual ao número informado. Para cada iteração do loop, calculamos o próximo número na sequência de Fibonacci como a soma dos dois números anteriores e adicionamos o resultado à lista de Fibonacci.

Por fim, verificamos se o número informado está na lista de Fibonacci usando um if statement. Se o número estiver na lista, imprimimos uma mensagem indicando que o número está na sequência de Fibonacci. Caso contrário, imprimimos uma mensagem indicando que o número não está na sequência de Fibonacci.
