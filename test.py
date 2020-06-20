from sqlserver import  *
mydb=conn()
head_1,head_2,head_3,head_4,query_data_1,query_data_2,query_data_3,query_data_4=three.query_1(mydb,'123')
print(head_3)
print(head_1,head_2,head_3,head_4)
print(query_data_1,query_data_2,query_data_3,query_data_4)