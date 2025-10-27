document.addEventListener('DOMContentLoaded', function() {
    // Exemplo de validação de formulário
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(event) {
            let isValid = true;

            // Validação de campos obrigatórios
            form.querySelectorAll('[required]').forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('error');
                } else {
                    input.classList.remove('error');
                }
            });

            // Validação de e-mail
            const emailInput = form.querySelector('input[type="email"]');
            if (emailInput) {
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailPattern.test(emailInput.value)) {
                    isValid = false;
                    emailInput.classList.add('error');
                } else {
                    emailInput.classList.remove('error');
                }
            }

            // Impede o envio do formulário se houver erros
            if (!isValid) {
                event.preventDefault();
                alert('Por favor, corrija os erros no formulário.');
            }
        });
    });
});