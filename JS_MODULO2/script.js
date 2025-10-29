// 1. Selecione o H1 pelo seu ID
let titulo = document.getElementById("titulo");
console.log("Elemento H1:", titulo);

// 2. Selecione os itens da lista pela sua CLASSE 'item'
let itensComClasse = document.getElementsByClassName("item");
console.log("Elementos com a classe 'item':", itensComClasse);

// 3. Selecione o PRIMEIRO item dessa lista
let primeiroItem = itensComClasse[0];
console.log("O primeiro item da classe 'item' é:", primeiroItem);

// 4. Selecione TODOS os <li> pela TAG
let todosOsItensDaLista = document.getElementsByTagName("li");
console.log("Todos os elementos <li>:", todosOsItensDaLista);


// 5. Mostre o texto de todos os itens com um loop
console.log("--- Mostrando o texto de todos os itens com um loop ---");
for (let i = 0; i < itensComClasse.length; i++) {
  console.log(itensComClasse[i].innerText);
}