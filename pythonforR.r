##R code for the Python examples
#Aaron Erlich
##Chapter 1
Rlist1 <- list('hello world', 'hello Seattle')
print(Rlist1)

oneCountry  <- "USA"
oneCountry_Vector <- vector(mode ="character", 1)
oneCountry_Vector[1] <- "USA"
oneCountry == oneCountry_Vector


mode(oneCountry)
mode(oneCountry_Vector)
oneCountry == oneCountry_Vector
length(oneCountry)

oneCountry[1]
oneCountry[2]

countryCodes <- c('RUS', 'AFG', 'GER') 

countryCodes <- as.list(countryCodes) #make my vector a list
subset(countryCodes, countryCodes != "AFG") #remove AFG but doesn't change underlying object
countryCodes[1:4]

#############
###Chapter 2
############

strsplit("I don't wanna go to school, but I have to, but I don't want to", "but")

twoSchoolStatements <- c("I don't wanna go to school, but I have to, but I don't want to",
						"I really wanna go to school, but I am sick, but I really don't have to")

strsplit(twoSchoolStatements, "but")

twoSchoolsStatementsList <- list("I don't wanna go to school, but I have to, but I don't want to",
								"I really wanna go to school, but I am sick, but I really don't have to")

lapply(twoSchoolsStatementsList, strsplit, "but")


#############
###Chapter 3
############
DOI <- c(1963, 1776)
pop <- c(40000000, 300000000)
subnat <- c("Kilifi, Nairobi", "WA, ME")  
countryMatrix <- matrix(c(DOI, pop, subnat), nrow=2, ncol=3, 
  	dimnames = list(c("USA", "KEN"), c("DOI", "pop", "subnat")))
print(countryMatrix)

