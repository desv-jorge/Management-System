# 📦 Backend - Management System (Loja de Celulares)

API desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) para gerenciamento de usuários, autenticação, envio de e-mails e operações administrativas relacionadas a uma loja de celulares.

---

## 🚀 Tecnologias utilizadas

* **🐍 Python 3.11+**
* **⚡ FastAPI** — Web framework moderno e performático
* **🍃 MongoDB** — Banco de dados NoSQL (via MongoEngine)
* **🔐 JWT** — Autenticação com JSON Web Tokens
* **📦 Pydantic** — Validação e tipagem de dados
* **🔄 CORS Middleware**
* **🔧 Uvicorn** — Servidor ASGI leve e rápido

---

## 📁 Estrutura de Pastas

```
backend/
│
├── controllers/               # Funções de controle de negócio
├── database/                  # Conexão com MongoDB
├── models/                    # Schemas e validações (Pydantic)
├── providers/                 # Serviços auxiliares (e-mail, hash, JWT)
├── routers/                   # Rotas organizadas por responsabilidade
├── schemas/                   # Modelos de banco de dados com o mongoEngine
├── services/                  # Regras de negócio
├── templates/                 # Templates HTML para e-mails
├── .env                       # Variáveis de ambiente
├── .gitignore
├── README.md
└── server.py                  # Ponto de entrada da aplicação
```

---

## 🧩 Endpoints disponíveis

### 🔐 Autenticação (`/auth`)

* `POST /auth/token` — Login de usuário
* `GET /auth/me` — Dados do usuário autenticado

### 👤 Registro (`/register`)

* `POST /register/user` — Cadastrar novo usuário
* `POST /register/client` — Cadastrar novo cliente

### ✉️ E-mails (`/email`)

* `POST /email/confirm` — Confirmação de e-mail

### 🗑️ Deleções (`/delete`)

* `DELETE /delete/user` — Deletar usuário autenticado
* `DELETE /delete/client/{id}` — Deletar cliente por ID

### ✏️ Modificações (`/modify`)

* `PATCH /modify/status/{email}` — Ativar conta via e-mail

> ⚠️ Acesse `/docs` para visualizar todos os endpoints com exemplos interativos.

---

## ▶️ Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/desv-jorge/Management-System.git
cd Management-System/backend
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Crie o arquivo `.env`

```env
MONGO_URI = "string de conexão"

SECRET_KEY = "hash gerado por um bash"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 14400
```

> 🔒 **Importante:** Certifique-se de que o arquivo `.env` está listado no `.gitignore` para evitar o versionamento de dados sensíveis.

### 5. Inicie o servidor

```bash
uvicorn server:app --reload
```

### 6. Acesse a documentação interativa

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✅ TODO

* [ ] Implementar testes automatizados com `pytest`
* [ ] Adicionar autenticação OAuth2 (Google, GitHub etc.)
* [ ] Dockerizar o projeto
* [ ] Criar sistema de logs
* [ ] Melhorar tratamento de erros com `HTTPException`
* [ ] Adicionar sistema de permissões (roles de admin e cliente)

---

## 👨‍💻 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou pull request.

---

## 📝 Licença

Este projeto está licenciado sob a **MIT License**.

