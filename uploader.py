from my_settings import JSON_PATH, SHEET_PATH
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pprint

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monmal_uploader.settings")

import django
django.setup()

from uploader.models import Category, SubCategory, Tag, Text, Chunk, TextToChunk, Dictionary


scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

json_file_name = JSON_PATH
spreadsheet_url = SHEET_PATH
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)

gc = gspread.authorize(credentials)
doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet('upload_test')

# values_list = worksheet.row_values(1)
# print(values_list) # ['textId', 'order', 'chunk']

list_of_lists = worksheet.get_all_values()
# pprint.pprint(list_of_lists[1])
CATEGORY = '고전문학'
SUBCATEGORY = '가정문학'
TAG = ['연행록', '가정적'] ## 리스트 구현 필요
TEXT = '북학의'

# category upload
category, created = Category.objects.get_or_create(name = CATEGORY)
if created:
    print(f"success created {category}")

# subCategory upload
categoryInfo = Category.objects.get(name = CATEGORY)
print(categoryInfo.id)

subcategory, created = SubCategory.objects.get_or_create(
    name     = SUBCATEGORY,
    category = Category.objects.get(name = CATEGORY)
    )
if created:
    print(f"success created {subcategory}")

# tag upload
for item in TAG:
    tag, created = Tag.objects.get_or_create(name = item)
    if created:
        print(f"success created {tag}")

# text upload
text, created = Text.objects.get_or_create(
    name        = TEXT,
    category    = Category.objects.get(name = CATEGORY),
    subcategory = SubCategory.objects.get(name = SUBCATEGORY),
    tag         = Tag.objects.get(name = TAG)
    )
if created:
    print(f"success created {category}")

# chunk upload
for row in list_of_lists:
    print(row) # ['1', '1', '18']
    chunk, created = Chunk.objects.get_or_create(name = row[2])
    if created:
        print(f"success created {chunk}")

# chunkToText upload
textInfo  = Text.objects.get(name = TEXT)

for row in list_of_lists:
    print(row) # ['1', '2', '세기']
    textToChunk, created = TextToChunk.objects.get_or_create(
        text  = Text.objects.get(name = TEXT),
        chunk = Chunk.objects.get(name = row[2]),
        order = row[1] 
        )
    if created:
        # print(f"success created {textToChunk}")
        print('success created')

