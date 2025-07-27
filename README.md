# Mini ML Platform

Este projeto simula uma plataforma simplificada de deploy de modelos de Machine Learning, composta por:

- Treinamento automatizado de um modelo
- Servimento via API REST documentada com Swagger
- Containerização com Docker e Docker Compose

A API está preparada para consumir modelos treinados localmente. Neste exemplo, é utilizado o dataset Iris e um classificador RandomForestClassifier.

## Estrutura do Projeto

mini-ml-platform/
├── train/              # Código para treinar o modelo
│   └── train.py
├── serve/              # API REST com FastAPI
│   ├── app.py
│   ├── init.py
│   └── model.pkl       # Modelo salvo após o treinamento
├── tests/              # Testes automatizados com pytest
│   └── test_api.py
├── Dockerfile          # Imagem Docker da aplicação
├── docker-compose.yml  # Orquestração dos containers
├── requirements.txt    # Lista de dependências
└── README.md           # Instruções e informações do projeto

## O que o código faz

1. `train/train.py`: treina um modelo RandomForest usando o dataset Iris e salva como serve/model.pkl.
2. `serve/app.py`: implementa uma API REST com FastAPI que carrega o modelo treinado e expõe o endpoint /predict.
3. `Dockerfile` e `docker-compose.yml`: permitem executar treinamento, API e testes automatizados em containers isolados.
4. O modelo é acessado dentro de um container Docker e exposto localmente via porta `8000`.


## Instruções para rodar localmente

### Clonar o repositório

```bash
git clone <url-do-repositorio>
cd mini-ml-platform
```

### Criar e ativar o ambiente virtual
## Versão utilizada do Python para esse código foi Python 3.12.10

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
.\venv\Scripts\activate    # Windows
```

### Instalar as dependências - versão utilizada do Python 3.12.10 para esse exercicio

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Treinar o modelo

Para treinar o modelo dentro de um container Docker e gerar o arquivo `serve/model.pkl`, execute:

```bash
docker-compose run --rm train
```
💡 Nota: Caso deseje adaptar a plataforma para outros modelos e dados, basta alterar o conteúdo do script train/train.py, treinando o modelo desejado e salvando como serve/model.pkl. A API irá carregá-lo automaticamente no momento da inicialização.

## Subir a API com Docker Compose

Após o treinamento, inicie os containers:

```bash
docker-compose up --build
```

## Acessar a documentação Swagger

Abra no navegador: http://localhost:8000/docs

## Como testar a API no Swagger

1. Clique no endpoint `POST /predict`
2. Clique no botão "Try it out"
3. Insira o seguinte corpo de requisição:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

4. Clique em "Execute"
5. A resposta será um número representando a classe prevista, nesse caso o response body será:

```json
{
  "prediction": 0
}
```

## Interpretação da predição

O modelo treinado com o dataset Iris retorna os seguintes códigos:

- 0: Setosa
- 1: Versicolor
- 2: Virginica

## Executar Testes

Com Docker

```bash
docker-compose run --rm test
```

## Dependências principais

Contidas no arquivo `requirements.txt`:

```
fastapi==0.111.0
uvicorn==0.29.0
scikit-learn==1.4.2
joblib==1.4.2
numpy==1.26.4
pytest==8.2.1
```

## Contato
Lázara Camila  
lazaracamila@gmail.com