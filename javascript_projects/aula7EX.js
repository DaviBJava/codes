// 1. Crie um array vazio chamado 'tarefas'.
let tarefas = [];
console.log("Minha lista inicial:", tarefas);

// 2. Adicione 3 tarefas à lista usando .push()
tarefas.push("Estudar JavaScript");
tarefas.push("Lavar a louça");
tarefas.push("Passear com o cachorro");
console.log("Lista após adicionar tarefas:", tarefas);

// 3. Acesse e exiba no console a segunda tarefa da lista (índice 1).
console.log("A segunda tarefa da lista é:", tarefas[1]);

// 4. Altere a primeira tarefa (índice 0) para "Estudar JavaScript com mais foco!".
tarefas[0] = "Estudar JavaScript com mais foco!";
console.log("Lista após alteração:", tarefas);

// 5. Remova a última tarefa da lista usando .pop().
let tarefaRemovida = tarefas.pop();
console.log("A tarefa removida foi:", tarefaRemovida);
console.log("Lista final:", tarefas);

// 6. Exiba o tamanho final da lista.
console.log("Agora tenho", tarefas.length, "tarefas.");