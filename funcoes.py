import requests
from cache_data import POKEMON_CACHE

BASE_URL = "https://pokeapi.co/api/v2/"

def get_types_list():
    """Retorna a lista de tipos para os filtros."""
    return ['normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dark', 'dragon', 'steel', 'fairy']

def get_pokemon_details(name_or_id, is_detail_page=False):
    """
    Busca detalhes de um Pokémon.
    is_detail_page=True: Busca descrição em PT e estatísticas completas.
    is_detail_page=False: Retorna apenas o básico (ideal para listagem rápida).
    """
    # 1. Tenta buscar no cache (Pokémon 1 a 64)
    try:
        pid = int(name_or_id)
        if pid in POKEMON_CACHE:
            p = POKEMON_CACHE[pid].copy()
            
            # Se for página de detalhes e o cache não tiver stats/descrição detalhada, busca na API
            if is_detail_page:
                res = requests.get(f"{BASE_URL}pokemon/{pid}").json()
                p['height'] = res['height']
                p['weight'] = res['weight']
                p['stats'] = {
                    "hp": res['stats'][0]['base_stat'],
                    "attack": res['stats'][1]['base_stat'],
                    "defense": res['stats'][2]['base_stat'],
                    "special_attack": res['stats'][3]['base_stat'],
                    "special_defense": res['stats'][4]['base_stat'],
                    "speed": res['stats'][5]['base_stat']
                }
                
                # Busca Descrição e Evoluções (mesmo para os do cache, para garantir a cadeia completa)
                species_res = requests.get(res['species']['url']).json()
                
                # Lógica de tradução para Português
                p['description'] = "Descrição não disponível."
                for entry in species_res['flavor_text_entries']:
                    if entry['language']['name'] in ['pt', 'pt-br']:
                        p['description'] = entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
                        break
                    elif entry['language']['name'] == 'en' and p['description'] == "Descrição não disponível.":
                        p['description'] = entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')

                # Busca Cadeia de Evolução
                evo_url = species_res['evolution_chain']['url']
                evo_data = requests.get(evo_url).json()
                p['evolutions'] = []
                
                curr = evo_data['chain']
                while curr:
                    eid = curr['species']['url'].split('/')[-2]
                    p['evolutions'].append({
                        "id": int(eid),
                        "name": curr['species']['name'].capitalize(),
                        "image": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{eid}.png",
                        "is_current": int(eid) == pid
                    })
                    curr = curr['evolves_to'][0] if curr['evolves_to'] else None
            return p
    except:
        pass

    # 2. Fallback para API (Pokémon > 64 ou busca por nome)
    try:
        res = requests.get(f"{BASE_URL}pokemon/{str(name_or_id).lower()}")
        if res.status_code != 200: return None
        data = res.json()

        p_data = {
            "id": data['id'],
            "name": data['name'].capitalize(),
            "types": [t['type']['name'] for t in data['types']],
            "image": data['sprites']['other']['official-artwork']['front_default'],
            "height": data['height'],
            "weight": data['weight'],
            "stats": {
                "hp": data['stats'][0]['base_stat'],
                "attack": data['stats'][1]['base_stat'],
                "defense": data['stats'][2]['base_stat'],
                "special_attack": data['stats'][3]['base_stat'],
                "special_defense": data['stats'][4]['base_stat'],
                "speed": data['stats'][5]['base_stat']
            },
            "description": "",
            "evolutions": []
        }

        # Busca dados da espécie (Sempre necessário para Evolução e Descrição)
        species_res = requests.get(data['species']['url']).json()
        
        # Descrição em Português
        for entry in species_res['flavor_text_entries']:
            if entry['language']['name'] in ['pt', 'pt-br']:
                p_data['description'] = entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
                break
            elif entry['language']['name'] == 'en' and not p_data['description']:
                p_data['description'] = entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')

        # Cadeia de Evolução
        evo_url = species_res['evolution_chain']['url']
        evo_data = requests.get(evo_url).json()
        
        curr = evo_data['chain']
        while curr:
            eid = curr['species']['url'].split('/')[-2]
            p_data["evolutions"].append({
                "id": int(eid),
                "name": curr['species']['name'].capitalize(),
                "image": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{eid}.png",
                "is_current": int(eid) == data['id']
            })
            curr = curr['evolves_to'][0] if curr['evolves_to'] else None
        
        return p_data
    except:
        return None

def get_paginated_pokemon(offset=0, limit=64):
    """Gera a lista de Pokémon para a home."""
    final_list = []
    for i in range(offset + 1, offset + limit + 1):
        if i > 1025: break 
        # Na listagem principal, is_detail_page=False para ser rápido
        p = get_pokemon_details(i, is_detail_page=False)
        if p: final_list.append(p)
    return final_list