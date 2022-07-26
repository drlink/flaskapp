import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=eb674176aa071860cd64f69cad582750"

resp = urllib.request.urlopen(url)

dados = resp.read()

jsondata = json.loads(dados)

print(jsondata['results'])