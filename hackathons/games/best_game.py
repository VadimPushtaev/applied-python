from datetime import datetime
import sys
from timeit import default_timer as timer
import random

from BaseGame import BaseGame

#random.randrange()

#Сергей Бакаев, Лера Соколовская, Александр Назаров
#оманда ЛУчших

class Game:
    def __init__(self):
        self.player = list()
        self.text = str()
        self.start = int()
        self.end = int()
        self.quiz_easy = {'Цвет неба?':'Голубой, синий, Синий, голубой, Фукси',
                          'Цвет солнышка?':'Желтый, желтый, желтенький',
                          'Как зовут Отца Марьи Ивановны?': 'Иван',
                          'Сколько хвостов у питона?': 'Один, 1, один',
                          'Наша планета?':'Земля, земля',
                          'Сколько пальцев у человека?':'20',
                          'С какой ноги ты встал, если у тебя только левая?': 'Левая с левой',
                          'Кто будет президентом России в 2024?': 'Putin Путин'}
        self.quiz_hard = {'Наша планета?':'Земля, земля',
                          'Сколько пальцев у человека?':'20',
                          'С какой ноги ты встал, если у тебя только левая?': 'Левая с левой',
                          'Кто будет президентом России в 2024?': 'Putin Путин'}
        self.keys = []
        self.keys_hard = []
        self.list_time = list()
        self.time = ()
        self.counter = 0

    def add_scores(self, score):
        pass

    def question_hardesty(self):
        text = str(input("{}, выбери уровень сложности: (EASY/HARD) ".format(self.player[-1])))
        if text == r'EASY':
            return self.answer_easy()
                
        elif text == r'HARD':
            return self.answer_easy()
        else:
            print('Пиши EASY ли HARD')
            self.question_hardesty()

    def answer_easy(self):
        
        print("На каждый вопрос у тебя 7 секунд")
        print("          Вперед!")
        
        start_time = timer()
        for i in range(7):
            new_time = timer()
            question = random.choice(self.keys)
            flag = False
            while True:
                l = input(question)
                delta = timer() - new_time
                if delta > 7:
                    flag = True
                    break
                if l:
                    break
            if flag:
                print('Время истекло')

                n = self.keys.remove(question)

                continue
                
            if l in self.quiz_easy.setdefault(question):
                print('Ты прав!')

                self.keys.remove(question)
                self.counter += 1
                continue

            else:
                n = self.keys.remove(question)
                print('Ты не прав!')
                continue
            
        end_time = timer() - start_time
        if not self.counter:
            print('Ты ничего не заработал. Сожалеем.')
            return True
        ochko = end_time/self.counter
        ochko = ochko//1
        print('Твои очки:',ochko)
        
        self.add_scores(ochko)
        
    def answer_hard(self):
        print("На каждый вопрос у тебя 10 секунд")
        print("          Вперед!")
        
        start_time = timer()
        for i in range(4):
            new_time = timer()
            question = random.choice(self.keys_hard)
            flag = False
            while True:
                l = input(question)
                delta = timer() - new_time
                if delta > 10:
                    flag = True
                    break
                if l:
                    break
            if flag:
                print('Время истекло')

                n = self.keys_hard.remove(question)

                continue
                
            if l in self.quiz_hard.setdefault(question):
                print('Ты прав!')

                self.keys_hard.remove(question)
                self.counter += 1
                continue

            else:
                n = self.keys_hard.remove(question)
                print('Ты не прав!')
                continue
            
        end_time = timer() - start_time
        if not self.counter:
            print('Ты ничего не заработал. Сожалеем.')
            return True
        ochko = end_time/self.counter
        ochko = ochko//1
        print('Твои очки:',ochko)
        self.add_scores(ochko)

    def run(self):
        print('        ПРАВИЛА:')
        print('Чем быстрее и точнее ты отвечаешь, тем больше очков получишь!')
        key_names = list(self.quiz_easy.keys())
        self.keys = key_names
        name = input("Как к тебе обращаться?")
        self.player.append(name)

        k = self.question_hardesty()

        return(k)
name = 'Serg'
score = 0
class Starter(BaseGame):
    def run(self):
        
        n = Game()
        n.run()
        
        
t = Starter(name, score)

t.run()
