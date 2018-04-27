from command_pool import CommandPool
from command_handler import CommandHandler
from bs4 import BeautifulSoup
import requests



@CommandPool.register_command_class
class Test1421(CommandHandler):
    def handle(self, text):
        if text.startswith('stack: '):
            ask = text.split(':')[1]
            base_url = 'https://ru.stackoverflow.com/questions/tagged/{}'.format(ask)
            html = requests.get(base_url).text
            soup = BeautifulSoup(html, 'lxml')
            answers = soup.find('div', id='mainbar').find_all('div', class_='question-summary')
            for ans in answers:
                if ans.find('div', class_='status answered-accepted'):
                    result = ans.find('div', class_='excerpt').text
                    url = ans.find('a')
                    true_url = 'https://ru.stackoverflow.com/' + url.get('href')
                    break
            return str(result).strip() + '\n' + str(true_url)

if __name__ == '__main__':
    test = Test1421()
    result = test.handle('stack: python virtualenv')
    print(result)