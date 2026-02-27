# cache_data.py

def get_evo_list(ids, current_id):
    """Gera a lista de evolução com base nos IDs fornecidos."""
    names = {
        1: "Bulbasaur", 2: "Ivysaur", 3: "Venusaur", 4: "Charmander", 5: "Charmeleon", 6: "Charizard",
        7: "Squirtle", 8: "Wartortle", 9: "Blastoise", 10: "Caterpie", 11: "Metapod", 12: "Butterfree",
        13: "Weedle", 14: "Kakuna", 15: "Beedrill", 16: "Pidgey", 17: "Pidgeotto", 18: "Pidgeot",
        19: "Rattata", 20: "Raticate", 21: "Spearow", 22: "Fearow", 23: "Ekans", 24: "Arbok",
        25: "Pikachu", 26: "Raichu", 27: "Sandshrew", 28: "Sandslash", 29: "Nidoran-f", 30: "Nidorina",
        31: "Nidoqueen", 32: "Nidoran-m", 33: "Nidorino", 34: "Nidoking", 35: "Clefairy", 36: "Clefable",
        37: "Vulpix", 38: "Ninetales", 39: "Jigglypuff", 40: "Wigglytuff", 41: "Zubat", 42: "Golbat",
        43: "Oddish", 44: "Gloom", 45: "Vileplume", 46: "Paras", 47: "Parasect", 48: "Venonat",
        49: "Venomoth", 50: "Diglett", 51: "Dugtrio", 52: "Meowth", 53: "Persian", 54: "Psyduck",
        55: "Golduck", 56: "Mankey", 57: "Primeape", 58: "Growlithe", 59: "Arcanine", 60: "Poliwag",
        61: "Poliwhirl", 62: "Poliwrath", 63: "Abra", 64: "Kadabra"
    }
    return [
        {
            "id": i, 
            "name": names[i], 
            "image": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{i}.png",
            "is_current": i == current_id
        } for i in ids if i in names
    ]

# Lista de tuplos: (ID, Nome, Tipos, IDs da linha evolutiva)
RAW_DATA = [
    (1, "Bulbasaur", ["grass", "poison"], [1,2,3]), (2, "Ivysaur", ["grass", "poison"], [1,2,3]), (3, "Venusaur", ["grass", "poison"], [1,2,3]),
    (4, "Charmander", ["fire"], [4,5,6]), (5, "Charmeleon", ["fire"], [4,5,6]), (6, "Charizard", ["fire", "flying"], [4,5,6]),
    (7, "Squirtle", ["water"], [7,8,9]), (8, "Wartortle", ["water"], [7,8,9]), (9, "Blastoise", ["water"], [7,8,9]),
    (10, "Caterpie", ["bug"], [10,11,12]), (11, "Metapod", ["bug"], [10,11,12]), (12, "Butterfree", ["bug", "flying"], [10,11,12]),
    (13, "Weedle", ["bug", "poison"], [13,14,15]), (14, "Kakuna", ["bug", "poison"], [13,14,15]), (15, "Beedrill", ["bug", "poison"], [13,14,15]),
    (16, "Pidgey", ["normal", "flying"], [16,17,18]), (17, "Pidgeotto", ["normal", "flying"], [16,17,18]), (18, "Pidgeot", ["normal", "flying"], [16,17,18]),
    (19, "Rattata", ["normal"], [19,20]), (20, "Raticate", ["normal"], [19,20]),
    (21, "Spearow", ["normal", "flying"], [21,22]), (22, "Fearow", ["normal", "flying"], [21,22]),
    (23, "Ekans", ["poison"], [23,24]), (24, "Arbok", ["poison"], [23,24]),
    (25, "Pikachu", ["electric"], [25,26]), (26, "Raichu", ["electric"], [25,26]),
    (27, "Sandshrew", ["ground"], [27,28]), (28, "Sandslash", ["ground"], [27,28]),
    (29, "Nidoran-f", ["poison"], [29,30,31]), (30, "Nidorina", ["poison"], [29,30,31]), (31, "Nidoqueen", ["poison", "ground"], [29,30,31]),
    (32, "Nidoran-m", ["poison"], [32,33,34]), (33, "Nidorino", ["poison"], [32,33,34]), (34, "Nidoking", ["poison", "ground"], [32,33,34]),
    (35, "Clefairy", ["fairy"], [35,36]), (36, "Clefable", ["fairy"], [35,36]),
    (37, "Vulpix", ["fire"], [37,38]), (38, "Ninetales", ["fire"], [37,38]),
    (39, "Jigglypuff", ["normal", "fairy"], [39,40]), (40, "Wigglytuff", ["normal", "fairy"], [39,40]),
    (41, "Zubat", ["poison", "flying"], [41,42]), (42, "Golbat", ["poison", "flying"], [41,42]),
    (43, "Oddish", ["grass", "poison"], [43,44,45]), (44, "Gloom", ["grass", "poison"], [43,44,45]), (45, "Vileplume", ["grass", "poison"], [43,44,45]),
    (46, "Paras", ["bug", "grass"], [46,47]), (47, "Parasect", ["bug", "grass"], [46,47]),
    (48, "Venonat", ["bug", "poison"], [48,49]), (49, "Venomoth", ["bug", "poison"], [48,49]),
    (50, "Diglett", ["ground"], [50,51]), (51, "Dugtrio", ["ground"], [50,51]),
    (52, "Meowth", ["normal"], [52,53]), (53, "Persian", ["normal"], [52,53]),
    (54, "Psyduck", ["water"], [54,55]), (55, "Golduck", ["water"], [54,55]),
    (56, "Mankey", ["fighting"], [56,57]), (57, "Primeape", ["fighting"], [56,57]),
    (58, "Growlithe", ["fire"], [58,59]), (59, "Arcanine", ["fire"], [58,59]),
    (60, "Poliwag", ["water"], [60,61,62]), (61, "Poliwhirl", ["water"], [60,61,62]), (62, "Poliwrath", ["water", "fighting"], [60,61,62]),
    (63, "Abra", ["psychic"], [63,64]), (64, "Kadabra", ["psychic"], [63,64])
]

POKEMON_CACHE = {}

for id, name, types, evos in RAW_DATA:
    POKEMON_CACHE[id] = {
        "id": id,
        "name": name,
        "types": types,
        "image": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png",
        "height": 0, "weight": 0, "stats": {}, "description": "", 
        "evolutions": get_evo_list(evos, id)
    }