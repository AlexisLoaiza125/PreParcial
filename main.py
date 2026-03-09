from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Pokemon(BaseModel):
    id:int
    name:str
    attack:int    
    life:int
    type:str

    # Metodo de ataque
    def attack_enemy(self, enemy):
        enemy.life -= self.attack
        return f"{self.name} atacó a {enemy.name} causando {self.attack} de daño"
    
     # Metodo para salir de la pokeball
    def leavepokeball(self):
        return f"{self.name} salió de la pokeball! y tiene {self.attack} de daño con {self.life} de vida"
    

pokemons_db = [
    Pokemon(id=1, name="Pikachu", attack=10, life=35, type="Eléctrico"),
    Pokemon(id=2, name="Bulbasaur", attack=8, life=40, type="Planta"),
    Pokemon(id=3, name="Charmander", attack=12, life=30, type="Fuego"),
    Pokemon(id=4, name="Squirtle", attack=9, life=38, type="Agua"),
    Pokemon(id=5, name="Caterpie", attack=4, life=20, type="Bicho"),
    Pokemon(id=6, name="Weedle", attack=5, life=22, type="Bicho"),
    Pokemon(id=7, name="Pidgey", attack=6, life=28, type="Volador"),
    Pokemon(id=8, name="Rattata", attack=7, life=25, type="Normal"),
    Pokemon(id=9, name="Spearow", attack=8, life=27, type="Volador"),
    Pokemon(id=10, name="Ekans", attack=9, life=30, type="Veneno"),
    Pokemon(id=11, name="Sandshrew", attack=10, life=35, type="Tierra"),
    Pokemon(id=12, name="Nidoran", attack=9, life=33, type="Veneno"),
    Pokemon(id=13, name="Clefairy", attack=7, life=40, type="Hada"),
    Pokemon(id=14, name="Vulpix", attack=11, life=32, type="Fuego"),
    Pokemon(id=15, name="Jigglypuff", attack=6, life=45, type="Normal"),
    Pokemon(id=16, name="Zubat", attack=8, life=30, type="Volador"),
    Pokemon(id=17, name="Oddish", attack=7, life=35, type="Planta"),
    Pokemon(id=18, name="Paras", attack=9, life=28, type="Bicho"),
    Pokemon(id=19, name="Venonat", attack=8, life=32, type="Bicho"),
    Pokemon(id=20, name="Diglett", attack=10, life=25, type="Tierra"),
    Pokemon(id=21, name="Meowth", attack=9, life=30, type="Normal"),
    Pokemon(id=22, name="Psyduck", attack=10, life=34, type="Agua"),
    Pokemon(id=23, name="Mankey", attack=12, life=33, type="Lucha"),
    Pokemon(id=24, name="Growlithe", attack=13, life=36, type="Fuego"),
    Pokemon(id=25, name="Poliwag", attack=8, life=29, type="Agua"),
    Pokemon(id=26, name="Abra", attack=6, life=25, type="Psíquico"),
    Pokemon(id=27, name="Machop", attack=14, life=40, type="Lucha"),
    Pokemon(id=28, name="Bellsprout", attack=9, life=34, type="Planta"),
    Pokemon(id=29, name="Tentacool", attack=8, life=33, type="Agua"),
    Pokemon(id=30, name="Geodude", attack=13, life=38, type="Roca"),
    Pokemon(id=31, name="Ponyta", attack=12, life=36, type="Fuego"),
    Pokemon(id=32, name="Slowpoke", attack=7, life=45, type="Agua"),
    Pokemon(id=33, name="Magnemite", attack=10, life=30, type="Eléctrico"),
    Pokemon(id=34, name="Farfetchd", attack=11, life=35, type="Volador"),
    Pokemon(id=35, name="Doduo", attack=12, life=33, type="Volador"),
    Pokemon(id=36, name="Seel", attack=9, life=37, type="Agua"),
    Pokemon(id=37, name="Grimer", attack=10, life=40, type="Veneno"),
    Pokemon(id=38, name="Shellder", attack=11, life=32, type="Agua"),
    Pokemon(id=39, name="Gastly", attack=13, life=28, type="Fantasma"),
    Pokemon(id=40, name="Onix", attack=15, life=45, type="Roca"),
    Pokemon(id=41, name="Drowzee", attack=9, life=35, type="Psíquico"),
    Pokemon(id=42, name="Krabby", attack=12, life=33, type="Agua"),
    Pokemon(id=43, name="Voltorb", attack=11, life=30, type="Eléctrico"),
    Pokemon(id=44, name="Exeggcute", attack=8, life=34, type="Planta"),
    Pokemon(id=45, name="Cubone", attack=13, life=36, type="Tierra"),
    Pokemon(id=46, name="Hitmonlee", attack=16, life=40, type="Lucha"),
    Pokemon(id=47, name="Hitmonchan", attack=15, life=40, type="Lucha"),
    Pokemon(id=48, name="Lickitung", attack=10, life=42, type="Normal"),
    Pokemon(id=49, name="Koffing", attack=11, life=38, type="Veneno"),
    Pokemon(id=50, name="Rhyhorn", attack=15, life=45, type="Tierra"),
]

#prueba
@app.get("/holalalallala")
def hello():
    return {"hello":"in FastAPI"}

# Endpoint para obtener todos los Pokémon
@app.get("/pokemons")
def get_all_pokemons():
    return pokemons_db
# Endpoint para Pokémon por nombre
@app.get("/pokemon/name/{name}")
def obtener_pokemon(name: str):
    for pokemon in pokemons_db:
        if pokemon.name.lower() == name.lower():
            return pokemon
    return {"error": "Pokemon no encontrado"}
# Endpoint para Pokémon por id
@app.get("/pokemon/id/{id}")
def get_pokemon_by_id(id: int):
    for pokemon in pokemons_db:
        if pokemon.id == id:
            return pokemon
    return {"error": "Pokemon no encontrado"}
# Endpoint para organizar pokemons por vida max
@app.get("/pokemons/sorted/life")
def sort_pokemons_by_life():
    sorted_pokemons = sorted(pokemons_db, key=lambda pokemon: pokemon.life, reverse=True)
    return sorted_pokemons

# Endpoint para simular batalla
@app.get("/battle/{id1}/{id2}")
def battle(id1: int, id2: int):

    pokemon1 = None
    pokemon2 = None

    for p in pokemons_db:
        if p.id == id1:
            pokemon1 = p
        if p.id == id2:
            pokemon2 = p

    if not pokemon1 or not pokemon2:
        return {"error": "Uno de los pokemons no existe"}

    log = []
    log.append(pokemon1.leavepokeball())
    log.append(pokemon2.leavepokeball())

    while pokemon1.life > 0 and pokemon2.life > 0:

        log.append(pokemon1.attack_enemy(pokemon2))

        if pokemon2.life <= 0:
            log.append(f"{pokemon2.name} fue derrotado")
            log.append(f"{pokemon1.name} gana la batalla!")
            break

        log.append(pokemon2.attack_enemy(pokemon1))

        if pokemon1.life <= 0:
            log.append(f"{pokemon1.name} fue derrotado")
            log.append(f"{pokemon2.name} gana la batalla!")
            break

    return {"resumen_batalla": log}