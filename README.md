## 📦 Backend - Manager de uma loja de Celulares

API desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) para gerenciamento de usuários, autenticação, carrinhos, modificações e operações relacionadas a um sistema de controle de celulares.

---

### 🚀 Tecnologias utilizadas

* **Python 3.11+**
* **FastAPI**
* **PyMongo** (MongoDB)
* **Pydantic**
* **Uvicorn** (servidor ASGI)
* **CORS Middleware**

---

### 📁 Estrutura de Pastas

```
backend/
│
├── controllers/               # Funções de controle de negócio
│   ├── auth_controllers.py
│   ├── delete_controllers.py
│   ├── modify_controllers.py
│   ├── register_controllers.py
├── database/                  # Conexão com MongoDB
│   ├── connection.py
├── models/                    # Modelos Pydantic
│   ├── auth.py
│   ├── client.py
│   ├── email.py
│   ├── user.py
├── providers/                 # Funções auxiliares ou externas
│   ├── email_provider.py
│   ├── hash_provider.py
│   ├── token_provider.py
├── routers/                   # Rotas organizadas por responsabilidade
│   ├── __init__.py
│   ├── auth_utils.py
│   ├── router_auth.py
│   ├── router_deletes.py
│   ├── router_emails.py
│   ├── router_modifications.py
│   └── router_registers.py
│
├── services/                  # Lógica de serviço (ex: banco de dados)
│   ├── client_delete.py
│   ├── client_register.py
│   ├── user_delete.py
│   ├── user_email_get.py
│   ├── user_get_hash_ByEmail.py
│   ├── user_modify_status.py
│   ├── user_register.py
├── templates/                 # Templates de e-mail ou HTML (se houver)
│   ├── confirm_email.py
├── .gitignore 
├── README.md 
└──  server.py                  # Ponto de entrada da aplicação
```

---

### 🧩 Endpoints disponíveis

#### 🔐 Autenticação (`/auth`)

* `POST /auth/login` — Login de usuário
* `POST /auth/logout` — Logout (se implementado)

#### 👤 Registro (`/register`)

* `POST /register/client` — Cadastrar novo cliente
* `POST /register/admin` — Cadastrar novo administrador (exemplo)

#### ✉️ E-mails (`/email`)

* `POST /email/send-verification` — Enviar código ou link de verificação

#### 🗑️ Deleções (`/delete`)

* `DELETE /delete/client/{id}` — Deletar cliente por ID
* `DELETE /delete/admin/{id}` — Deletar administrador por ID

#### ✏️ Modificações (`/modify`)

* `PATCH /modify/client/{id}` — Atualizar dados do cliente
* `PUT /modify/status` — Atualizar status com base no e-mail (exemplo)
* `DELETE /modify/client/{id}` — Deletar cliente com verificação

> ⚠️ Consulte o Swagger para ver todos os endpoints disponíveis (`/docs`).

---

### ▶️ Como executar localmente

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo/backend
```

2. **Crie e ative um ambiente virtual**

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Configure o `.env`**
   Crie um arquivo `.env` com as configurações necessárias (exemplo de variáveis comuns):

```
MONGO_URL=mongodb://localhost:27017
JWT_SECRET=uma_senha_segura
TOKEN_EXPIRE_MINUTES=30
```

5. **Inicie o servidor**

```bash
uvicorn server:app --reload
```

6. **Acesse a documentação**

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### ✅ TODO

* [ ] Implementar testes unitários com `pytest`
* [ ] Adicionar autenticação OAuth2
* [ ] Melhorar tratamento de erros com `HTTPException`
* [ ] Dockerizar o projeto

---

### 👨‍💻 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

### 📝 Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo `LICENSE` para mais detalhes.

