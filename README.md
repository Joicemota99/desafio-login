# Projeto Django + Vue.js

Este projeto consiste em uma API desenvolvida com Django e um frontend utilizando Vue.js.

## Requisitos

Antes de iniciar, certifique-se de ter instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Como Rodar o Backend (Django)

1. Clone o repositório:
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```

5. Execute o servidor Django:
   ```sh
   python manage.py runserver
   ```

O backend estará rodando em `http://127.0.0.1:8000/`

## Como Rodar o Frontend (Vue.js)

1. Acesse a pasta do frontend:
   ```sh
   cd frontend
   ```

2. Instale as dependências:
   ```sh
   npm install
   ```

3. Inicie o servidor de desenvolvimento:
   ```sh
   npm run dev
   ```

O frontend estará rodando em `http://localhost:5173/` (ou outra porta informada pelo terminal).

## Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do backend e adicione:
```env
SECRET_KEY=suachavesecreta
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3  # Ou configure seu banco de dados
```

No frontend, crie um arquivo `.env` na pasta `frontend` e adicione:
```env
VITE_API_BASE_URL=http://127.0.0.1:8000/
```

## Endpoints da API

A API conta com os seguintes endpoints principais:

- `POST /api/auth/register/` - Registrar usuário
- `POST /api/auth/login/` - Autenticar usuário
- `GET /api/auth/user/` - Obter dados do usuário logado

## Como Enviar para o GitHub

1. Inicialize um repositório Git (se ainda não estiver iniciado):
   ```sh
   git init
   ```

2. Adicione os arquivos ao repositório:
   ```sh
   git add .
   ```

3. Faça um commit inicial:
   ```sh
   git commit -m "Primeiro commit"
   ```

4. Adicione o repositório remoto:
   ```sh
   git remote add origin <URL_DO_SEU_REPOSITORIO>
   ```

5. Envie os arquivos para o GitHub:
   ```sh
   git push -u origin main
   ```

## Licença

Este projeto é de uso livre, sujeito aos termos especificados no repositório.

---


