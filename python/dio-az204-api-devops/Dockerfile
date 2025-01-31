# Utilize uma imagem oficial do Python como base
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências para o container
COPY requirements.txt ./

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação para o container
COPY . ./

# Expõe a porta utilizada pelo FastAPI
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "weather_api:app", "--host", "0.0.0.0", "--port", "8000"]
