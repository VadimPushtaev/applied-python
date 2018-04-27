from command_pool import CommandPool
from command_handler import CommandHandler
from bs4 import BeautifulSoup
import requests



@CommandPool.register_command_class
class StackOverFlow(CommandHandler):
    def handle(self, text):
        if text.startswith('Stack '):
            ask = text[6:].replace(' ', '+')
            base_url = 'https://ru.stackoverflow.com/search?q={}'.format(ask)
            html = requests.get(base_url).text
            soup = BeautifulSoup(html, 'lxml')
            answers = soup.find('div', id='mainbar').find_all('div', class_='question-summary')
            result = 'Not found'
            true_url = 'Not found'
            for ans in answers:
                if ans.find('div', class_='status answered-accepted'):
                    result = ans.find('div', class_='excerpt').text
                    result = ' '.join(result.split())
                    url = ans.find('a')
                    true_url = 'https://ru.stackoverflow.com/' + url.get('href')
                    break
            return str(result).strip() + '\n' + str(true_url)

if __name__ == '__main__':
    s = StackOverFlow()
    result = s.handle('Stack python virtualenv')
    print(result)
