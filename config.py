import os

import openpyxl

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
START_PAGE = 'https://www.flashscorekz.com/favourites/'
EXCEL_FILE = "work_table.xlsx"

WB = openpyxl.load_workbook(filename=EXCEL_FILE, data_only=True)
SHEET = WB['Лист1']
LOGIN = SHEET['X3'].value
PASSWORD = SHEET['X4'].value
CHAT_ID = SHEET['X6'].value
