from lib.web2py.dal import *

# DAL reference: http://www.web2py.com/book/default/chapter/06#The-database-abstraction-layer
db = DAL('sqlite://database/usdadb.sqlite')
#db = DAL('postgres://username:password@localhost/database')
#db = DAL('mysql://username:password@localhost/database')
#db=DAL('mssql://username:password@localhost/database')
#db=DAL('oracle://username/password@database')


# Avoid "no such table sqlite_sequence" error: sqlite_sequence table is not created,
# until you define at least one autoincrement and primary key column in your schema
db.define_table('dummy')

# Documentation reference: http://www.ars.usda.gov/SP2UserFiles/Place/12354500/Data/SR26/sr26_doc.pdf
db.define_table('food_group_description',
    Field('FdGrp_Cd', 'string', length=4, label='Code'),
    Field('FdGrp_Desc', 'string', length=60, label='Name'),
    primarykey=['FdGrp_Cd']
)

db.define_table('food_description',
    Field('NDB_No', 'string', length=5, label='ID'),
    Field('FdGrp_Cd', 'reference food_group_description', label='Food group'),
    Field('Long_Desc', 'string', length=200, label='Long description'),
    Field('Shrt_Desc', 'string', length=60, label='Short description'),
    Field('ComName', 'string', length=100, label='Other names'),
    Field('ManufacName', 'string', length=65, label='Company'),
    Field('Survey', 'string', length=1),
    Field('Ref_desc', 'string', length=135, label='Inedible parts'),
    Field('Refuse', 'integer', default=0, label='Inedible %'),
    Field('SciName', 'string', length=65, label='Scientific name'),
    Field('N_Factor', 'double'),
    Field('Pro_Factor', 'double'),
    Field('Fat_Factor', 'double'),
    Field('CHO_Factor', 'double'),
    primarykey=['NDB_No']
)

db.define_table('nutrient_definition',
    Field('Nutr_No', 'string', length=3, label='ID'),
    Field('Units', 'string', length=7),
    Field('Tagname', 'string', length=20, label='INFOODS name'),
    Field('NutrDesc', 'string', length=60, label='Name'),
    Field('SR_Order', 'integer', 'Order'),
    primarykey=['Nutr_No']
)

db.define_table('nutrient_data',
    Field('NDB_No', 'reference food_description', label='Food ID'),
    Field('Nutr_No', 'reference nutrient_definition', label='Nutrient ID'),
    Field('Nutr_Val', 'double', label='Edible amount in 100g'),
    Field('Num_Data_Pts', 'double', label='No. of analyses'),
    Field('Std_Error', 'double', label='Mean std. err.'),
    Field('Src_Cd', 'string', length=2, label='Data type code'),
    Field('Deriv_Cd', 'string', length=4, label='Data Derivation Code'),
    Field('Ref_NDB_No', 'string', length=5, label='NDB number'),
    Field('Add_Nutr_Mark', 'string', length=1, label='Fortified'),
    Field('Num_Studies', 'integer', label='Studies'),
    Field('Min_Val', 'double'),
    Field('Max_Val', 'double'),
    Field('DF', 'integer', label='Degrees of freedom'),
    Field('Low_EB', 'double', label='Lower 95% error bound'),
    Field('Up_EB', 'double', label='Upper 95% error bound'),
    Field('Stat_cmt', 'string', length=10, label='Statistical comments'),
    Field('AddMod_Date', 'string', length=10, label='Modified'),
    Field('CC', 'string', length=1, label='Confidence code'),
    primarykey=['NDB_No', 'Nutr_No']
)


db.define_table('weight',
    Field('NDB_No', 'reference food_description', label='Food ID'),
    Field('Seq', 'string', length=2, label='Sequence'),
    Field('Amount', 'double'),
    Field('Msre_Desc', 'string', length=100, label='Description'),
    Field('Gm_Wgt', 'double', label='Gram weight'),
    Field('Num_Data_Pts', 'integer', 'Data points'),
    Field('Std_Dev', 'double', label='Std. deviation'),
    primarykey=['NDB_No', 'Seq']
)