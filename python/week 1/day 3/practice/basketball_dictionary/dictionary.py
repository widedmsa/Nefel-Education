players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    new_team=[]
    def __init__(self,value):
        self.name=value["name"]
        self.age = value["age"]
        self.position=value["position"]
        self.team= value["team"]

    def display_info(self):
        print(f"Name: {self.name}\nAge : {self.age}\nPosition : {self.position} \nTeam : {self.team}")


first_player = Player(players[0])
first_player.display_info()

second_player= Player(players[3])
second_player.display_info()

third_player=Player(players[2])
third_player.display_info()

new_list = []
for i in range (len(players)) :
    new_list.append(Player(players[i]))
    
