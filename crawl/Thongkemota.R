#set về thư mục làm việc
setwd("C:\\Users\\Admin\\PycharmProjects\\crawl")
#ĐỌc file csv được lưu về sau khi chỉnh sửa ở python
df = read.csv(file = 'Bangxephang.csv',header = TRUE)
#Xem data
View(df)
#THêm vào các thư viện
library(tidyverse)
library(dplyr)
library(psych)
library(ggplot2)
library(fBasics)
#Xóa cột index
df = df[,-1]
#Tính các giá trị thống kê miêu tả
describe(df)

summary(df)

basicStats(df[,-1])

#Vẽ hiểu đồ
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
  ggtitle('tổng quan tổng số bàn thắng và bàn thua của các clb mùa giải 2020/2021')


#plot4
ggplot(df,aes(x = xG, y = xGA,fill = Team))+
  geom_point(size = 3,aes(col = Team))+
  theme(legend.position = "bottom")+
  xlab("Expected Goal")+ylab("Expected Goal Against")+
  ggtitle('tổng quan tổng số bàn thắng kỳ vọng và bàn thua kỳ vọng của các clb mùa giải 2020/2021')


#plot5
ggplot(df,aes(x = Team,y = G.xG))+
  geom_bar(stat="identity", width=0.5, color="blue",fill = "#4C5AD4")+
  xlab("CLB")+ylab("Goal - Expected Goal")+
  ggtitle("Chênh lệch bàn thắng và bàn thắng kỳ vọng của các clb mùa giải 2020/2021")+
  theme(text = element_text(size=10),
        axis.text.x = element_text(angle=45, hjust=1))


#plot6
ggplot(df,aes(x = Team,y = GA.xGA))+
  geom_bar(stat="identity", width=0.5, color="#20FA34",fill = "#F7E60C")+
  xlab("CLB")+ylab("Goal Against - Expected Goal Against")+
  ggtitle("Chênh lệch bàn thua và bàn thua kỳ vọng của các clb mùa giải 2020/2021")+
  theme(text = element_text(size=10),
        axis.text.x = element_text(angle=45, hjust=1))


#plot7
ggplot(df,aes(x = Team,y = Point.xPoint))+
  geom_bar(stat="identity", width=0.5, color="#FFB0DE",fill = "#F78219")+
  xlab("CLB")+ylab("Point - Expected Point")+
  ggtitle("Chênh lệch Điểm và Điểm kỳ vọng của các clb mùa giải 2020/2021")+
  theme(text = element_text(size=10),
        axis.text.x = element_text(angle=45, hjust=))


#plot8
ggplot(df,aes(x = GD, y = xGD,fill = Team))+
  xlab("Goal Difference")+ylab("Expected Goal Difference")+
  geom_point(size = 3,aes(col = Team))+
  theme(legend.position = "bottom")+
  ggtitle('tổng quan Hiệu số kỳ vọng và hiệu số kỳ vọng của các clb')
