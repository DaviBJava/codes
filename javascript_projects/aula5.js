// 1. Peça ao usuário para digitar a hora atual (apenas a hora, de 0 a 23).
// Lembre-se de converter para Number!
let hora = Number(prompt("Que horas são agora? (Digite apenas a hora, ex: 14)"));

// 2. Use a estrutura if / else if / else para decidir a mensagem.
if (hora >= 5 && hora < 12) {
  alert("Bom dia!");
} else if (hora >= 12 && hora < 18) {
  alert("Boa tarde!");
} else {
  // Consideramos que o resto (18 a 23 e 0 a 4) é noite.
  alert("Boa noite!");
}

console.log("Programa finalizado.");