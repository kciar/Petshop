# 🐾 Pet Shop "Amigo Fiel" — Sistema de Gestão

Aplicação completa para controle de **produtos, clientes e vendas** de um pet shop.  
Feita com **Flask**, **SQLite** e **HTML/CSS**, substitui planilhas manuais, automatizando cálculos e controle de estoque em tempo real.

---

## 🚀 Funcionalidades Principais

✅ Login de Usuário (autenticação com senha)  
✅ Dashboard com acesso rápido às áreas do sistema  
✅ CRUD de Produtos (com alerta visual de baixo estoque ⚠️)  
✅ CRUD de Clientes (com validação de e-mail)  
✅ Gestão de Vendas com atualização automática de estoque  
✅ Cálculo automático de totais e bloqueio de vendas sem estoque  

---

## ⚙️ Como Rodar o Projeto (Guia Rápido)

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seuusuario/petshop-amigo-fiel.git
cd petshop-amigo-fiel/meu_app


Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate    # (Windows)
# ou
source venv/bin/activate # (Linux/Mac)

Instale as dependências
pip install -r requirements.txt

Inicialize o banco de dados
python
>>> from app import db
>>> db.create_all()
>>> exit()

Rode a aplicação
python app.py
Acesse em: 👉 http://127.0.0.1:5000

Estrutura do projeto
meu_app/
│
├── app.py               # Backend Flask
├── models.py            # Modelos ORM (SQLite)
├── templates/           # Páginas HTML
│   ├── login.html
│   ├── dashboard.html
│   ├── produtos.html
│   ├── clientes.html
│   └── vendas.html
├── static/              # CSS, JS e imagens
│   ├── style.css
│   └── logo_petshop.png
└── database.db          # Banco de dados local


📸 Visual do Sistema
Tela de Login

Dashboard

Gestão de Vendas

🔗 Links Úteis

Documentação Flask: https://flask.palletsprojects.com

GitHub do Projeto: https://github.com/seuusuario/petshop-amigo-fiel

Visual: 

🧑‍💻 Autor
<img width="1919" height="884" alt="Captura de tela 2025-11-03 104516" src="https://github.com/user-attachments/assets/6fa0668a-2f7e-4f68-9820-805d61e5cbbf" />
<img width="1919" height="873" alt="Captura de tela 2025-11-03 105222" src="https://github.com/user-attachments/assets/bf5fc1de-44bd-4440-8d91-8c9ef255535e" />
<img width="1874" height="913" alt="Captura de tela 2025-11-03 105204" src="https://github.com/user-attachments/assets/80d92e8d-ae6b-4acc-ba74-da003a351db8" />

Raíck Miranda
Projeto desenvolvido para o Pet Shop “Amigo Fiel”, com foco em automação e gestão de estoque eficiente.

📅 Versão: 1.0
📍 Licença: MIT
