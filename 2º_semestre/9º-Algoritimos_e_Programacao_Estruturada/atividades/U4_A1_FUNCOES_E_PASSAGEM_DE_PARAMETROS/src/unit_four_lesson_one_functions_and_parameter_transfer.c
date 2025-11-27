#include <stdio.h>

// Funcao para calcular o salario bruto
float calcular_salario_bruto(float valor_hora, int horas_trabalhadas) {
    return valor_hora * horas_trabalhadas;
}

// Funcao para calcular o desconto de 9%
float calcular_desconto(float salario_bruto) {
    return salario_bruto * 0.09;
}

// Funcao para calcular o salario liquido
float calcular_salario_liquido(float salario_bruto, float desconto) {
    return salario_bruto - desconto;
}

int main() {
    float valor_hora, salario_bruto, desconto, salario_liquido;
    int horas_trabalhadas;
    
    printf("\n");
    printf("=== 💻 SISTEMA DE CÁLCULO DE SALÁRIO 💻 ===\n\n");
    
    // Solicita os dados do usuario
    printf("💲 Digite o valor da hora trabalhada: R$ ");
    scanf("%f", &valor_hora);
    
    printf("⌚ Digite a quantidade de horas trabalhadas no mês: ");
    scanf("%d", &horas_trabalhadas);
    
    // Chama as funcoes para realizar os calculos
    salario_bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas);
    desconto = calcular_desconto(salario_bruto);
    salario_liquido = calcular_salario_liquido(salario_bruto, desconto);
    
    // Exibe os resultados
    printf("\n=== RESULTADO DOS CÁLCULOS ===\n");
    printf("Salário bruto: R$ %.2f\n", salario_bruto);
    printf("Desconto (9%%): R$ %.2f\n", desconto);
    printf("Salário líquido: R$ %.2f\n", salario_liquido);
    printf("\n✅ Programa encerrado.\n");
    printf("\n");
    
    return 0;
}