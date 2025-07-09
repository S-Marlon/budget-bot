topicos = ["Prospeccao","Perfuracao","Estrutura","equipamentos","Instalação","Documentação","Extras"]

document.addEventListener('DOMContentLoaded', async function() {
    await fetch('budget.json')
        .then(response => response.json())
        .then(data => {

            console.log("antes do for "+ Object.keys(data));
             for (let key in data) {
                if (Array.isArray(data[key])) {
                    console.log("a chave é" + key);
                    
                    // Exemplo: monta id da tabela igual ao nome da key
                    const tabela = document.getElementById(key + '-tabela');
                    if (!tabela) continue; // pula se não existir tabela para essa key
                    const tbody = tabela.getElementsByTagName('tbody')[0];
                    tbody.innerHTML = '';
                    data[key].forEach((item, idx) => {
                        const tr = document.createElement('tr');
                        tr.innerHTML = `
                            <td style="width: 8%;">${idx + 1}</td>
                            <td style="width: 42%;">${item.descricao ?? '-'}</td>
                            <td style="width: 15%;">${item.quantidade ?? '-'}</td>
                            <td style="width: 15%;">${item.valor ?? '-'}</td>
                            <td style="width: 20%;" class="total">${item.valor * item.quantidade ?? '-'}</td>
                        `;
                        tbody.appendChild(tr);
                    });
                }
            }

    
        });
        totalizacao();
})

function totalizacao() {
     let somaTotal = 0;
document.querySelectorAll(".total").forEach(e =>{
     const valor = Number(e.textContent.replace(/[^\d.,-]/g, '').replace(',', '.'));
    if (!isNaN(valor)) somaTotal += valor;
});
document.querySelector("#valor_calculado").textContent = somaTotal
}
   





        // // const budgetList = document.getElementById('budget-list');
        
        // //     const listItem = document.createElement('li');
        // //     listItem.textContent = `${data.cliente.nome}: ${data.cliente.cidade} o brab`;
        // //     budgetList.appendChild(listItem);

        //     document.getElementById("cliente-nome").textContent = data.cliente.nome;
        //     document.getElementById("cliente-local").textContent = data.cliente.local + " - " + data.cliente.cidade;
        //     for(let key in data.prospeccao){

        //         if (data.prospeccao[key] == true) {
        //             console.log("Visita Técnica está marcada como true");
        //                 const listItem = document.createElement('li');
        //                 listItem.textContent = `✓ v${key.replace(/_/g, ' ')}`;
        //                 document.getElementById("listagem").appendChild(listItem).style.textTransform = "capitalize";
        //         }
        //     }


        //     // perfuração
        //         const listItem = document.createElement('td');
        //         listItem.textContent = `${data.perfuração.metros_perfuração} m`;
        //         document.getElementById("perfuração").appendChild(listItem);
                
        //         const priceItem = document.createElement('td');
        //         priceItem.textContent = `R$ ${data.perfuração.preco_por_metro}`;
        //         document.getElementById("perfuração").appendChild(priceItem);
                
        //         const totalItem = document.createElement('td');
        //         totalItem.textContent = `R$ ${data.perfuração.metros_perfuração * data.perfuração.preco_por_metro}`;
        //         document.getElementById("perfuração").appendChild(totalItem);

        //         if (data.perfuração.uso_martelo_fundo == true) {
        //             const marteloItem = document.createElement('tr');
        //             marteloItem.innerHTML = '<td colspan="4">* perfuração com uso de Martelo de Fundo (DTH)</td>';
        //             document.querySelector('table').appendChild(marteloItem);
        //         } else{
        //             const marteloItem = document.createElement('tr');
        //             marteloItem.innerHTML = '<td colspan="4">* perfuração com uso de Bomba de lama</td>';
        //             document.querySelector('table').appendChild(marteloItem);
        //         }
        //     // perfuração

        //     // tubulação 
            
        //     const tubulacao_diametroItem = document.createElement('td');
        //         tubulacao_diametroItem.textContent = `${data.estrutura_poco.tubulacao_diametro} `;
        //         document.getElementById("estrutura").appendChild(tubulacao_diametroItem);
                
        //         const tubulacao_metrosItem = document.createElement('td');
        //         const metrosOriginal = data.perfuração.metros_perfuração;
        //         const metrosArredondado = Math.ceil(metrosOriginal / 6) * 6;
        //         tubulacao_metrosItem.textContent = ` ${metrosArredondado} m`;
        //         document.getElementById("estrutura").appendChild(tubulacao_metrosItem);
                
        //         const valor_tuboItem = document.createElement('td');
        //         let valor_tubo = 150; // Valor unitário do tubo
        //         valor_tuboItem.textContent = `R$ ${valor_tubo}`;
        //         document.getElementById("estrutura").appendChild(valor_tuboItem);

        //         const filtro_fundoItem = document.createElement('td');
        //         filtro_fundoItem.textContent = `R$ ${(metrosArredondado/6) * valor_tubo}`;
        //         document.getElementById("estrutura").appendChild(filtro_fundoItem);

        //     // tubulação 
        //     // equipamentos

        //         const BombaItem = document.createElement('td');
        //         BombaItem.textContent = ` Bomba submersa ${data.equipamentos.bomba_submersa.potencia_cv} Hp`;
        //         document.getElementById("bomba").appendChild(BombaItem);

        //         const calor = document.createElement('td');
        //         calor.textContent = ` R$ ${900}`;
        //         document.getElementById("bomba").appendChild(calor);

        //         const calor2 = document.createElement('td');
        //         calor2.textContent = `R$ ${900}`;
        //         document.getElementById("bomba").appendChild(calor2);
                
        //         const calo32 = document.createElement('td');
        //         calo32.textContent = `R$ ${900}`;
        //         document.getElementById("painel").appendChild(calo32);

        //     // equipamentos


               
            