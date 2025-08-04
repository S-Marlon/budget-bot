
topicos = ["prospeccao","Perfuracao","revestimento","equipamentos","Instalação","documentacao","Extras"]
// equip = ["Bomba","Tampa de poço","Painel","Cabos el\u00e9tricos submersos","V\u00e1lvula de reten\u00e7\u00e3o","V\u00e1lvula de reten\u00e7\u00e3o","Corda Submersa","Hidr\u00f4metro","Cimenta\u00e7\u00e3o"]
// const modeloItensEquipamentos = {
//   "Bomba": { "descricao": "Bomba 2cv", "quantidade": 1, "valor": 1500.00 },
//   "Tampa de poço": { "descricao": "Tampa de PVC", "quantidade": 1, "valor": 250.00 },
//   "Painel": { "descricao": "Painel de controle", "quantidade": 1, "valor": 300.00 }
//   // ... e assim por diante
// };
un = 1
document.addEventListener('DOMContentLoaded', async function() {
    await fetch('../budget/dados.json')
        .then(response => response.json())
        .then(data => {

            console.log("antes do for "+ Object.keys(data));
             for (let key in data) {
                if (Array.isArray(data[key])) {
                    console.log("a chave é " + key);
                    
                    // Exemplo: monta id da tabela igual ao nome da key
                    const tabela = document.getElementById(key + '-tabela');
                    if (!tabela) continue; // pula se não existir tabela para essa key
                    const tbody = tabela.getElementsByTagName('tbody')[0];
                    tbody.innerHTML = '';
                    data[key].forEach((item, idx) => {
                        if (key === "equipamentos") {
                            var um = 1;
                            // Itera sobre cada chave dentro do objeto 'item' (ex: "Bomba")
                            for (const nomeEquipamento in item) {
                                // Acessa o objeto de detalhes do equipamento (ex: { descricao: "...", ... })
                                const detalhesEquipamento = item[nomeEquipamento];

                                console.log("equipamento: " + nomeEquipamento);
                                console.log("equipamento.descricao: " + detalhesEquipamento.descricao);
                                
                                const tr = document.createElement('tr');

                                tr.innerHTML = `
                                    <td style="width: 8%;">${((um + idx) / 10) + un}</td>
                                    <td style="width: 42%;">${detalhesEquipamento.descricao ?? '-'}</td>
                                    <td style="width: 15%;">${detalhesEquipamento.quantidade ?? '-'}</td>
                                    <td style="width: 15%;">${detalhesEquipamento.valor ?? '-'}</td>
                                    <td style="width: 20%;" class="total">${detalhesEquipamento.valor * detalhesEquipamento.quantidade ?? '-'}</td>
                                `;

                                tbody.appendChild(tr);
                                um++;
                            }
                        } else if (key === "equipamentos" &&  nomeEquipamento in item === null) {
                            log("Item é nulo, não adicionando à tabelaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
                        } else {

                        const tr = document.createElement('tr');
                        tr.innerHTML = `
                            <td style="width: 8%;">${((1 +  idx)/10) + un}</td>
                            <td style="width: 42%;">${item.descricao ?? '-'}</td>
                            <td style="width: 15%;">${item.quantidade ?? '-'}</td>
                            <td style="width: 15%;">${item.valor ?? '-'}</td>
                            <td style="width: 20%;" class="total">${item.valor * item.quantidade ?? '-'}</td>
                        `;
                        tbody.appendChild(tr);
                        }
                       
                    });
                    un++
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


               
            