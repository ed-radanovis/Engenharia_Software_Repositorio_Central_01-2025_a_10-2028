#include <stdio.h>

int main() {
    // Declaracao do vetor para armazenar 5 numeros inteiros
    int vendas[5];
    int soma = 0;
    
    printf("\n");
    printf("=== 💻 SISTEMA DE CONTROLE DE VENDAS DIÁRIAS 💻 ===\n");
    printf("Informe abaixo as vendas realizadas dia a dia no período de 5 dias:\n\n");
    
    // Leitura dos valores fornecidos pelo usuario
    for(int i = 0; i < 5; i++) {
        printf("⌨ Digite as vendas do dia %d: ", i + 1);
        scanf("%d", &vendas[i]);
    }
    
    // Calculo da soma dos elementos do vetor
    for(int i = 0; i < 5; i++) {
        soma += vendas[i];
    }
    
    // Exibicao dos elementos do vetor e soma total
    printf("\n=== 📋 RELATORIO DE VENDAS 📊 ===\n");
    printf("Vendas por dia:\n");
    
    for(int i = 0; i < 5; i++) {
        printf("Dia %d: %d vendas\n", i + 1, vendas[i]);
    }
    
    printf("\n=== TOTAL GERAL ===\n");
    printf("Soma total de vendas: %d\n", soma);
    printf("✅ Programa encerrado.\n");
    printf("\n");
    
    return 0;
}