import requests

class PlayerModel:
    def __init__(self, id, username, email, password, created_on, max_score, coins):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_on = created_on
        self.max_score = max_score
        self.coins = coins

    def save_data(self):
        data = {
            "max_score": self.max_score
        }

        r = requests.put(f"http://127.0.0.1:5000/player/{self.id}", json=data)
