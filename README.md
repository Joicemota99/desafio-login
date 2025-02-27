Projeto Django + Vue.js

Este projeto consiste em uma API desenvolvida com Django e um frontend utilizando Vue.js.

Requisitos

Antes de iniciar, certifique-se de ter instalado:

Python 3.x

Node.js

pip

Virtualenv

Como Rodar o Backend (Django)

Clone o repositório:

git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>

Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

Instale as dependências:

pip install -r requirements.txt

Realize as migrações do banco de dados:

python manage.py migrate

Execute o servidor Django:

python manage.py runserver

O backend estará rodando em http://127.0.0.1:8000/

Como Rodar o Frontend (Vue.js)

Acesse a pasta do frontend:

cd frontend

Instale as dependências:

npm install

Inicie o servidor de desenvolvimento:

npm run dev

O frontend estará rodando em http://localhost:5173/ (ou outra porta informada pelo terminal).

Configuração de Variáveis de Ambiente

Crie um arquivo .env na raiz do backend e adicione:

SECRET_KEY=suachavesecreta
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3  # Ou configure seu banco de dados

No frontend, crie um arquivo .env na pasta frontend e adicione:

VITE_API_BASE_URL=http://127.0.0.1:8000/

Endpoints da API

A API conta com os seguintes endpoints principais:

POST /api/auth/register/ - Registrar usuário

POST /api/auth/login/ - Autenticar usuário

GET /api/auth/user/ - Obter dados do usuário logado

Licença

Este projeto é de uso livre, sujeito aos termos especificados no repositório.
