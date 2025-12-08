// 1. Selecione o H1 e mude seu texto
let titulo = document.querySelector("#titulo");
titulo.innerText = "Minha Página Manipulada!";
console.log(titulo);

// 3. Selecione a imagem e mude o 'src' e o 'alt'
let imagem = document.querySelector("#imagem-principal");
imagem.src = "https://placehold.co/150x150/0000FF/FFFFFF?text=Azul"; // Agora um quadrado azul
imagem.setAttribute("alt", "Quadrado azul criado pelo JS");

// 4. Selecione o container da lista e use 'innerHTML' para adicionar HTML
let listaContainer = document.querySelector("#lista-container");
listaContainer.innerHTML = `
  <h2>Minha Lista de Compras</h2>
  <ul>
    <li>Pão</li>
    <li>Leite</li>
    <li>Ovos</li>
  </ul>
`;

let aviso = document.querySelector("#aviso");

if (aviso.classList.contains("destaque")) {
  console.log("O aviso já está com o estilo!");
} else {
  console.log("O aviso está sem o estilo");
  aviso.classList.add("destaque");
}

if (aviso.classList.contains("destaque")) {
  console.log("O aviso já está com o estilo!");
} else {
  console.log("O aviso está sem o estilo");
  aviso.classList.add("destaque");
}
