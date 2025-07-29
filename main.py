from fastapi import FastAPI
from pydantic import BaseModel
from selenium import webdriver
from selenium_stealth import stealth
import time
import random

def generate_random_number():
    return random.randint(12, 20)

visualizacao = generate_random_number()

app = FastAPI()

# Modelo esperado no JSON
class WebhookData(BaseModel):
    mensagem: str

@app.post("/webhook")
async def webhook(data: WebhookData):    
    
    for i in range(visualizacao):
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

        driver.get(data.mensagem)   

        time.sleep(150)
        driver.quit()
    
    return {"status": 'ok'}
