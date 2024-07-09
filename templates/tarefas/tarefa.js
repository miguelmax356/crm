
    const cards = document.querySelectorAll('.kanban-card');
    const columns = document.querySelectorAll('.kanban-column');

    cards.forEach(card => {
        card.addEventListener('dragstart', dragStart);
        card.addEventListener('dragend', dragEnd);
    });

    columns.forEach(column => {
        column.addEventListener('dragover', dragOver);
        column.addEventListener('drop', drop);
    });

    function dragStart(e) {
        e.dataTransfer.setData('text/plain', e.target.id);
        setTimeout(() => e.target.classList.add('invisible'), 0);
    }

    function dragEnd(e) {
        e.target.classList.remove('invisible');
    }

    function dragOver(e) {
        e.preventDefault();
    }

    function drop(e) {
        e.preventDefault();
        const id = e.dataTransfer.getData('text');
        const card = document.querySelector(`[id='${id}']`);
        const column = e.target.closest('.kanban-column');
        column.appendChild(card);

        // Determina o novo status com base no ID da coluna
        let status;
        if (column.id === 'to-do') {
            status = 'Nova';
        } else if (column.id === 'in-progress') {
            status = 'Em andamento';
        } else if (column.id === 'done') {
            status = 'Concluida';
        }

        // Envia uma requisição AJAX para atualizar o status
        fetch(`/update_status/${id.replace('card', '')}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Adiciona o CSRF token
            },
            body: JSON.stringify({status: status})
        }).then(response => {
            if (!response.ok) {
                throw new Error('Erro ao atualizar status.');
            }
            return response.json();
        }).then(data => {
            console.log('Status atualizado com sucesso:', data);
        }).catch(error => {
            console.error('Erro:', error);
        });
    }

    // Função para obter o CSRF token dos cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


//Script para abrir o pop-ups

    document.addEventListener('DOMContentLoaded', function() {
        const openPopups = document.querySelectorAll('.open-popup');
        openPopups.forEach(popup => {
            popup.addEventListener('click', function(e) {
                e.preventDefault();
                const url = popup.getAttribute('data-popup-url');
                openPopup(url);
            });
        });

        function openPopup(url) {
            const width = 800;
            const height = 600;
            const left = (window.innerWidth - width) / 2;
            const top = (window.innerHeight - height) / 2;
            window.open(url, 'popup', `width=${width},height=${height},left=${left},top=${top}`);
        }
    });



    // Script para ajustar o modal ao abrir
    $('#modalCriarTarefa').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Botão que acionou o modal
        // Se necessário, você pode pegar informações do botão para modificar o conteúdo do modal
    });
