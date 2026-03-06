from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Pokemon(BaseModel):
    id:int
    name:str
    attack:int    
    life:int
    type:str


pokemons_db = [
    Pokemon(id=1, name="Pikachu", attack=10, life=35, type="Eléctrico"),
    Pokemon(id=2, name="Bulbasaur", attack=8, life=40, type="Planta"),
    Pokemon(id=3, name="Charmander", attack=12, life=30, type="Fuego"),
]

@app.get("/holalalallala")
def hello():
    return {"hello":"in FastAPI"}

# Endpoint para obtener todos los Pokémon
@app.get("/pokemons")
def get_all_pokemons():
    return pokemons_db