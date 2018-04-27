from command_pool import CommandPool
from command_handler import CommandHandler

import requests
import json
import urllib

@CommandPool.register_command_class
class YahooWeatherForecast(CommandHandler):
      def handle(self, city):
            if not city.startswith('Weather'):
                return None

            city = city[7:].strip()

            if city.startswith('id'):
                response = requests.get(
                    'https://api.vk.com/method/users.get?user_ids={}&fields=city&lang=en&v=5.74'.format(city.split()[1]))

                data = json.loads(response.text)

                city = data['response'][0]['city']['title']

            url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather." \
                  "forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%" \
                  "20text%3D%22{}%22)%20and%20u%20%3D%20%22c%22&format=json&env=store%3A%2F%2Fdatatables." \
                  "org%2Falltableswithkeys".format(city)
            data = requests.get(url).json()
            try:
                forecast_data = data['query']['results']['channel']['item']['forecast']
            except TypeError:
                return 'Incorrect city name'
            day_data = forecast_data[0]
            forecast = {
                  'Date': day_data['date'],
                  'Low_temp': day_data['low'],
                  'High_temp': day_data['high'],
                  'Comment': day_data['text']
            }

            forecast_string = 'Date: {0}\nLow temp.: {1}\nHigh temp.: {2}\nType: {3}\n'.format(
                                                                                    day_data['date'],
                                                                                    day_data['low'],
                                                                                    day_data['high'],
                                                                                    day_data['text']
                                                                                    )

            return forecast_string