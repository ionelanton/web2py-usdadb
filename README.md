web2py-usdadb
=============

Overview
--------
Thanks to <a href='http://web2py.com'>web2py</a>'s DAL <a href='http://web2py.com/books/default/chapter/29/06'>(Database Abstraction Layer)</a>,
`web2py-usdadb` can import the USDA National Nutrient Database for Standard Reference  (SR26)
to the database of your choice: SQLite, MySQL, Postgresql, Oracle etc.

Requirements
------------
* Python 2.6.x

Utilization
------------
#. Copy the `web2py-usdadb` into a folder of your choice
#. Change the connection string in `model/db.py` to point to your database
#. run `python main.py` within `web2py-usdadb` folder

Imported tables
---------------
* food_group_description
* food_description
* nutrient_definition
* nutrient_data
* weight

Notes
-----
The USDA National Nutrient Database for Standard Reference can be found at:
https://www.ars.usda.gov/main/site_main.htm?modecode=12-35-45-00
