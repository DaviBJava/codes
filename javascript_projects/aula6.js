// 1. Peça ao usuário um número para iniciar a contagem.
let numeroInicial = Number(prompt("Iniciar contagem regressiva a partir de:"));

// 2. Use um loop 'for' para contar DE TRÁS PRA FRENTE.
// A inicialização é o número do usuário.
// A condição é 'enquanto o contador for >= 1'.
// O incremento na verdade será um DECREMENTO (contador--).
for (let i = numeroInicial; i >= 1; i--) {
  console.log(i);
  alert(i); // Usando alert para ficar mais interativo
}

// 3. Exiba a mensagem final.
alert("Lançar! 🚀");