FROM python:3.10-slim

# Instala dependências do sistema + Chrome + ChromeDriver
RUN apt update && apt install -y \
    wget unzip curl gnupg \
    chromium chromium-driver \
    && apt clean

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Comando para iniciar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
