import os
import urllib2
from model.db import db


def import_usda_data():
    delimiter = '^'
    quotechar = '~'

    usda_data = [  # (table_name, usda_ascii_file_url)
        ('food_group_description', 'https://www.ars.usda.gov/SP2UserFiles/Place/12354500/Data/SR26/asc/FD_GROUP.txt'),
        ('food_description', 'http://www.ars.usda.gov/SP2UserFiles/Place/12354500/Data/SR26/asc/FOOD_DES.txt'),
        ('nutrient_definition', 'http://www.ars.usda.gov/SP2UserFiles/Place/12354500/Data/SR26/asc/NUTR_DEF.txt'),
        ('nutrient_data', 'http://www.ars.usda.gov/SP2UserFiles/Place/12354500/Data/SR26/asc/NUT_DATA.txt'),
        ('weight', 'http://www.ars.usda.gov/SP2UserFiles/Place/12354500/Data/SR26/asc/WEIGHT.txt'),
    ]

    for table_name, url in usda_data:
        csv_file_path = os.path.join('uploads', table_name + '.csv')
        _upload_data(table_name, url, csv_file_path, delimiter, quotechar)
        os.remove(csv_file_path)

    print 'USDA database created/updated!'


def _upload_data(table_name, url, csv_file_path, delimiter, quotechar):

    print 'Creating/updating "' + table_name + '"...'

    csv_file = urllib2.urlopen(urllib2.Request(url)).read()

    f = open(csv_file_path, 'w')
    f.write(_get_csv_header(table_name))
    f.write('\r\n')
    f.write(csv_file)
    f.close()
    f = open(csv_file_path, 'r')
    db[table_name].import_from_csv_file(f, restore=True, delimiter=delimiter, quotechar=quotechar)
    db.commit()
    f.close()

    print 'Done!'


def _get_csv_header(table_name):
    csv_fields = ''
    for field in db[table_name].fields:
        if 'id' != field:
            csv_fields += '~' + table_name + '.' + str(field) + '~^'
    return csv_fields[:-1]

import_usda_data()

