import boto3
import json

def lambda_handler(event, context):
    ses = boto3.client('ses', region_name='sa-east-1')
    
    email_from = 'enderecoDeEmailVerificado@ses.com'  # Seu endereço de e-mail verificado no SES
    email_to = event['email_to']  # Endereço de e-mail do destinatário
    subject = event['subject']  # Titulo do e-mail
    body_text = event['body_text']  # Conteúdo do e-mail
    
    try:
        response = ses.send_email(
            Source=email_from,
            Destination={
                'ToAddresses': [email_to]
            },
            Message={
                'Subject': {
                    'Data': subject
                },
                'Body': {
                    'Text': {
                        'Data': body_text
                    }
                }
            }
        )
        print(response)
        return {
            'statusCode': 200,
            'body': json.dumps('Email enviado com sucesso!')
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Falha ao enviar e-mail')
        }

