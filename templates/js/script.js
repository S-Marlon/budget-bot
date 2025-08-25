// if (data selecionada === null, entao adcionar data do dict, se nao adcionar a data personalizada)

var currentdate = new Date()
document.querySelector('.data').textContent = 
currentdate.getDate() + "/" + (currentdate.getMonth()+1)  + "/" + currentdate.getFullYear()

// if (localização selecionada === null, entao adcionar data do dcit, se nao adcionar a localização personalizada)

document.querySelector('.localizacao').textContent = currentdate.getDate() + "/" + currentdate.getMonth() + "/" + currentdate.getFullYear()

// if (checks no dicrt, entao aparecer a respectiva, se nao dar um display.vlock/ ocultar )
// document.querySelector('.localizacao').textContent = 

// atribui qtd metros perfurados
metrosPerfurados = 12345

document.getElementsByClassName("#valorPerfurado").textContent = metrosPerfurados



// inclusos ---------------------------------------------------------------------------------------
 document.addEventListener('DOMContentLoaded', async function() {
     await fetch('../budget/selecionados.json')
         .then(response => response.json())
         .then(checks => {

            checks = checks.extras.inclusos

            console.log("checks: "+ checks);

     if (checks != null){
    const tabela = document.getElementById('checks');
    var n = 0
    checks.forEach(e => {
            const td = document.createElement('td');
            
            var valor = 100/checks.length
            
            // verificar quantidade de objetos em checks, atualmente apenas da undefined
            // dividir igualmente
            td.style.width = `${valor}%` 
            
            td.innerHTML = `<span> <strong>✓</strong> ${checks[n]} </span> `
            tabela.appendChild(td);
            n++
        });
    }

}
         )
        });
// inclusos ---------------------------------------------------------------------------------------
// miudas ----------------------------------------------------------------------------------------


 document.addEventListener('DOMContentLoaded', async function() {
     await fetch('../budget/selecionados.json')
         .then(response => response.json())
         .then(miudas => {

            miudas = miudas.extras.miudas

           

                if (miudas != null){
                const tabela = document.getElementById('miudas');
                var n = 0
                miudas.forEach(e => {
                        const fieldset = document.createElement('fieldset');
                        if (n == 0) {
                            fieldset.style.borderTop = "none"
                            fieldset.style.color = "red"
                            fieldset.innerHTML = `<em> ${miudas[n]} </em> `
                        } else {
                            fieldset.style.borderTop = "none"
                            fieldset.style.textAlign = "center"
                            fieldset.innerHTML = `<strong> ${miudas[n]} </strong> `
                        }
                        tabela.appendChild(fieldset);
                        n++
                    });
                }

}
         )
        });


// miudas ---------------------------------------------------------------------------------------- 
// pagamento ----------------------------------------------------------------------------------------


 document.addEventListener('DOMContentLoaded', async function() {
     await fetch('../budget/selecionados.json')
         .then(response => response.json())
         .then(pagamento => {

            pagamento = pagamento.extras.forma_pagamento
            console.log("pagamento: "+ pagamento);
           

                if (pagamento != null){
                const tabela = document.getElementById('condicoes-pagamento');
                var n = 0
                
                        const li = document.createElement('span');
                       
                            li.innerHTML = `<li><strong>Forma de Pagamento:</strong> ${pagamento.entrada} de Entrada: R$${ pagamento.valor_entrada },00 ,e saldo em até ${pagamento.saldo.parcelas}vezes no valor de  R$${ pagamento.saldo.valor_parcela }, no ${pagamento.saldo.metodo} em ${pagamento.saldo.prazo}</li>
                            <li><strong>Data de início:</strong> á Combinar </li>
                            <li><strong>Prazo de Execução:</strong> 7 Dias </li>
                            <li><strong>Validade da Proposta:</strong> 7 Dias </li>


                             `
                       
                        tabela.appendChild(li);

                        
                        n++
                   
                }

}
         )
        });


