Na língua inglesa existe algumas métricas de legibilidade, que podem ser calculadas automaticamente a partir de um texto. O objetivo dessas métricas é classificar a dificuldade de leitura do texto e indicar qual o nível de instrução e idade que o leitor deve ter para compreender bem o texto. Essas métricas são úteis para reescrever um texto até que ele fique mais acessível.

Uma dessas métricas é a Automated readability index, que pode ser calculada a partir da seguinte fórmula:
<img src="https://s3.amazonaws.com/hr-assets/0/1657713107-bd3f5059f5-ari.png">
Seu objetivo neste desafio é escrever uma função simplificada para calcular o automated readability index. O resultado da fórmula deve ser arredondada para o próximo inteiro e seu valor máximo deve ser 14. Se o resultado da fórmula for, 10,4, por exemplo o retorno da função deve ser 11.

Input Format

A entrada da função será uma string que representa uma frase. O programa desenvolvido, portanto, não precisa lidar com múltiplas frases. O texto das frases usadas no desafio terá apenas letras e espaços, não é preciso lidar com pontuação ou letras acentuadas, também não é necessário lidar com números.
Uma frase terá no máximo 32 palavras e 512 letras.

Output Format

A função implementada deve retornar o valor calculado, entre 1 e 14.

Sample Input 0

And you may ask yourself Well how did I get here
Sample Output 0

1
Explanation 0

A frase tem 11 palavras e 38 letras

4.71 * 38 / 11 ~= 16.27

0.5 * 11 = 5.5

16.27 + 5.5 - 21.43 = 0.34

Arredondando 0.34 para o próximo número inteiro temos o resultado 1.

Sample Input 1

The latter consisted simply of six hydrocoptic marzelvanes so fitted to the ambifacient lunar waneshaft that side fumbling was effectively prevented
Sample Output 1

14
Explanation 1

A frase tem 21 palavras e 128 letras

4.71 * 128 / 21 ~= 28.70

0.5 * 21 = 10.5

28.70 + 10.5 - 21.43 = 17.77

Arredondando 17.77 para o próximo número inteiro obtemos o valor 18, mas o valor mais alto da escala é 14, portanto o resultado final é 14.
