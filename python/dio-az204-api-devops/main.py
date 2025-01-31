from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# Substitua "YOUR_API_KEY" pela sua chave da OpenWeatherMap
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/{city}")
async def get_weather(city: str):
    """
    Endpoint para obter informações sobre o clima de uma cidade.
    
    Args:
        city (str): Nome da cidade a ser pesquisada.

    Returns:
        dict: Informações sobre o clima da cidade.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Erro ao buscar dados do clima.")

    data = response.json()

    return {
        "cidade": data.get("name"),
        "temperatura": data["main"].get("temp"),
        "descricao": data["weather"][0].get("description"),
        "umidade": data["main"].get("humidity"),
        "vento": {
            "velocidade": data["wind"].get("speed"),
            "direcao": data["wind"].get("deg")
        }
    }

# Para rodar o servidor localmente, utilize o comando abaixo:
# uvicorn weather_api:app --reload
