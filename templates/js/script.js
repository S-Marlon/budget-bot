document.addEventListener('DOMContentLoaded',async function() {
await fetch('budget.json')
    .then(response => response.json())
    .then(data => {
        // const budgetList = document.getElementById('budget-list');
        
        //     const listItem = document.createElement('li');
        //     listItem.textContent = `${data.cliente.nome}: ${data.cliente.cidade} o brab`;
        //     budgetList.appendChild(listItem);

            document.getElementById("cliente-nome").textContent = data.cliente.nome;
            document.getElementById("cliente-local").textContent = data.cliente.local + " - " + data.cliente.cidade;
        
    }

).catch(error => {
        console.error('Error fetching budget data:', error);
});

});