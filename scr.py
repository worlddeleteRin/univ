import pandas as pd
from lessons.models import * 
import os
# import pathlib

# PATH = pathlib.Path().absolute()
PATH = os.getcwd()
image_path = 'static/images/'

def create_teachers():
    print('-----------------------')
    print('Start creating teachers')
    print('-----------------------')
    data = pd.read_csv(PATH + '/data/teachers.csv')
    for index, item in data.iterrows():
        teacher = Teacher(
            name = item['name'],
            imgurl = image_path + item['imgurl'],
        )
        teacher.save()

    print('-----------------------')
    print('End creating teachers')
    print('-----------------------')

def create_subjects():
    print('-----------------------')
    print('Start creating subjects')
    print('-----------------------')
    data = pd.read_csv(PATH + '/data/subjects.csv')
    for index, item in data.iterrows():
        subject = Subject(
            name = item['name'],
            imgurl = image_path + item['imgurl'],
        )
        subject.save()
        print('create subjects', subject.name)
        print('start adding teacher for ', subject.name)
        for t in eval(item['teacher']):
            print('teacher: ', t)
            current_teacher = Teacher.objects.get(name = t)
            subject.s_teacher.add(current_teacher)
    print('-----------------------')
    print('End creating subjects')
    print('-----------------------')

def create_item_types():
    print('-----------------------')
    print('Start creating types')
    print('-----------------------')
    all_types = [
        'Общая информация',
        'Теоретический раздел',
        'Практический раздел'
    ]
    for item in all_types:
        new_type = Itemtypes(
            name = item
        )
        new_type.save()
    print('-----------------------')
    print('End creating types')
    print('-----------------------')


def createall():
    create_teachers()
    create_subjects()
    # create_item_types()


if __name__ == "__main__":
    createall()
        
