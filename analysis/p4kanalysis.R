library(tidyverse)
p4k <- read.csv("C:/Users/Evan/Documents/scrapeFork/p4kreviews.csv")
glimpse(p4k)
#by genre
p4k %>% group_by(genre) %>% summarise(n=n(), avg_score = mean(score), std.dev = sd(score), best = mean(best)) %>% arrange(desc(n))
#histogram by genre
hist <- p4k %>% ggplot(aes(x=score)) + geom_histogram(bins=50) + geom_vline(xintercept=mean(p4k$score)) + theme_bw() + scale_x_continuous(breaks = c(1:10)) + labs(x = "Score",y="Count")
#rounded barplot
p4k %>% mutate(roundScore = floor(score)) %>% filter(genre %in% c("Rock","Electronic","Jazz")) %>% ggplot(aes(x=roundScore, fill = genre)) + geom_bar(position="dodge") + scale_x_continuous(limits = c(3, 10))
#popular artist - sorted by number
p4k %>% group_by(artist) %>% mutate(n=n()) %>% filter(n >= 5) %>% summarise(n=n(), avg_score = mean(score), std.dev = sd(score), best = mean(best)) %>% arrange(desc(n))
#popular artist - sorted by rating
bar2 <- p4k %>% group_by(artist) %>% mutate(n=n()) %>% filter(n >= 5) %>% summarise(n=n(), avg_score = mean(score), std.dev = sd(score), best = mean(best)) %>% arrange(desc(avg_score)) %>% filter(avg_score > 8.5) %>% ggplot(aes(x = reorder(artist, desc(avg_score)), y = avg_score, fill = best)) + geom_bar(stat="identity") + coord_cartesian(ylim=c(8.5,9.5)) + labs(x = "Artist (>5 reviews)",y="Average Score") + guides(fill = guide_colorbar(title = "% Best")) + theme(axis.text.x = element_text(angle = 55, hjust = 1))
#by high score and >2 releases reviewed
p4k %>% group_by(artist) %>% filter(n() >= 2) %>% summarise(n=n(), avg = mean(score), best = sum(best)) %>% arrange(desc(avg))
#by genre
bar <- p4k %>% group_by(genre) %>% mutate(n = n(), b = mean(best)) %>% ggplot(aes(x = reorder(genre, desc(score)), fill = b)) + geom_bar(position="dodge") + labs(x = "Genre", y = "Count") + guides(fill = guide_colorbar(title = "% Best"))
