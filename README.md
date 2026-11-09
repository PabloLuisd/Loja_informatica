# ByteStore – Sistema de Controle de Estoque

Sistema web desenvolvido em **Python e Django** para gerenciamento de estoque de uma loja de informática. O projeto permite cadastrar produtos, categorias e fornecedores, controlar entradas e saídas de mercadorias e acompanhar o histórico de movimentações.

## 2. Funcionalidades

### Gestão de cadastros
- Cadastro, consulta, edição e exclusão de categorias.
- Cadastro, consulta, edição e exclusão de fornecedores.
- Cadastro, consulta, edição e exclusão de produtos.

### Controle de estoque
- Registro de entradas de produtos.
- Registro de saídas de produtos.
- Atualização automática da quantidade em estoque.
- Bloqueio de saídas superiores à quantidade disponível.
- Identificação de produtos com estoque baixo.

### Movimentações
- Consulta do histórico de movimentações.
- Registro automático da data da movimentação.
- Identificação do tipo de movimentação (entrada ou saída).
- Registro da quantidade e de observações.

### Painel inicial
- Resumo da quantidade de produtos cadastrados.
- Total de categorias e fornecedores.
- Quantidade de movimentações registradas.
- Visualização de produtos com estoque baixo.

## 3. Tecnologias Utilizadas

- **Python:** linguagem de programação principal.
- **Django:** framework utilizado no desenvolvimento do sistema.
- **SQLite:** banco de dados.
- **HTML5:** estrutura das páginas.
- **CSS3:** estilização e organização visual.

## 4. Estrutura do Projeto

O projeto foi organizado em arquivos separados para facilitar a manutenção e a compreensão do código.

```text
loja_info/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── estoque/
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── categoria.py
│   │   ├── fornecedor.py
│   │   ├── produto.py
│   │   └── movimentacao_estoque.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   ├── home_views.py
│   │   ├── categoria_views.py
│   │   ├── fornecedor_views.py
│   │   ├── produto_views.py
│   │   └── movimentacao_views.py
│   │
│   ├── urls_configs/
│   │   ├── __init__.py
│   │   ├── categoria_urls.py
│   │   ├── fornecedor_urls.py
│   │   ├── produto_urls.py
│   │   └── movimentacao_urls.py
│   │
│   ├── templates/
│   │   └── estoque/
│   │
│   ├── static/
│   │   └── estoque/
│   │       └── style.css
│   │
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   └── apps.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## 5. Modelagem do Sistema

O sistema possui quatro entidades principais:

| Modelo | Descrição |
|---|---|
| Categoria | Armazena as categorias dos produtos. |
| Fornecedor | Armazena os dados dos fornecedores. |
| Produto | Armazena as informações dos produtos e seu saldo atual. |
| MovimentacaoEstoque | Registra as entradas e saídas de produtos. |

### Relacionamentos

- Uma categoria pode possuir vários produtos.
- Um fornecedor pode fornecer vários produtos.
- Um produto pode possuir várias movimentações de estoque.
- Cada movimentação está vinculada a um único produto.

## 6. Regras de Negócio

O sistema segue algumas regras para garantir a consistência das informações:

1. Todo produto deve estar associado a uma categoria e a um fornecedor.
2. Uma entrada aumenta a quantidade disponível em estoque.
3. Uma saída diminui a quantidade disponível em estoque.
4. Não é permitido registrar uma saída superior ao saldo disponível.
5. Toda movimentação registra automaticamente sua data.
6. Produtos com cinco unidades ou menos são identificados como estoque baixo.
7. O saldo do produto é atualizado automaticamente após cada movimentação.

## 7. Instalação e Configuração

### Pré-requisitos

- Python instalado.
- Visual Studio Code ou outro editor de código.
- Terminal ou prompt de comando.

### Passo 1 – Clonar ou baixar o projeto

```bash
python -m venv venv
```

### Passo 3 – Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### Passo 4 – Instalar as dependências

```bash
pip install django
```

### Passo 5 – Criar as migrações

```bash
python manage.py makemigrations
```

### Passo 6 – Aplicar as migrações

```bash
python manage.py migrate
```

### Passo 7 – Iniciar o servidor

```bash
python manage.py runserver
```

Após iniciar o servidor, acesse:

http://127.0.0.1:8000/

## 8. Acesso ao Django Admin

Para acessar o painel administrativo do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

Depois, acesse:

http://127.0.0.1:8000/admin/

Utilize as credenciais cadastradas durante a criação do superusuário.

## 9. Considerações Finais

O ByteStore foi desenvolvido com o propósito de aplicar conhecimentos de desenvolvimento web utilizando Python e Django, trabalhando conceitos como modelagem de dados, operações CRUD, relacionamentos entre entidades, organização de código e regras de negócio.

O projeto também demonstra a utilização de um sistema de controle de estoque, automatizando processos que auxiliam na organização e no gerenciamento de uma loja de informática.

---

**ByteStore – Sistema de Controle de Estoque**
*Desenvolvido como projeto acadêmico.*