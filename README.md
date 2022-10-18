# Leitor-CNAB

## Inicializando banco de dados
  Essa aplicação usa banco de dados sqlite3, para inicializá-lo:

  1. Abra o terminal na pasta raiz do repositório;
  2. Configure seu ambiente virtual da forma como preferir (opcional); 
  3. Use o comando `python manage.py migrate` para gerar o banco de dados com as tabelas necessárias para a aplicação;
  4. Você pode rodar a aplicação com o comando `python manage.py runserver` e pará-la com as teclas `CTRL + C` no windows e linux, ou `CMD + C` no mac

## Populando a tabela de tipos de transação
  Para utilizar os tipos de transação pré-definidos, use o comando `python manage.py loaddata types-fixture.json`

## Criando um usuário
  Esta aplicação usa o django admin para registrar e listar dados. Para ter acesso ao django admin primeiro você precisa criar uma conta de superuser:

  1. Abra o terminal na pasta raiz do repositório;
  2. Use o comando `python manage.py createsuperuser` e crie um usuário com as informações pedidas;
  3. Acesse o endereço [http://localhost:8000/admin] para abrir o django admin;
  4. Use o login e senha criados para ter acesso

## Criando e listando transações
  - Na barra esquerda da página do admin, clique em Transactions para mostrar a lista de todas as transações cadastradas.
  - Você pode cadastrar transações uma a uma manualmente ou carregar um arquivo CNAB
  - Para carregar um arquivo CNAB, clique no link "Import CNAB" no topo da lista.
  - O link levará a uma nova tela aonde você poderá fazer upload de um arquivo CNAB (o arquivo provido para teste se encontra na pasta data/CNAB.txt)