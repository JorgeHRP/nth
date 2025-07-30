from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from selenium import webdriver
from selenium_stealth import stealth
import time
import random

app = FastAPI()

class WebhookData(BaseModel):
    mensagem: str

def generate_random_number():
    return random.randint(12, 20)

def visualizar_url(mensagem: str, visualizacao: int):
    for _ in range(visualizacao):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

        stealth(driver,
                languages=["pt-BR", "pt"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        driver.get(mensagem)
        time.sleep(150)
        driver.quit()

@app.post("/webhook")
async def webhook(data: WebhookData, background_tasks: BackgroundTasks):
    visualizacao = generate_random_number()
    background_tasks.add_task(visualizar_url, data.mensagem, visualizacao)
    return {"status": "recebido"}
