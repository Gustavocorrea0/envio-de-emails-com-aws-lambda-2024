# Envio de Emails com AWS Lambda e Python

## Ferramentas
Python 3.12: [Download Python](https://www.python.org/downloads/) &nbsp;&middot;&nbsp; <br>
AWS: [AWS Amazon Web Services](https://aws.amazon.com/pt/) &nbsp;&middot;&nbsp;

# Documentação e Forma de Criação

## AWS
Crie uma Conta AWS: [AWS Amazon Web Services](https://aws.amazon.com/pt/) &nbsp;&middot;&nbsp;
<br><br>
<img width="500px" src="./imgs/conta_aws.png"> <br><br>

## AWS Lambda
<a>1 - Selecione a melhor região desejada </a><br><br>
<img width="500px" src="./imgs/console_aws_1.png"> <br><br>
<a>2 - Selecione o serviço AWS Lambda</a><br><br>
<img width="500px" src="./imgs/console_aws_2.png"> <br><br>
<a>3 - Selecione "Painel" e clique em "Criar Função"</a><br><br>
<img width="500px" src="./imgs/console_aws_3.png"> <br><br>
<a>4 - Configure a função - Adicione Nome</a><br>
<a>5 - Configure a função - Adicione Linguagem(neste caso Python 3.12)</a><br>
<a>6 - Crie a função</a><br><br>
<img width="500px" src="./imgs/console_aws_4.png"> <br><br>
<a>7 - Crie a função</a><br><br>

## Criar Codigo
<a>1 - Adicione o codigo de "funcao_lambda_v3.py" ao arquivo "lambda_function.py" na função</a><br>
<a>2 - Clique em "Deploy"</a><br><br>
<img width="500px" src="./imgs/console_aws_5.png"> <br><br>

## Criar Teste 
<a>1 - Navegue até o campo "Testar"</a><br>
<a>2 - Adicione o nome para evento</a><br>
<a>3 - Adicione o codigo JSON de "jsonTeste.json" em "JSON do evento"</a><br>
<a>4 - Preencha os campos de "JSON do evento" com os dados necessarios</a><br>
<a>5 - Dados: Email do Destinatario, Titulo e Assunto</a><br>
<a>6 - Clique em salvar</a><br><br>
<img width="500px" src="./imgs/console_aws_6.png"> <br><br>

## Configuração de SES(Amazon Simple Email Service)
<a>1 - Volte para o "Console AWS" e Busque por "SES"</a><br>
<a>2 - Clique em "Amazon Simple Email Service"</a><br><br>
<img width="500px" src="./imgs/configuracao_ses_1.png"> <br><br>
<a>3 - Clique em "Começar"</a><br><br>
<img width="500px" src="./imgs/configuracao_ses_2.png"> <br><br>
<a>4 - Vá até "Identidades" na barra lateral esquerda</a><br>
<a>5 - Clique em "Criar identidade"</a><br><br>
<img width="500px" src="./imgs/configuracao_ses_3.png"><br><br>
<a>6 - Selecione a opção "Endereço de e-mail"</a><br>
<a>7 - Adicione o email do destinatario</a><br><br>
<img width="500px" src="./imgs/configuracao_ses_4.png"><br><br>
<a>8 - Clique em "Criar identidade"</a><br>
<a>9 - A AWS irá enviar um email para destinatario solicitando a confirmação do Email</a><br>
<a>10 - Basta clicar no Link para validar</a><br><br>
<img width="500px" src="./imgs/configuracao_ses_5.png"><br><br>
<a>11 - Após isso volte ao Amazon SES e o email estará verificado</a><br><br>
<img width="500px" src="./imgs/configuracao_ses_6.png"><br><br>
<a>12 - É necessario adicionar no minimo 2 Emails(Origem e Destino)</a><br>

## Configuração de IAM para permissão de envio
<a>1 - Volte para o "Console AWS" e Busque por "IAM"</a><br>
<a>2 - Clique em "IAM"</a><br><br>
<img width="500px" src="./imgs/configuracao_iam_1.png"><br><br>
<a>3 - Clique em "Funções" barra lateral esquerda</a><br>
<a>4 - Clique na função</a><br><br>
<img width="500px" src="./imgs/configuracao_iam_2.png"><br><br>
<a>5 - Em adicionar "Adicionar permissões" selecione "Anexar Políticas"</a><br><br>
<img width="500px" src="./imgs/configuracao_iam_3.png"><br><br>
<a>6 - Busque por "AmazonSESFullAccess"</a><br>
<a>7 - Selecione e clique em adicionar Permissão</a><br><br>
<img width="500px" src="./imgs/configuracao_iam_4.png"><br><br>
<a>8 - Após isso volte para "Console AWS"</a><br>

## Execução de Envio
<a>1 - Volte para o "Console AWS" e Busque por "Lambda" e a acesse</a><br>
<a>2 - Acesse a função</a><br>
<a>3 - No código adicione o email de origem na variavél "email_from"</a><br><br>
<img width="500px" src="./imgs/configuracao_envio_de_email_1.png"><br><br>
<a>4 - Clique em "Deploy" e vá para a aba de "Testar"</a><br>
<a>5 - Adicione o email do destinatario no campo "email_to" no campo "JSON do evento"</a><br>
<a>6 - Clique em "Testar"</a><br><br>
<img width="500px" src="./imgs/configuracao_envio_de_email_2.png"><br><br>
<a>7 - A seguinte LOG será lançada</a><br><br>
<img width="500px" src="./imgs/log_status_200.png"><br><br>
<a>8 - E o email será enviado</a><br><br>
<img width="500px" src="./imgs/email_recebido.png"><br><br>
<img width="500px" src="./imgs/email_recebido_1.png"><br><br>
<a>9 - Finalizando o processo</a><br><br>

## Possivéis erros e soluções
<a>1 - Tempo de Execução</a><br>
<a>2 - Erro de validação de SES</a><br>
<a>3 - Erro de validação de IAM</a><br>
<a>4 - Erro de digitação de código</a><br>
<a>5 - Email não adicionado</a><br>
<a>6 - Email Inválido</a><br>

## Possivéis erros e soluções
<a>1 - Alterar tempo nas configurações da Lambda</a><br>
<a>2 - Verificar e Alterar informações de SES</a><br>
<a>3 - Verificar e Alterar informações de IAM</a><br>
<a>4 - Revisar código</a><br>
<a>5 - Adicionar email ao SES</a><br>
<a>6 - Adicionar email valido ao SES</a><br>
