from pyspark.sql import SparkSession, functions as f

spark = SparkSession.builder.master("local[*]").appName("MyApp").getOrCreate()

#Dataset location
dloc='dataset/orders.csv'

print('\n'*5)
print('='*125)

df=spark.read.csv(dloc, header='true', inferSchema='true')
print(f'Dataset read: {dloc}\n\n\nFollowing are few rows from dataset:')

df.show(5)

print('\n\nSchema of the dataset used:')
df.printSchema()

print(f'\n\nTotal rows in dataset: {df.count()}')

print('\nCount of Null values in each column:')
# for i in df.columns:
#     print(f"{i}:{df.filter(f.col(i).isNull()).count()}")

nullc_df=df.select([
    f.sum(f.col(c).isNull().cast("int")).alias(c)    
    for c in df.columns
])

nullc_df.show()


print('='*125)
print('\n'*5)