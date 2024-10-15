from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("FinancialTransactionsMonitoring") \
    .getOrCreate()

# Load data from S3
input_path = "s3://your-bucket-name/data/transactions.csv"
transactions_df = spark.read.csv(input_path, header=True, inferSchema=True)

# Transform: Flag fraudulent transactions
fraudulent_df = transactions_df.withColumn(
    "is_fraud",
    when((col("amount") > 10000) & (col("transaction_type") == "withdrawal"), True).otherwise(False)
)

# Process transactions
fraudulent_count = fraudulent_df.filter(col("is_fraud") == True).count()
print(f"Total fraudulent transactions flagged: {fraudulent_count}")

# Save flagged transactions back to S3
output_path = "s3://your-bucket-name/output/fraudulent_transactions.csv"
fraudulent_df.write.csv(output_path, header=True)

# Stop Spark session
spark.stop()
