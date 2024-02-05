import datetime ,random ,requests


class DynamicData:
    def __init__(self):
        self.timestamp = datetime.datetime.now()
        self.quotes = self.get_quotes()
        self.weather = self. get_weather()
    
    
    def get_quotes(self):
        Quotes = ["The greatest glory in living lies not in never falling, but in rising every tMandelaime we fall. -Nelson ",
                  "The way to get started is to quit talking and begin doing. -Walt Disney",
                  "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma - which is living with the results of other people's thinking. -Steve Jobs",
                  "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
                  "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
                  "If set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron ",
                  "You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one. -John Lennon ",
                  "You must be the change you wish to see in the world. -Mahatma Gandhi",
                  "Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that. -Martin Luther King Jr. "
                  ]
        num = random.randint(0,8)
        quote = Quotes[num]
        return  quote

    def get_weather(self):
        weather_api_url = "https://api.openweathermap.org/data/2.5/weather?lat=12.971599&lon=77.594566&appid=<api_key>"
        weather = requests.get(weather_api_url)
        data = weather.json()
        return data