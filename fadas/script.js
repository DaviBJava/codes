const items = [
    { name: "Capa Vermelha", clue: "Quem a vestia ao visitar a avó e encontrou um lobo falante?", story: "Chapeuzinho Vermelho", character: "Chapeuzinho Vermelho", image: "imagens/red_hood.png" },
    { name: "Pão / Farinha", clue: "Quem usou migalhas para tentar marcar o caminho e se perdeu na floresta?", story: "João e Maria", character: "João e Maria", image: "imagens/joao_e_maria.png" },
    { name: "Maçã Envenenada", clue: "Quem a mordeu e caiu em sono profundo, esperando um beijo de amor?", story: "Branca de Neve e os Sete Anões", character: "Branca de Neve", image: "imagens/branca_de_neve.png" },
    { name: "Feijões Mágicos", clue: "Quem os plantou no jardim e subiu em um caule gigante até a terra de um gigante?", story: "João e o Pé de Feijão", character: "João", image: "imagens/feijao.png" },
    { name: "Tijolos e Palha", clue: "Quem construiu casas diferentes para se proteger do Lobo Mau?", story: "Os Três Porquinhos", character: "Os Três Porquinhos", image: "imagens/porcos.png" },
    { name: "Relógio de Bolso", clue: "Quem corre atrás de um Coelho Branco, entrando em um buraco e em um mundo de loucuras?", story: "Alice no País das Maravilhas", character: "Alice", image: "imagens/alice.png" },
    { name: "Uma Rosa", clue: "Quem a amava muito e a protegia com um globo de vidro em seu pequeno planeta?", story: "O Pequeno Príncipe", character: "Pequeno Príncipe", image: "imagens/principe.png" },
    { name: "Chave Antiga", clue: "Quem a usou para abrir um portão secreto e encontrar um lugar cheio de vida e mistérios?", story: "O Jardim Secreto", character: "Mary Lennox", image: "imagens/jardim.png" },
    { name: "Um Machado", clue: "Quem a visitava e pedia suas partes (folhas, galhos, tronco) ao longo da vida para ser feliz?", story: "A Árvore Generosa", character: "O Menino", image: "imagens/generosa.png" },
    { name: "Um Rochedo", clue: "Quem era o leão que sentava no trono e ensinava seu filhote sobre o 'ciclo da vida'?", story: "O Rei Leão (Disney)", character: "Simba", image: "imagens/rei.png" }
];

// --- Elementos HTML ---
const rouletteWheel = document.getElementById('roulette-wheel');
const spinButton = document.getElementById('spin-button');
const gameArea = document.getElementById('game-area');
const clueText = document.getElementById('clue-text');
const revealButton = document.getElementById('reveal-button');
const characterImage = document.getElementById('character-image');
const storyName = document.getElementById('story-name');

let selectedItem = null; 
const numItems = items.length;
const degreesPerItem = 360 / numItems; // 36 graus por fatia (10 itens)


// Ação de Girar a Roleta
spinButton.addEventListener('click', () => {
    // 1. Resetar o estado da tela
    gameArea.style.display = 'block'; 
    revealButton.style.display = 'none';
    characterImage.style.display = 'none';
    storyName.style.display = 'none';
    clueText.textContent = "Girando...!"; 
    spinButton.disabled = true;

    // --- CORREÇÃO DE GIRO LENTO ---
    // A. Remove a transição (o giro para no lugar)
    rouletteWheel.style.transition = 'none';
    // B. Reseta o ângulo para 0deg para garantir um novo ponto de partida
    rouletteWheel.style.transform = 'rotate(0deg)';
    
    // Força o navegador a renderizar o reset antes do giro (fundamental)
    void rouletteWheel.offsetWidth; 
    
    // C. Re-adiciona a transição para que o próximo 'transform' seja animado
    rouletteWheel.style.transition = 'transform 5s cubic-bezier(0.25, 0.1, 0.25, 1)';
    // -----------------------------

    // 2. Lógica de Sorteio
    const randomIndex = Math.floor(Math.random() * numItems);
    selectedItem = items[randomIndex];

    // Calcula a rotação: 7 giros completos + rotação para centralizar o item sorteado no ponteiro.
    const rotationToStop = (randomIndex * degreesPerItem) + (degreesPerItem / 2);
    const totalRotation = (360 * 7) - rotationToStop; 
    
    // 3. Aplica o Giro (agora com a transição reativada)
    rouletteWheel.style.transform = `rotate(${totalRotation}deg)`;

    // 4. Exibe a Dica após a Roleta Parar
    setTimeout(() => {
        // Exibe o item sorteado e a dica na tela
        clueText.textContent = `Item Sorteado: ${selectedItem.name}. Dica: ${selectedItem.clue}`;
        revealButton.style.display = 'block';
        
        // Alerta: Apenas o nome do item
        alert(`O item sorteado é: ${selectedItem.name}`);
        
    }, 5100);
});


// Ação de Revelar a Resposta
revealButton.addEventListener('click', () => {
    if (selectedItem) {
        // Exibe o resultado final
        characterImage.src = selectedItem.image;
        characterImage.alt = `Personagem de ${selectedItem.story}`;
        characterImage.style.display = 'block';
        storyName.textContent = `Conto de Fadas: ${selectedItem.story} | Personagem: ${selectedItem.character}`;
        storyName.style.display = 'block';
        
        // Finaliza o turno
        revealButton.style.display = 'none';
        spinButton.disabled = false;
    }
});