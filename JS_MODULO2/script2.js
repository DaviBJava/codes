// 1. Selecione o 'Item 2' (li.item-destaque) usando querySelector
let itemDestaque = document.querySelector(".item-destaque");
console.log("Item Destaque:", itemDestaque);

// 2. A partir do 'itemDestaque', navegue para o PAI dele (a <ul>)
let lista = itemDestaque.parentElement;
console.log("O Pai do item é:", lista);

// 3. A partir do 'itemDestaque', navegue para o IRMÃO ANTERIOR
let itemAnterior = itemDestaque.previousElementSibling;
console.log("O irmão anterior é:", itemAnterior); // Item 1

// 4. A partir do 'itemDestaque', navegue para o PRÓXIMO IRMÃO
let proximoItem = itemDestaque.nextElementSibling;
console.log("O próximo irmão é:", proximoItem); // Item 3

// 5. Selecione o primeiro <p> dentro do 'footer' (exemplo de seletor complexo)
let copyright = document.querySelector(".footer p");
console.log("Texto do Copyright:", copyright);

// 6. Selecione todos os parágrafos dentro do 'footer' e exiba seus textos
let todosParagrafos = document.querySelectorAll(".footer p");
todosParagrafos.forEach((p) => {
  console.log("Texto do Parágrafo:", p.innerText);
});