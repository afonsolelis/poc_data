import json
import time
import os
import pika
from faker import Faker

fake = Faker()

def generate_message():
    """
    Gera um JSON com dados aleatórios utilizando o Faker.
    """
    data = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "job": fake.job(),
        "created_at": fake.iso8601()
    }
    return json.dumps(data)

def main():
    # Obtém o hostname do RabbitMQ via variável de ambiente; padrão: 'rabbitmq'
    rabbitmq_host = os.environ.get("RABBITMQ_HOST", "rabbitmq")
    
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbitmq_host)
        )
    except Exception as e:
        print(f"Erro ao conectar no RabbitMQ em {rabbitmq_host}: {e}")
        return

    channel = connection.channel()

    # Declara a fila 'myqueue'; se não existir, ela será criada com persistência
    queue_name = 'myqueue'
    channel.queue_declare(queue=queue_name, durable=True)

    try:
        while True:
            message = generate_message()
            channel.basic_publish(
                exchange='',
                routing_key=queue_name,
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2  # Mensagem persistente
                )
            )
            print(f" [x] Enviado: {message}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Encerrando produtor...")
    finally:
        connection.close()

if __name__ == '__main__':
    main()
