# Flavio Macedo - Blog Pessoal

Blog pessoal desenvolvido com **Django 5 + Tailwind CSS v4**, focado em **Linux, Tecnologia, Economia e Política**.

Projeto construído com o objetivo de compartilhar conhecimento técnico, tutoriais práticos, análises econômicas e reflexões sobre política, além de servir como portfólio de projetos.

---

## ✨ Funcionalidades

- Design moderno com **dark/light mode** (toggle com ícones Sol/Lua)
- Editor rico com **CKEditor 5**
- Sistema completo de categorias e tags
- Seção dedicada a **Tutoriais**
- Página de **Portfólio** com links para repositórios GitHub
- Totalmente responsivo e otimizado para mobile
- Integração com Tailwind CSS v4
- Suporte a imagens destacadas nos posts
- Contador de visualizações
- Estrutura limpa e escalável

---

## 🛠 Tecnologias Utilizadas

- **Backend**: Python + Django 5.1
- **Frontend**: Tailwind CSS v4 + Alpine.js
- **Editor**: CKEditor 5
- **Banco de dados**: PostgreSQL (produção) / SQLite (desenvolvimento)
- **Estilo**: Tailwind CSS com suporte nativo a dark mode
- **Deploy**: Pronto para Railway, Render ou VPS Linux

---

## 📁 Estrutura do Projeto

```text
blog_pessoal/
├── core/                  # Configurações principais
├── blog/                  # App principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
├── theme/                 # Configuração do django-tailwind
│   └── static_src/
│       └── src/input.css
├── static/
├── media/                 # Imagens dos posts
├── templates/
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/Flaviohmm/blog-pessoal.git
cd blog-pessoal
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
# venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco e migrações
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Compile o Tailwind CSS
```bash

# Usando o binário standalone (recomendado)
./tailwindcss -i ./theme/static_src/src/input.css -o ./theme/static/css/output.css --watch

# Usando o node
npx @tailwindcss/cli -i ./theme/static_src/src/input.css -o ./theme/static/css/output.css --watch
```

### 6. Rode o servidor
```bash
python manage.py runserver
python manage.py tailwind dev
```

Acesse em: http://127.0.0.1:8000

### 📬 Contato
**Flavio Macedo**
Natal, Rio Grande do Norte - Brasil

- GitHub: @[Flaviohmm](https://github.com/Flaviohmm)
- LinkedIn: https://www.linkedin.com/in/flavio-henrique-m2/
- E-mail: fhenrique609@gmail.com

### ⭐ Se gostou do projeto
Sinta-se à vontade para dar uma estrela ⭐ no repositório!

Contribuições, sugestões e feedbacks são sempre bem-vindos.