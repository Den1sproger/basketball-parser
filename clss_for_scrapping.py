import json

from scrapping_tools import Basketball
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup



class Fill_Table(Basketball):

    def fill_table(self, string_number: int = 5) -> None:
        # Fill the excel table with game data
        # Заполнить excel таблицу данными о матчах
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        games_bs = soup.find_all('div', class_='event__match')
        games_sl = self.driver.find_elements(By.CLASS_NAME, 'event__match')
        count = 0
        count_xl = string_number
        games_number = {}
        for game in games_bs:
            time = game.find('div', class_='event__stage--block')
            if time is None:
                time = game.find('div', class_='event__time').text
            else:
                time = time.text.replace(' ', ' ')
            team_1 = game.find('div', class_='event__participant--home').text.strip()
            self.sheet[f'D{count_xl}'] = team_1
            games_number[team_1] = count_xl
            self.sheet[f'D{count_xl + 1}'] = game \
                .find('div', class_='event__participant--away').text.strip()
            self.update_info(
                game=game, count_xl=count_xl,
                game_sl=games_sl[count], first_use=True,
                time=time
            )
            count += 1
            count_xl += 2

        self._close_driver

        with open('games_strings.json', 'w', encoding='utf-8') as file:
            json.dump(games_number, file, indent=4, ensure_ascii=False)



class Monitoring(Basketball):

    def monitoring(self):
        # Monitoring completed in the excel table games
        # Мониторинг заполненных в таблицу матчей
        with open('games_strings.json', 'r', encoding='utf-8') as file:
            games_strings = json.load(file)

        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        begin_games = len(soup.find_all('div', class_='event__match'))
        finish_games = []
        stop = False

        while not stop:
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            games_bs = soup.find_all('div', class_='event__match')
            count = 0

            for game in games_bs:
                if game in finish_games:
                    pass
                else:
                    time = game.find('div', class_='event__stage--block')
                    if time is None:
                        time = game.find('div', class_='event__time').text.strip()
                    else:
                        time = time.text.replace(' ', ' ')

                    team_1 = game.find('div', class_='event__participant--home').text.strip()
                    xl_string = games_strings.get(team_1)
                    if ('1-я четверть 10' in time) or \
                        ('2-я четверть 10' in time) or \
                        ('3-я четверть 10' in time):
                        self.update_info(
                            game=game, time=time,
                            count_xl=xl_string
                        )
                    elif 'Завершен' in time:
                        self.update_info(
                            game=game, time=time,
                            count_xl = xl_string
                        )
                        finish_games.append(game)
                        if len(finish_games) >= begin_games:
                            stop = True
                            break
                count += 1

            sleep(60)
            
        self._close_driver()