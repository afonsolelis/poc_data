# POC Data

Este é um projeto educacional para demonstrar a integração de diferentes tecnologias para ingestão, processamento e visualização de dados. O projeto utiliza RabbitMQ, Logstash, ClickHouse e Grafana.

## Estrutura do Projeto

- `docker-compose.yml`: Arquivo de configuração do Docker Compose para orquestrar os serviços.
- `pipe.py`: Script Python para gerar e enviar mensagens para o RabbitMQ.
- `requirements.txt`: Arquivo de dependências do Python.
- `clickhouse/`: Diretório com a configuração do ClickHouse.
  - `config/default-users.xml`: Configuração de usuários do ClickHouse.
- `logstash/`: Diretório com a configuração do Logstash.
  - `config/logstash.yml`: Configuração principal do Logstash.
  - `pipeline/logstash.conf`: Configuração do pipeline do Logstash.

## Tecnologias Utilizadas

- **RabbitMQ**: Fila de mensagens para comunicação assíncrona.
- **Logstash**: Ferramenta de processamento de dados.
- **ClickHouse**: Banco de dados analítico.
- **Grafana**: Plataforma de visualização de dados.
- **Python**: Linguagem de programação utilizada para gerar e enviar mensagens.

## Configuração e Execução

### Pré-requisitos

- Docker e Docker Compose instalados.

### Passos para Executar

1. Clone o repositório:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd poc_data
    ```

2. Instale as dependências do Python:
    ```sh
    pip install -r requirements.txt
    ```

3. Inicie os serviços com Docker Compose:
    ```sh
    docker-compose up
    ```

4. Execute o script Python para gerar e enviar mensagens:
    ```sh
    python pipe.py
    ```

### Acessando os Serviços

- **RabbitMQ**: Acesse a interface de gerenciamento em `http://localhost:15672` (usuário: `guest`, senha: `guest`).
- **ClickHouse**: Acesse a interface HTTP em `http://localhost:8123`.
- **Grafana**: Acesse a interface web em `http://localhost:3000` (usuário: `admin`, senha: `admin`).

## Estrutura do Código

### `pipe.py`

Este script gera dados aleatórios utilizando a biblioteca Faker e envia para o RabbitMQ.

### `logstash/pipeline/logstash.conf`

Configuração do Logstash para ler mensagens do RabbitMQ, processar e enviar para o ClickHouse.

## Contribuição

Este é um projeto educacional, contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
