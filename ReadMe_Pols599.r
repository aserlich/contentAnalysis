library(ReadMe)

#read in csvs
#this file has the text and all ofthe truth and training information
bills <- read.csv('/Volumes/Optibay-1TB/Dropbox/Content_Wilker/LatexSlides/4_readMe/ReadmeforAaron.csv',
	stringsAsFactors=FALSE, header=FALSE)

########IF YOU WANT README TO DO THE PREPOCESSING, DO THIS
###NOT RECOMMENDED BUT USED IN THE EXAMPLE
#create a new directory
# dir.create(file.path('/Volumes/Optibay-1TB/Dropbox/Content_Wilker/LatexSlides/4_readMe',
# 	'billTexts'), showWarnings = FALSE)
# 
# #set the working director
# setwd(file.path('/Volumes/Optibay-1TB/Dropbox/Content_Wilker/LatexSlides/4_readMe',
# 		'billTexts'))
# 
# #write out the files one per text document
# for(i in 1:nrow(bills))	{
# 	write(bills[i,1], file = paste(i, "bill.txt", sep=""))
# 	print(paste("bill", i))
# }


######CREATE CONTROL FILE
bills <- bills[, 2:5]#Remove actual text 
bills$ROWID <- paste(seq(1:nrow(bills)), "bill.txt", sep="")
names(bills)[1] <- "TRUTH" #cannot be missing when training set is 1, can be missing if you don't know
names(bills)[2] <- "TRAININGSET" # 1, if in the training seth
names(bills)[3] <- "SUBID" #this is the sub ID


#We will iterate with different training set sizes

setwd(file.path('/Volumes/Optibay-1TB/Dropbox/Content_Wilker/LatexSlides/4_readMe',
		'billTexts'))

set.seed(20130428)
#my matrix of results
simulations <- matrix(data=rnorm(200*20), ncol =length(mySequence), 200)

for(i in mySequence){
	bills$TRAININGSET <- 0 # make nothing in the training set
	#readMe is very particular about the control file
	#you cannot have quotation marks or row.names
	#create the control file with the varying training set size
	billsforReadMe <- bills[sample(nrow(bills), 50000),c("ROWID","TRUTH","TRAININGSET")]
	billsforReadMe$TRAININGSET[sample(nrow(billsforReadMe), i)] <- 1 #sample i bills
	print(sum(billsforReadMe$TRAININGSET))
	write.csv(billsforReadMe, file="control.txt", quote=FALSE,row.names=FALSE) #create
	print(paste("Working on the sample size of", i))
	#PREPROCESS SAMPLE OF BILLS
	#table file is the the tdf
	#threshold - words occurrring in x percent of texts
	billsUG <- undergrad(control ="control.txt", stem=TRUE,strip.tags=TRUE,ignore.case=TRUE,
		table.file="tablefile.txt",threshold=0.01, python3=FALSE,
		pyexe=NULL, sep=",",printit=TRUE)
	billsUG_P <- preprocess(billsUG) #remove invariant columns
	#Run ReadMe
	billsResults <- readme(billsUG_P)
	#Put the estimates in our matrix of simulations
	simulations[ , (i/mySequence[1])] <- billsResults$est.CSMF
}

simulations <- t(simulations)
simulations <- as.data.frame(simulations)
names(simulations)<- paste("Category", seq(1,20))
simulations$cat <- seq(200, 2000, 200)

TRUTH <- billsResults$true.CSMF

# write.csv(simulations, "simulationsv1.csv")
# write.csv(TRUTH, "truth1.csv")

true <- as.data.frame(TRUTH)
names(true) <- "true"
true$cat <- paste("Category", seq(1,20))

library(ggplot2)
library(reshape2)
d <- melt(simulations, id.vars="cat")

# Everything on the same plot
pdf(file="readmesims.pdf")
ggplot(d, aes(cat,value, col=variable)) + 
  geom_point() + 
  geom_line() +
  geom_hline(data = true, aes(yintercept = true, col = cat), linetype='dashed')
dev.off()

pdf(file="readmesims2.pdf")
 ggplot(d, aes(cat,value)) + 
  geom_point() +
  facet_wrap(~variable)
dev.off()

sims1 <- read.csv("simulationsv1.csv", header=TRUE)
truth1 <- read.csv("truth1.csv", header=TRUE)
topics <- read.csv(file.path("/Volumes/Optibay-1TB/Dropbox/Content_Wilker/LatexSlides/4_readMe", "majtopics.csv"), header=TRUE, stringsAsFactors=FALSE)

sims1 <- sims1[, 2:ncol(sims1)]
sims2 <- apply(sims1, 2, function(x) abs(x-truth1$x))

sims2 <- t(sims2)
sims2 <- as.data.frame(sims2)
names(sims2)[1:8]<- topics$topic[1:8]
names(sims2)[10:20]<- topics$topic[9:19]
sims2$cat <- seq(200, 2000, 200)

test250 <- sims1[,1]
test500<- sims1[,2]

pdf(file="/Volumes/Optibay-1TB/Dropbox/Content_Wilker/LatexSlides/4_readMe/truevest1.pdf", width =8, height =4)
par(mfrow=c(1,2))
plot(	truth1$x, test250,xlim = seq(0,.1,.1), ylim = seq(0,.1,.1), ylab='estimate proportions - 250 training set', xlab = "true proportions")
abline(a=0, b=1)
#abline(a=0.025, b=1, col="red", lty =2)
#abline(a=-0.025, b=1, col="red", lty =2)

plot(	truth1$x, test500,xlim = seq(0,.1,.1), ylim = seq(0,.1,.1), ylab='estimated proportions - 500 training set', xlab = "true proportions")
abline(a=0, b=1)
#abline(a=0.025, b=1, col="red", lty =2)
#abline(a=-0.025, b=1, col="red", lty =2)
dev.off()

d2 <- melt(sims2, id.vars="cat")

pdf(file="/Volumes/Optibay-1TB/Dropbox/Content_Wilker/LatexSlides/4_readMe/readmesims2.pdf")
ggplot(d2, aes(cat,value)) + 
ggtitle("ReadMe rate of misprediction by category")+
 geom_point() +
 geom_smooth(method = "lm") +
 ylab("Misprediction") +
 xlab("Size of training set") +
 facet_wrap(~variable)
dev.off()

sum(bills2$TRAININGSET)

nrow(bills2) - sum(bills2$TRAININGSET)

#undergrad is also particular. You need the proper separators here. 
#control.txt is the default name for you file with your bill names

#we can see the term document matrix has been automatically created. 
billsUG$testset[1:10, 1:10]

billsResults <- readme(billsUG_P)

billsResults$est.CSMF
billsResults$true.CSMF

billsResults$est.CSMF-billsResults$true.CSMF

rmvfiles <- list.files(path = "/Volumes/Optibay-1TB/Dropbox/Content_Wilker/Content_Analysis/Code", pattern = '[1-9].*bill.*txt', all.files = FALSE)
#file.remove(rmvfiles)

