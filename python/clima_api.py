import requests

def get_coordinates(cidade):
    """
    Consulta o Nominatim (OpenStreetMap) para obter latitude e longitude de uma cidade
    """
    url = f"https://nominatim.openstreetmap.org/search?q={cidade}&format=json"
    try:
        resposta = requests.get(url, headers={"User-Agent": "FarmTechApp"})
        resposta.raise_for_status()
        dados = resposta.json()
        if not dados:
            print("⚠️ Cidade não encontrada. Use um nome válido.")
            return None, None
        lat = float(dados[0]["lat"])
        lon = float(dados[0]["lon"])
        return lat, lon
    except requests.RequestException as e:
        print("Erro ao buscar coordenadas:", e)
        return None, None

def obter_clima(cidade_entrada):
    """
    Recebe cidade como string, busca coordenadas e retorna clima atual
    """
    lat, lon = get_coordinates(cidade_entrada)
    if lat is None or lon is None:
        return

    # Consulta Open-Meteo
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if "current_weather" not in dados:
            print("⚠️ Dados do clima não disponíveis.")
            return

        clima = dados["current_weather"]
        temperatura = clima["temperature"]
        vento = clima["windspeed"]
        codigo_tempo = clima["weathercode"]

        # Mapear códigos do tempo para descrição
        tempo_map = {
            0: "Céu limpo",
            1: "Principalmente limpo",
            2: "Parcialmente nublado",
            3: "Nublado",
            45: "Neblina",
            48: "Neblina gelada",
            51: "Chuva fraca",
            53: "Chuva moderada",
            55: "Chuva forte",
            61: "Chuva leve",
            63: "Chuva moderada",
            65: "Chuva forte",
            71: "Neve leve",
            73: "Neve moderada",
            75: "Neve forte",
            80: "Chuva fraca com trovoadas",
            81: "Chuva moderada com trovoadas",
            82: "Chuva forte com trovoadas"
        }

        descricao_tempo = tempo_map.get(codigo_tempo, "Não disponível")

        print(f"\n📍 Local: {cidade_entrada} (lat {lat}, lon {lon})")
        print(f"🌡️ Temperatura atual: {temperatura} °C")
        print(f"💨 Velocidade do vento: {vento} km/h")
        print(f"🌤️ Condição: {descricao_tempo}\n")

    except requests.RequestException as e:
        print("Erro ao obter dados meteorológicos:", e)
