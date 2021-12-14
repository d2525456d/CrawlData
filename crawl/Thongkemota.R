#set v??? thu m???c làm vi???c
setwd("C:\\Users\\Admin\\PycharmProjects\\crawl")
#D???c file csv du???c luu v??? sau khi ch???nh s???a ??? python
df = read.csv(file = 'Bangxephang.csv',header = TRUE)
#Xem data
View(df)
#THêm vào các thu vi???n
library(tidyverse)
library(dplyr)
library(psych)
library(ggplot2)
library(fBasics)
#Xóa c???t index
df = df[,-1]
#Tính các giá tr??? th???ng kê miêu t???
describe(df)

summary(df)

basicStats(df[,-1])

#V??? hi???u d???
#plot1
ggplot(df,aes(x = Team,y = Point))+
  geom_bar(stat="identity", width=0.5, color="blue",fill = "#FF6666")+
  ggtitle("Point of all team in 2020/2021")+
  xlab("CLB")+ylab("Point")+
  theme(text = element_text(size = 10),
        axis.text.x = element_text(angle=45, hjust=1))


#plot2
ggplot(df,aes(x = Team,y = xPoint))+
  geom_bar(stat="identity", width=0.5, color="red",fill = "#98EBDD")+
  ggtitle("Expected Point of all team in 2020/2021")+
  xlab("CLB")+ylab("Expected Goal Against")+
  theme(text = element_text(size = 10),
        axis.text.x = element_text(angle=45, hjust=1))


#plot3 
ggplot(df,aes(x = G, y = GA,fill = Team))+
  geom_point(size = 3,aes(col = Team))+
  theme(legend.position = "bottom")+
  xlab("Goal")+ylab("Goal Against")+
  ggtitle('t???ng quan t???ng s??? bàn th???ng và bàn thua c???a các clb mùa gi???i 2020/2021')


#plot4
ggplot(df,aes(x = xG, y = xGA,fill = Team))+
  geom_point(size = 3,aes(col = Team))+
  theme(legend.position = "bottom")+
  xlab("Expected")+ylab("Expected Goal Against")+
  ggtitle('t???ng quan t???ng s??? bàn th???ng k??? v???ng và bàn thua k??? v???ng c???a các clb mùa gi???i 2020/2021')


#plot5
ggplot(df,aes(x = Team,y = G.xG))+
  geom_bar(stat="identity", width=0.5, color="blue",fill = "#4C5AD4")+
  xlab("CLB")+ylab("Goal - Expected Goal")+
  ggtitle("Chênh l???ch bàn th???ng và bàn th???ng k??? v???ng c???a các clb mùa gi???i 2020/2021")+
  theme(text = element_text(size=10),
        axis.text.x = element_text(angle=45, hjust=1))


#plot6
ggplot(df,aes(x = Team,y = GA.xGA))+
  geom_bar(stat="identity", width=0.5, color="#20FA34",fill = "#F7E60C")+
  xlab("CLB")+ylab("Goal Against - Expected Goal Against")+
  ggtitle("Chênh l???ch bàn thua và bàn thua k??? v???ng c???a các clb mùa gi???i 2020/2021")+
  theme(text = element_text(size=10),
        axis.text.x = element_text(angle=45, hjust=1))


#plot7
ggplot(df,aes(x = Team,y = Point.xPoint))+
  geom_bar(stat="identity", width=0.5, color="#FFB0DE",fill = "#F78219")+
  xlab("CLB")+ylab("Point - Expected Point")+
  ggtitle("Chênh l???ch Di???m và Di???m k??? v???ng c???a các clb mùa gi???i 2020/2021")+
  theme(text = element_text(size=10),
        axis.text.x = element_text(angle=45, hjust=))


#plot8
ggplot(df,aes(x = GD, y = xGD,fill = Team))+
  xlab("Goal Difference")+ylab("Expected Goal Difference")+
  geom_point(size = 3,aes(col = Team))+
  theme(legend.position = "bottom")+
  ggtitle('t???ng quan Hi???u s??? k??? v???ng và hi???u s??? k??? v???ng c???a các clb')
