library(tidyverse)

conflicts <- read.csv('Asia_Africa_2000.csv', stringsAsFactors = F)
conflicts2 <- read.csv('2000.csv', stringsAsFactors = T)
conflicts2 <- ordered(conflicts2,
                      levels = c("Africa", "Americas", "Asia", "Europe", "Middle East"))
                      #labels = c("AF", "AM", "A", "EU", "ME"))
conflicts3 <- read.csv('World_Year.csv', stringsAsFactors = F)
glimpse(conflicts)
conflicts

#This shows the count without separating into 3 types of conflict
ggplot()+
  geom_bar(data = conflicts, aes(x=region))

#graph that shows the different types of conflicts the 2 continents
ggplot()+
  geom_bar(data = conflicts, aes(x=region, color = 'red')) +
  facet_grid(~type_of_violence)+
  ggtitle('Type of Conflicts in Africa and Asia in 2000') +
  xlab('Continent') +
  ylab('Number of Incidents')

#graph that shows conflicts of all continents in all years, faceted by conflict type
ggplot()+
  geom_bar(data = conflicts2, aes(x=region, color = 'red')) +
  facet_grid(~type_of_violence)+
  ggtitle('Type of Conflicts in the world from 1989 to 2015') +
  xlab('Continent') +
  ylab('Number of Incidents') +
  theme(legend.position = "none") +
  scale_x_discrete(
    labels = c("AF", "AM", "A", "EU", "ME")
)

#creating a line graph that separates by region, showing the changes in the number of conflicts over time
conflict_lines <- conflicts3 %>%
    group_by(year, region) %>%
    summarise(n_conflicts = n())

ggplot()+
  geom_line(data = conflict_lines, aes(x=year, y = n_conflicts, group = region, color = region)) +
  ggtitle('Number of conflicts around the world by year by continent') +
  xlab('Year')+
  ylab('Number of Incidents')
