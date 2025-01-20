textFile = spark.read.text("README.md?token=GHSAT0AAAAAACZTAM6DAU5FTPX2OOGNBV6WZ4KR4UA")
wordCounts = textFile.rdd.flatMap(lambda row: row[0].split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
wordCounts.collect()

