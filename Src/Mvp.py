def imprimir_ranking(ronda_puntos):
    print("\n Ronda: \n")
    print(f"{'Jugador':<10} {'Kills':<8} {'Asistencias':<12} {'Muertes':<8} {'Puntos':<8}")
    print("-" * 50)
    for jugador in sorted(ronda_puntos, key=lambda p: ronda_puntos[p]['puntos'], reverse=True):
        stats = ronda_puntos[jugador]
        print(f"{jugador:<10} {stats['kills']:<8} {stats['assists']:<12} {stats['deaths']:<8} {stats['puntos']:<8}")

def imprimir_partido(jugador):
   print("\nRanking final:\n")
   print(f"{'Jugador':<10} {'Kills':<8} {'Asistencias':<12} {'Muertes':<8} {'MVPs':<6} {'Puntos':<8}")
   for player in sorted(jugador, key=lambda p: jugador[p]['puntos'], reverse=True):
     stats = jugador[player]
     print(f"{player:<10} {stats['kills']:<8} {stats['assists']:<12} {stats['deaths']:<8} {stats['mvps']:<6} {stats['puntos']:<8}")  
             


def procesar_rondas(rondas):
    player_stats = {}
    for rondas in rondas:
     ronda_puntos = {}
     for jugador,stats in rondas.items():
        kills = stats['kills']
        assists = stats['assists']
        deaths = 1 if stats['deaths'] else 0
        score = 3 * kills + assists - deaths

        ronda_puntos[jugador] = {
            'kills': kills,
            'assists': assists,
            'deaths': deaths,
            'puntos': score
        }

        if jugador not in player_stats:
            player_stats[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'puntos': 0}
       
       
        player_stats[jugador]['kills'] += kills
        player_stats[jugador]['assists'] += assists    
        player_stats[jugador]['deaths'] += deaths
        player_stats[jugador]['puntos'] += score

     mvp = max(ronda_puntos, key=lambda p: ronda_puntos[p]['puntos'])
     player_stats[mvp]['mvps'] += 1
     imprimir_ranking(ronda_puntos)
    imprimir_partido(player_stats)
    return player_stats

             