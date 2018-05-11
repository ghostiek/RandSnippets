#This function gets all the linear models from the regsubsets method from the leaps package
#Mostly gotten from https://stackoverflow.com/questions/41000835/get-all-models-from-leaps-regsubsets

#install.packages("leaps")
library(leaps)

#Parameter regsubs takes in the object returned from the leaps::resubsets() method
#Parameter responseName takes in a string, the name of the response variable of your Linear Model inputed in your regsubsets method
#Parameter dataset is the dataframe of the dataset 
getAllModels <- function(regsubs, responseName, dataset){
  X <- summary(regsubs)$which
  
  xvars <- dimnames(X)[[2]][-1]  ## column names (all covariates except intercept)
  responsevar <- responseName  ## name of response
  
  lst <- vector("list", dim(X)[1])  ## set up an empty model list
  
  ## loop through all rows / model specifications
  for (i in 1:dim(X)[1]) {
    id <- X[i, ]
    form <- reformulate(xvars[which(id[-1])], responsevar, id[1])
    lst[[i]] <- lm(form, dataset)
  }
  
  return(lst)
}
