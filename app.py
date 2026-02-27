from flask import Flask, render_template, request, jsonify
from funcoes import get_paginated_pokemon, get_pokemon_details, get_types_list
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Parâmetros de busca e paginação
    search = request.args.get('search')
    tipo = request.args.get('type')
    offset = int(request.args.get('offset', 0))
    
    # Se for o carregamento inicial (offset 0), traz 64 (do cache).
    # Caso contrário, traz os próximos 8.
    limit = 64 if offset == 0 else 8
    
    pokemons = []
    show_back_button = False
    
    if search:
        # Busca por nome ou ID (is_detail_page=False para ser rápido na home)
        p = get_pokemon_details(search, is_detail_page=False)
        if p:
            pokemons.append(p)
        show_back_button = True
    elif tipo:
        # Filtro por tipo (limitado para performance)
        try:
            res = requests.get(f"https://pokeapi.co/api/v2/type/{tipo.lower()}").json()
            for item in res['pokemon'][:12]:
                p_detail = get_pokemon_details(item['pokemon']['name'], is_detail_page=False)
                if p_detail:
                    pokemons.append(p_detail)
            show_back_button = True
        except:
            pokemons = []
    else:
        # Carregamento normal paginado
        pokemons = get_paginated_pokemon(offset, limit)

    return render_template('index.html', 
                           pokemons=pokemons, 
                           types=get_types_list(), 
                           next_offset=offset + limit,
                           is_search=bool(search or tipo),
                           show_back_button=show_back_button)

# --- NOVA ROTA PARA CARREGAR MAIS VIA AJAX ---
@app.route('/api/pokemons')
def api_pokemons():
    """Rota que devolve Pokémon em JSON para o JavaScript anexar à lista existente."""
    offset = int(request.args.get('offset', 0))
    limit = 8
    pokemons = get_paginated_pokemon(offset, limit)
    
    # Retornamos os dados e o próximo offset para o botão continuar a funcionar
    return jsonify({
        "pokemons": pokemons, 
        "next_offset": offset + limit
    })

@app.route('/pokemon/<name_or_id>')
def pokemon_detalhe(name_or_id):
    # is_detail_page=True força a busca de descrição em PT e status completos
    pokemon = get_pokemon_details(name_or_id, is_detail_page=True)
    
    if not pokemon:
        return "Pokémon não encontrado", 404
        
    return render_template('detalhes.html', pokemon=pokemon)

if __name__ == '__main__':
    app.run(debug=True)