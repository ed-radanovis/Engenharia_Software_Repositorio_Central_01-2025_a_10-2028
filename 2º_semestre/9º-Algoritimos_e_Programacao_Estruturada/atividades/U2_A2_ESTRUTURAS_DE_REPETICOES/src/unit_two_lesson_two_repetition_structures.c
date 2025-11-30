
// versão com while que atende aos requisitos solicitados
// #include <stdio.h>

// int main() {
//     int numero;
//     int soma = 0;

//     printf("\n");
//     printf("=== 📱 CALCULADORA DE SOMA 📱 ===\n");
//     printf("Digite números inteiros para somar.🔢\n");
//     printf("Digite 0 (zero) para encerrar e ver o resultado.\n\n");
    
//     // Solicita o primeiro número
//     printf("Digite um número: ");
//     scanf("%d", &numero);
    
//     // Estrutura de repetição while
//     while (numero != 0) {
//         // Soma o número digitado ao total
//         soma += numero;
        
//         // Solicita o próximo número
//         printf("Digite um número: ");
//         scanf("%d", &numero);
//     }
    
//     // Exibe o resultado final
//     printf("\n=== ✅ RESULTADO FINAL ✅ ===\n");
//     printf("A soma de todos os números digitados é: ... %d\n", soma, "📈");
//     printf("Programa encerrado. 🔚 \n");
//     printf("\n");
    
//     return 0;
// }


// // versão com do-while que evita duplicação de código
#include <stdio.h>

int main() {
    int numero;
    int soma = 0;
    
    printf("\n");
    printf("=== 📱 CALCULADORA DE SOMA 📱 ===\n");
    printf("Digite números inteiros para somar.🔢\n");
    printf("Digite 0 (zero) para encerrar e ver o resultado.\n\n");
    
    // Estrutura de repetição do-while
    do {
        printf("Digite um número: ");
        scanf("%d", &numero);
        
        if (numero != 0) {
            soma += numero;
        }
    } while (numero != 0);
    
    // Exibe o resultado final
    printf("\n=== ✅ RESULTADO FINAL ✅ ===\n");
    printf("A soma de todos os números digitados é: . . . %d\n", soma);
    printf("Programa encerrado.\n");
    printf("\n");
    
    return 0;
}