
#6 Store the contents of the titanic.csv data in a variable in R then print the summary tabe of that table 

R = read.csv(file="titanic.csv", head=TRUE, sep=",")
print(R)
summary(R)

#7 print out the names of the columns in the titanic.csv file. Then print out the values for the first two columns in the dataset. Finally create a table that outlines the distribution of genders in the dataset 
names(R)
R$"PassengerId"
R$"Survived"

sex_table = table(R$"Sex")
print(sex_table)

#8 compute the proportion of men and women who survived. Then, compute the probability that if someone was a women, they would survive the crash and the probability that if someone was a man, they would survive the crash 
prop.table(sex_table)
sex_survive_prop = prop.table(table(R$"Sex", R$"Survived"))

#9 we want to test whether the old naval cliche of "women and children first" impacted survival. Assume that a child is anyone under the age of 18. Use the titanic dataset to answer this question by computing the average number of survivors for men and women and for children and adults. 

R$"Child"<-0
R$"Child"[R$"Age"<18]<-1
aggregate(R, by= list(R$"Sex", R$"Survived"), FUN="mean")
aggregate(R, by= list(R$"Child", R$"Survived"), FUN="mean")




