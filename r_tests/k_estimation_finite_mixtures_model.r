

mydata <- read.table('/Users/rmaestre/Projects/Twitter-semantic-recommender/data/vectors_flat.tsv')
mydata <- na.omit(mydata)
#mydata <- scale(mydata)

wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata, 
  	 centers=i)$withinss)
plot(1:15, wss, type="b", xlab="Number of Clusters",
  ylab="Within groups sum of squares")


fit <- kmeans(mydata, 4) # 5 cluster solution
# get cluster means 
aggregate(mydata,by=list(fit$cluster),FUN=mean)
# append cluster assignment
mydata <- data.frame(mydata, fit$cluster)



#mydata <- na.omit(mydata)
#mydata <- scale(mydata)
#d <- dist(mydata, method = "minkowski") # distance matrix
#fit <- hclust(d, method="ward") 
#plot(fit) # display dendogram

#library(mclust)
#data <- na.omit(data)
#data <- scale(data)
#model <- Mclust(data)
#plot(model, data)
#print(fit)