document.addEventListener('DOMContentLoaded', () => {
    const numbersGrid = document.getElementById('numbersGrid');
    const selectedNumbersDiv = document.getElementById('selectedNumbers');
    const confirmButton = document.getElementById('confirmButton');
    const BASE_URL = 'http://localhost:5000';


    // Gerar botões numerados de 1 a 60 dinamicamente
    for (let i = 1; i <= 60; i++) {
        const button = document.createElement('button');
        button.className = 'number';
        button.textContent = padNumber(i); // Função para formatar o número com dois dígitos (ex: 01, 02, ..., 60)
        button.onclick = () => toggleNumberSelection(button, i);
        numbersGrid.appendChild(button);
    }

    let selectedNumbers = [];

    function toggleNumberSelection(button, number) {
        const index = selectedNumbers.indexOf(number);
        if (index !== -1) {
            // Se o número já foi selecionado, remova-o da lista e restaure o estilo
            selectedNumbers.splice(index, 1);
            button.classList.remove('selected');
        } else {
            // Verifique se já há entre 6 e 9 números selecionados
            if (selectedNumbers.length >= 9) {
                alert('Você só pode selecionar no máximo 9 números!');
                return;
            }

            // Adicione o número à lista de selecionados e aplique o estilo selecionado
            selectedNumbers.push(number);
            button.classList.add('selected');
        }

        // Atualize a lista de números selecionados exibida abaixo da cartela
        displaySelectedNumbers();

        // Verifique se o botão de confirmação deve ser habilitado
        updateConfirmButton();
    }
    // Função para exibir os números selecionados
    function displaySelectedNumbers() {
        const selectedCount = selectedNumbers.length;

        // Atualiza o texto exibido abaixo da cartela
        selectedNumbersDiv.textContent = 'Números selecionados: ' + selectedNumbers.sort((a, b) => a - b).join(', ');

        // Atualiza a classe dos botões com base no número de seleções
        const numberButtons = document.querySelectorAll('.number');
        numberButtons.forEach(button => {
            const number = parseInt(button.textContent);
            const isSelected = selectedNumbers.includes(number);

            if (selectedCount < 6) {
                button.classList.toggle('selected', isSelected);
                button.classList.toggle('minimum-selected', isSelected);
            } else {
                button.classList.toggle('selected', isSelected);
                button.classList.toggle('minimum-selected', false);
            }
        });
    }

    // Função para verificar e habilitar/desabilitar o botão de confirmação
    function updateConfirmButton() {
        confirmButton.disabled = selectedNumbers.length < 6;
    }

    // Função para confirmar a seleção (a ser chamada quando o botão Confirmar for clicado)
    confirmButton.addEventListener('click', () => {
        const API_URL = `${BASE_URL}/conferir`;
        fetch(API_URL, {
            method: 'POST',
            headers: {'Content-Type': 'application/json',},
            body: JSON.stringify({numbers: selectedNumbers}),
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Erro ao enviar os números selecionados.');
        })
        .then(data => {
            let html = '<h3>Resultados dos jogos:</h3><br>';
            if (data.result.length === 0) {
                html += '<p>Nenhum houve acertos.</p>';
            } else {
                for(let i = 0; i < data.result.length; i++){
                    html += `<p>${data.result[i]['data']} - ${data.result[i]['premiacao']}</p>`;
                }
            }
            document.getElementById('resultados').innerHTML = html;
            alert('Cartela enviada com sucesso!');
            // Limpar a seleção após o envio bem-sucedido (opcional)
            selectedNumbers = [];
            displaySelectedNumbers();
            updateConfirmButton();
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao enviar os números selecionados.');
        });

    });

    // Função para formatar o número com dois dígitos (ex: 01, 02, ..., 60)
    function padNumber(num) {
        return num.toString().padStart(2, '0');
    }
});