//   "forma_pagamento":[
//     {
//       "entrada": "30%",
//       "valor_entrada": 5478.00,
//       "saldo": {
//         "parcelas": 3,
//         "valor_parcela": 4260.66,
//         "prazo": ["30 dias", "60 dias", "90 dias"],
//         "metodo": "boleto"
//       }
//     },
//     {
//       "entrada": "50%",
//       "valor_entrada": 9130.00,
//       "saldo": {
//         "parcelas": 10,
//         "valor_parcela": 913.00,
//         "metodo": "cartao",
//         "juros": "sem juros"
//       }
//     },
//     {
//       "entrada": "50%",
//       "valor_entrada": 9130.00,
//       "saldo": {
//         "parcelas": 4,
//         "valor_parcela": 2282.50,
//         "prazo": ["30 dias", "60 dias", "90 dias", "120 dias"],
//         "metodo": "boleto"
//       }
//     },
//     {
//       "condicao": "a vista",
//       "desconto": "3%",
//       "valor_final": 17712.20
//     }
//   ]
// pagamento ---------------------------------------------------------------------------------------- 
topicos = ["prospeccao","Perfuracao","revestimento","equipamentos","Instalação","documentacao","Extras"]

un = 1
let incluso = true
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

                                if (incluso == true) {
                                    console.log("incluso é true");
                                    
                                     tr.innerHTML = `
                                    <td style="width: 8%;">${((um + idx) / 10) + un}</td>
                                    <td style="width: 42%;" class="descricao">${detalhesEquipamento.descricao ?? '-'}</td>
                                    <td style="width: 18%;">${detalhesEquipamento.quantidade ?? '-'}</td>
                                    <td style="width: 15%;">R$ ${detalhesEquipamento.valor ?? '-'}</td>
                                    <td style="width: 8.5%;" class="total" ><del>R$ ${detalhesEquipamento.valor * detalhesEquipamento.quantidade ?? '-'}</del></td>
                                    <td style="width: 8.5%;" class="totalincluso"><ins>INCLUSO<ins></td>
                                `;
                                }else{
                                    console.log("incluso é Façse");

                                    tr.innerHTML = `
                                    <td style="width: 8%;">${((um + idx) / 10) + un}</td>
                                    <td style="width: 42%;" class="descricao">${detalhesEquipamento.descricao ?? '-'}</td>
                                    <td style="width: 18%;">R$ ${detalhesEquipamento.quantidade ?? '-'}</td>
                                    <td style="width: 15%;">R$ ${detalhesEquipamento.valor ?? '-'}</td>
                                    <td style="width: 17%;" class="total">${detalhesEquipamento.valor * detalhesEquipamento.quantidade ?? '-'}</td>
                                `;
                                }

                                
                                if (um % 2 === 0) {
                                    tr.style.backgroundColor = "#f5f5f5";
                                }else{
                                    tr.style.backgroundColor = "white";
                                }
                                tbody.appendChild(tr);
                                
                                console.log("um: " +um)
                                um++;
                            }
                            
                        } else if (key === "equipamentos" &&  nomeEquipamento in item === null) {
                            log("Item é nulo, não adicionando à tabelaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
                        } else {
                        
                        const tr = document.createElement('tr');
                        var medida = 'unidade';
                            if (key === "perfuracao") {
                            medida = 'metro';
                            }
                            if (item.quantidade > 1){
                                medida = 'unidades';
                            }

                        tr.innerHTML = `
                            <td style="width: 8%;">${((1 +  idx)/10) + un}</td>
                            <td style="width: 42%;" class="descricao">${item.descricao ?? '-'}</td>
                            <td style="width: 18%;">${item.quantidade ?? '-'} (${medida})</td>
                            <td style="width: 15%;">R$ ${item.valor ?? '-'}</td>
                            <td style="width: 17%;" class="total">R$ ${item.valor * item.quantidade ?? '-'}</td>
                        `;
                        var result = (1 +  idx) % 2
                        console.log("result: " + result)
                        if (result === 0) {
                                    tr.style.backgroundColor = "#f5f5f5";
                                }else{
                                    tr.style.backgroundColor = "white";
                                }
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
   