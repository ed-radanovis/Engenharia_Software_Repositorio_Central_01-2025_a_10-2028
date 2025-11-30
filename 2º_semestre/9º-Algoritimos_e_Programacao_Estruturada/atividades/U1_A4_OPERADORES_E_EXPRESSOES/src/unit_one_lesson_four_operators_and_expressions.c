#include <stdio.h>

int main() {
    int num1, num2, num3;
    
    // Solicita três números inteiros ao usuário
    printf("\nDigite três números inteiros separados por vírgula (ex: 1,2,3):\n");
    scanf("%d, %d, %d", &num1, &num2, &num3);
    
    // 1. Operações Aritméticas
    printf("\n=== OPERAÇÕES ARITMÉTICAS ===\n");
    printf("Soma: %d + %d + %d = %d\n", num1, num2, num3, num1 + num2 + num3);
    printf("Subtração: %d - %d - %d = %d\n", num1, num2, num3, num1 - num2 - num3);
    printf("Multiplicação: %d * %d * %d = %d\n", num1, num2, num3, num1 * num2 * num3);
    
    // Verifica divisão por zero
    if(num2 != 0 && num3 != 0) {
        printf("Divisão: %d / %d / %d = %.2f\n", num1, num2, num3, (float)num1 / num2 / num3);
    } else {
        printf("Divisão: Não é possível dividir por zero!\n");
    }
    
    // 2. Operadores Relacionais
    printf("\n=== OPERADORES RELACIONAIS ===\n");
    printf("%d > %d: %s\n", num1, num2, num1 > num2 ? "Verdadeiro" : "Falso");
    printf("%d < %d: %s\n", num2, num3, num2 < num3 ? "Verdadeiro" : "Falso");
    
    // 3. Operadores Lógicos
    printf("\n=== OPERADORES LÓGICOS ===\n");
    int condicao1 = num1 > 0;        // Primeiro número é positivo
    int condicao2 = num2 % 2 == 0;   // Segundo número é par
    
    printf("Primeiro número é positivo: %s\n", condicao1 ? "Sim" : "Não");
    printf("Segundo número é par: %s\n", condicao2 ? "Sim" : "Não");
    
    if(condicao1 && condicao2) {
        printf("MENSAGEM ESPECIAL: Ambas as condições são verdadeiras!\n");
        printf("O primeiro número é positivo e o segundo número é par.\n");
        printf("\n");
    } else {
        printf("As duas condições não foram satisfeitas simultaneamente.\n");
        printf("\n");
    }
    
    return 0;
}