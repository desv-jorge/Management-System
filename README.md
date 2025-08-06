
# 📱 Management System

Sistema de gerenciamento para uma loja de celulares, acessórios e serviços de assistência técnica. A solução visa facilitar o controle de clientes, serviços prestados e usuários da loja, oferecendo uma API estruturada e segura para administradores e funcionários.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **FastAPI**
- **MongoEngine / PyMongo**
- **Uvicorn**
- **JWT Authentication**
- **dotenv** para gerenciamento de variáveis sensíveis

---

## 🧱 Estrutura do Projeto

```
backend/
├── controllers/               # Funções de controle de negócio
├── database/                  # Conexão com MongoDB
├── models/                    # Schemas e validações (Pydantic)
├── providers/                 # Serviços auxiliares (e-mail, hash, JWT)
├── routers/                   # Rotas organizadas por responsabilidade
├── schemas/                   # Modelos de banco com MongoEngine
├── services/                  # Regras de negócio
├── templates/                 # Templates HTML para envio de e-mails
├── .env                       # Variáveis de ambiente
├── requirements.txt           # Dependências do projeto
├── server.py                  # Ponto de entrada da aplicação
└── README.md
```

---

## ⚙️ Configuração e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/desv-jorge/Management-System.git
cd Management-System/backend
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
MONGO_URI = "sua_string_de_conexao_mongodb"

SECRET_KEY = "chave_gerada_pelo_bash"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 14400
```

> 🔐 **Importante:** Mantenha seu `.env` fora do versionamento (`.gitignore` já cobre isso).

### 5. Inicie o servidor

```bash
uvicorn server:app --reload
```

### 6. Acesse a documentação interativa

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 Endpoints disponíveis

> 🔒 Todos os endpoints protegidos requerem autenticação JWT

### 🔐 Autenticação
- `POST /auth/token` – Login
- `GET /auth/me` – Obter dados do usuário autenticado

### 👤 Usuário
- `POST /register/user` – Criar novo usuário
- `DELETE /delete/user` – Deletar usuário autenticado
- `PATCH /modify/status/{email}` – Ativar conta
- `POST /email/confirm` – Enviar confirmação de conta por email

### 👥 Clientes
- `POST /register/client` – Registrar cliente
- `GET /get/clients` – Listar clientes
- `DELETE /delete/client/{id}` – Deletar cliente

### 🛠️ Serviços
- `POST /register/services` – Registrar serviço
- `GET /get/services` – Listar serviços
- `DELETE /delete/service/{id}` – Deletar serviço

---

## 🧪 Exemplo de uso

```bash
curl -X POST http://localhost:8000/auth/token   -H "Content-Type: application/x-www-form-urlencoded"   -d "username=usuario@email.com&password=suasenha"
```

---

## 🤝 Contribuindo

Este projeto segue o padrão de commits atômicos:

```bash
type(scope): descrição clara da mudança
```

Exemplos:
- `feat(auth): add JWT token validation middleware`
- `fix(client): handle missing email on client registration`
- `refactor(routers): centralize router registration in __init__.py`

---

## 📜 Licença

Projeto pessoal desenvolvido para uso em uma loja real. Sem licença pública até o momento.

---

## ✉️ Contato

Caso tenha dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou entrar em contato via [LinkedIn](www.linkedin.com/in/jorge-nathanael) ou [email](nathanael.jorge@aluno.uepb.edu.br).