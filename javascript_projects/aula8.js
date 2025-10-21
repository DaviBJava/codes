// 1. Declare uma função chamada 'calcularAreaRetangulo'.
// Ela deve aceitar dois parâmetros: 'largura' e 'altura'.
function calcularAreaRetangulo(largura, altura) {
  // 2. Dentro da função, calcule a área (largura * altura).
  let area = largura * altura;

  // 3. Faça a função RETORNAR o valor da área.
  return area;
}

// 4. Chame a função com os argumentos 10 e 5.
// Guarde o resultado em uma variável chamada 'areaCalculada'.
let areaCalculada = calcularAreaRetangulo(10, 5);

// 5. Exiba o resultado no console com uma mensagem clara.
console.log(`A área de um retângulo de 10x5 é ${areaCalculada}.`);

// 6. Chame a função novamente com outros valores e exiba o resultado.
let outraArea = calcularAreaRetangulo(20, 30);
console.log(`A área de um retângulo de 20x30 é ${outraArea}.`);