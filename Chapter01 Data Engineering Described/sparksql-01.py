from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("MyApp").getOrCreate()

#Dataset location
dloc='dataset/orders.csv'

print('\n'*5)
print('='*125)

df=spark.read.csv(dloc, header='true', inferSchema='true')

df.createOrReplaceTempView('vw_orders_bronze')

print('Temporary View created')

print()
print()
spark.sql("""
          
          select count(*) as Total_rows
          from vw_orders_bronze
          
          """).show()

print()
print()
spark.sql("""
          
          select product_category, count(*) as Orders_by_category
          from vw_orders_bronze
          group by product_category          
          """).show()

print('\n\nChecking if key details are missing in any row:')
spark.sql("""
          
          select * from vw_orders_bronze
          where customer_id is Null
          or quantity is Null
          
          """).show()
