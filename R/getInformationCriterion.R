#Returns all AIC/BIC/R^2 adjusted based on a list of models and a dataframe
getInfo <- function(ModelList, df){
  for(i in 1:length(ModelList)){
    p <- length(ModelList[[i]]$coefficients) 
    n <- nrow(df)
    cat("Model", i, "\n")
    cat("RSquared Adjusted is", summary(ModelList[[i]])$adj.r.squared, "\n")
    cat("AIC is", extractAIC(ModelList[[i]])[2], "\n")
    cat("AICc is", extractAIC(ModelList[[i]])[2] + 2*(p+2)*(p+3)/(n-p-1), "\n")
    cat("BIC is", extractAIC(ModelList[[i]][2], k= log(length(Y))), "\n\n")
  }
}
