DATA_DIR <- "../DSAI Parma 20190409/netflix prize"

library(tidyverse)
library(readtext)

setwd(DATA_DIR)

movie_titles <- read.csv(paste0(DATA_DIR, "/movie_titles.txt"), header=FALSE)
names(movie_titles) <- c('id', 'year', 'title')



# da 0 a 9999
files <- readtext(paste0(DATA_DIR, "/training_set/mv_00000*"))

first_movie <- files$text[1]
object.size(files)
movie <- gsub("^([0-9]*):\n(.*)","\\1",first_movie)
user_rating_date <- gsub("^([0-9]*):\n(.*)","\\2",first_movie)
array_triplette <- strsplit(gsub("^([0-9]*):\n(.*)","\\2",first_movie), "\n")
matrix_user_rating_date <- matrix(unlist(lapply(array_triplette, strsplit, ",")[[1]]), ncol=3, byrow = TRUE)
df <- as.data.frame(matrix_user_rating_date)
names(df) <- c('user', 'rating', 'date')

df_complete <- df %>% mutate(movie) %>% select(movie, user, rating, date)
df_complete <- data.frame('','','','')
names(df_complete) <- c('movie', 'user', 'rating', 'date')

object.size(df_cosmplete)
head(df_complete)

from_text_to_df <- function(first_movie){
  movie <- gsub("^([0-9]*):\n(.*)","\\1",first_movie)
  user_rating_date <- gsub("^([0-9]*):\n(.*)","\\2",first_movie)
  array_triplette <- strsplit(gsub("^([0-9]*):\n(.*)","\\2",first_movie), "\n")
  matrix_user_rating_date <- matrix(unlist(lapply(array_triplette, strsplit, ",")[[1]]), ncol=3, byrow = TRUE)
  df <- as.data.frame(matrix_user_rating_date)
  names(df) <- c('user', 'rating', 'date')
  df_complete <- df %>% mutate(movie) %>% select(movie, user, rating, date)
  return(df_complete)
}


df_list <- lapply(files$text, from_text_to_df )

df_tot <- do.call("rbind", df_list )

df_tot %>% group_by(user) %>% summarise(n = n()) %>% arrange(-n) %>% head()

#df_tot[1:1000,] %>% spread(user, rating) %>% head()


#df_tot[1:1000,] %>% spread(user, rating) %>% head()

# da 0 a 9999
#files <- readtext(paste0(DATA_DIR, "/training_set/mv_000[1-9]*"))

# da 10000 a 17000
#a <- readtext(paste0(DATA_DIR, "/training_set/mv_001*"))