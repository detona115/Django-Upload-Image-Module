[![GitHub license](https://img.shields.io/badge/implemented%20by-Andy-blue)](https://www.linkedin.com/in/andy-kiaka-76a983110/)
# Django Module for image uploading

Módulo Django que permite ao usuário fazer o upload de imagens através de um formulário e consequentemente poder visualizá-las em uma galeria.

## Propósito 🚀

A idéia deste sistema consiste em ter um mini site desenvolvido com Django onde o usuário possa efetuar as operações de
upload de imagens e visualização em uma espécie de galeria. Na página inicial o usuário tem um formulário onde é necessário 
fornecer uma descrição ou nome da imagem a ser carregada e selecionar a imagem em sí, que logo em seguida já se encontra disponível
na galeria que pode ser acessada pelo link fotos. Todas as imagens possuem suas referências em uma base de dados postgres já 
pre configurado para este propósito junto com outros dados relevante ao processo que estão definidas na seção seguinte.

## Processo e Abordagem 🔩

- O primeiro passo exige que o usuário forneça uma descrição ou título do arquivo e selecionar o arquivo em si nos campos determinados.
- Uma vez confirmado o processo, o sistema extrai do arquivo os seguintes dados, formato, dimensao e cria uma miniatura (thumbnail), 
que é usado na galeria.
- Na galeria, o usuário podera visualizar todas as fotos carregadas no sistema, a galeria oferece dois modos de visualização (Grid e Lista)
- Ao clicar sobre cada foto da galeria, é mostrado uma popup com os detalhes referente ao arquivo clicado e dois links (editar e baixar)
- Além das funcionalidades mencionadas acima, o módulo conta com as funcionalidades de buscas e filtragens dos dados, especificamente neste 
módulo, optei em usar as duas funcionalidades ao mesmo tempo, onde a filtragem é feita pelo formato do arquivo ou sua descrição desta forma 
quando o usuário efetua uma busca no campo de busca, os primeiros resultados são baseados nas opções de filtragens mencionadas acima e por último 
uma busca livre.

### Pré-requisitos 📖

Para o bom funcionamento deste sistema, as bibliotecas a seguir são necessárias, no entanto nenhuma instalação manual será requerida, pois 
por questões de práticidades tudo é feito através do docker.

- Python 3.7 ou superior
- Django 3.0.8
- django-crispy-forms
- Pillow
- psycopg2-binary
- sorl-thumbnail

### Instalação e Execução 🔧

#### Após baixar , descompactar e acessar a pasta com os arquivos

N.B: Esta versão foi testada somente com ubuntu e a instalação leva uns 3 min devido ao tamanho das imagens e dos containers

- Em um terminal, execute o seguinte comando para construir as imagem e os containers   
- Antes da execução é necessário ter as portas 5432, 8000, 8088 e 8080 desocupadas no host para que postgres e adminer possam funcionar

```
docker-compose up -d
```      
e depois, os dois comandos seguintes para inicializar a base de dado.
```
docker-compose exec web python manage.py makemigrations uploads
```
```
docker-compose exec web python manage.py migrate
```

## Dados gerados 📦

* Para tornar mais comoda a visualização das operações feitas no sistema, o serviço adminer é instalado junto ao sistema, o que
permite acessar postgres pelo navegador web.
* Para acessar e usar o módulo basta digitar na barra de endereço do seu navegador favorito 'http://localhost:8000/'
* Para logar no adminer, uma vez todos os serviços estiverem funcionando, abre seu navegador preferido e digite na barra de
endereço 'localhost:8088' , uma vez feito estará na página de login do adminer. Adminer consegue se conectar a diferentes tipos
de SGBD, portanto na opção sistema, escolha 'PostgreSQL'. No campo servidor, digite 'mydb'. No campo usuario, digite 'user'.
No campo senha, digite 'password' e no campo Base de dados 'uploaddb'.

## Autor ✒️

* **Andy Kiaka** - *Job Completo* - [detona115](https://github.com/detona115)

---
⌨️ com ❤️ por [detona115](https://github.com/detona115) 😊
