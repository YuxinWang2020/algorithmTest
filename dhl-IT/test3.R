library(tidyverse)

prepare_data <- function(index_data_path, finance_data_path) {
  index_data_path <- "dhl-IT/index_data.csv"
  finance_data_path <- "dhl-IT/finance_data.csv"

  # read the "./data/index_data.csv" file
  index_data <- read_csv(index_data_path)
  # read the "./data/finance_data.csv" file
  finance_data <- read_csv(finance_data_path)
  # write your solution here (remember to return the right object)

  # cleans the index_data
  # convert ProductType, Plant, ComplexityScore to factors
  index_data$ProductType <- as.factor(index_data$ProductType)
  index_data$Plant <- as.factor(index_data$Plant)
  index_data$ComplexityScore <- as.factor(index_data$ComplexityScore)
  # convert IfPhasedOut to Boolean
  index_data$IfPhasedOut <- index_data$IfPhasedOut == "x" & !is.na(index_data$IfPhasedOut)

  # cleans finance_data
  # filter out rows where Sales or CoGS is NA
  finance_data <- drop_na(finance_data, Sales, CoGS)
  # create Profitability equal to (Sales-CoGS)/Sales
  finance_data$Profitability <- (finance_data$Sales - finance_data$CoGS) / finance_data$Sales
  # extract only MaterialNumber from the MaterialNumber column
  finance_data <- separate(finance_data, MaterialNumber, into = c(NA, "MaterialNumber"), sep = " ", remove = TRUE)

  # joins index_data with finance_data by MaterialNumber
  master_data <- left_join(index_data, finance_data, by = "MaterialNumber")

  return(master_data)
}



