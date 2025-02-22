import requests
from bs4 import BeautifulSoup

# URL do site que queremos raspar
url = "https://example.com"

# Faz a requisição HTTP
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Encontra todos os títulos <h1>, <h2> e <h3>
    for tag in soup.find_all(["h1", "h2", "h3"]):
        print(tag.text.strip())  # Exibe o texto do título
else:
    print("Erro ao acessar a página")
