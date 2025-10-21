function somarDoisNumeros(num1, num2) {
  return num1 + num2;
}

let number1 = Number(prompt("Digite o primeiro número: "));
let number2 = Number(prompt("Digite o segundo número: "));


somarDoisNumeros(number1, number2);

// A ordem dos argumentos é importante!
// num1 receberá 10, num2 receberá 5
let novoResultado = somarDoisNumeros(number1, number2);

console.log("O resultado da soma é: " + novoResultado);