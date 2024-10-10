import requests
from bs4 import BeautifulSoup

def get_top_100_players():
    url = "https://www.op.gg/leaderboards/tier"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        players = []
        
        # Find the elements containing player names and LP
        for row in soup.select('tr'):
            ## rank_tag = row.select_one('.css-1gozr20.e1br5d1')
            name_tag = row.select_one('.summoner-link .css-ao94tw')
            lp_tag = row.select_one('.css-1oruqdu span')
            profile_link_tag = row.select_one('.summoner-link')
            
            
            if name_tag and lp_tag and profile_link_tag: ##and rank_tag:
                name = name_tag.text.strip()
                lp = lp_tag.text.strip()
                ## rank = rank_tag.text.strip()
                profile = "https://www.op.gg" + profile_link_tag['href']
                players.append({
                ##     'rank': rank,
                    'name': name,
                    'LP': lp,
                    'profile': profile
                })
        return players[:100]  # Return only the top 100 players
    else:
        return None
    
if __name__ == "__main__":
    top_100_players = get_top_100_players()
    if top_100_players:
        for player in top_100_players:
            print(player)
    else:
        print("No players found.")