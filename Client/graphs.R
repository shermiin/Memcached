library(lattice)

csvDataFrame <- read.csv("output-throughput-latency/stats.csv", header=TRUE, sep=",")

trellis.device("pdf", file="graph1.pdf", color=T, width=6.5, height=5.0)

plot(csvDataFrame$response, csvDataFrame$rate, type="o", xlab="Response Rate", ylab="Request Rate")

dev.off() -> null

trellis.device("pdf", file="graph2.pdf", color=T, width=6.5, height=5.0)

plot(csvDataFrame$response, csvDataFrame$latency, type="o", xlab="Response Rate", ylab="Latency")

dev.off() -> null
