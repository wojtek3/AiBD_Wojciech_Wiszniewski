# zadanie 1
library(magrittr)

list <- 1:10
list %<>% log2 %>% sin %>% sum %>% sqrt
print(list)
data("iris")
print(head(iris, 5))
print(aggregate(. ~ Species, data=iris, mean))

# zadanie 2
#install.packages("ggplot2")
#install.packages("GGally")
library("ggplot2")
library("GGally")
means <- aggregate(. ~ Species, data=iris, mean)
wykres1 <- ggplot(data=iris, aes(x=Sepal.Length, color=Species)) + geom_histogram() + geom_vline(xintercept=means[, 2])
ggsave("/home/wykres1.jpg", plot = wykres1)
wykres2 <- ggpairs(data=iris, aes(color=Species))
ggsave("/home/wykres2.jpg", plot = wykres2)

# zadanie 3
library(cluster)
x <- iris[, 1:4]
y <- iris[,5]
sum_sqr <-c()
for (i in 1:10){
kmeans_result <- kmeans(x, i)
sum_sqr <- append(sum_sqr, kmeans_result$tot.withinss)
}
wykres3 <- ggplot(data.frame(iteration = 1:length(sum_sqr), value = sum_sqr), aes(x = iteration, y = sum_sqr)) +
geom_line()
ggsave("/home/wykres3.jpg", plot = wykres3)
kmeans_result <- kmeans(x, 3)
wykres4 <- ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color= kmeans_result$cluster)) + geom_point()
ggsave("/home/wykres4.jpg", plot = wykres4)
wykres5 <- ggplot(iris, aes(x = Sepal.Width, y = Petal.Width, color = Species)) + geom_point()
ggsave("/home/wykres5.jpg", plot = wykres5)