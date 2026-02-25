import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python310\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python310\python.exe"
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()

data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

df = spark.createDataFrame(data, columns)

df.groupBy("category").sum("value").show()

spark.stop()