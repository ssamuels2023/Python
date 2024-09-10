#!/usr/bin/env python
# coding: utf-8

# In[245]:


#create 1 dictionary for every movie
#movies as dictionaries
m1 = {'Genre':'Comedy', 'Title':'Shrek', 'Director':'Vicky Jensen', 'Investment':'60,000,000', 'Revenue':'267,665,011', 'Duration':'1:30'}
m2 = {'Genre':'Musical', 'Title':'Nighmare Before C...', 'Director':'Henry Selick', 'Investment':'24,000,000', 'Revenue':'91,000,000', 'Duration':'1:16'}
m3 = {'Genre':'Comedy-Drama', 'Title':'Ratatouille', 'Director':'Brad Bird', 'Investment':'150,000,000', 'Revenue':'263,700,000', 'Duration':'1:51'}
m4 = {'Genre':'Animation', 'Title':'Madagascar', 'Director':'Tom McGrath', 'Investment':'75,000,000', 'Revenue':'532,000,000', 'Duration':'1:26'}
m5 = {'Genre':'Fantasy', 'Title':'Spirited Away', 'Director':'Hayao Miyazaki', 'Investment':'19,200,000', 'Revenue':'395,580,000', 'Duration':'2:05'}

#create a list with all movies, playlist of movies
#mark favorite movie with a string
Movies = [m1, m2, m3, m4, m5]
FavoriteMovie = 'Shrek'

#print header
print('my favorite movies'.upper())
print("-"*115)
print(f"{'Genre':<20} {'Title':<20} {'Director':<20} {'Investment':<20} {'Revenue':<20} {'Duration':<20}")
print("-"*115)

#flag favorite song using if, else statement
for movie in Movies:
    if (movie['Title'] == FavoriteMovie):
        movie['Title'] = '**' + movie['Title'] + '**'
    else: 
        movie['Title'] = movie['Title']

#print movies in the list
for movie in Movies:
    print(f"{movie['Genre']:<20} {(flag+movie['Title']+flag):<20} {movie['Director']:<20} ${movie['Investment']:<20} ${movie['Revenue']:<20} {movie['Duration']:<20}")        
TotalMinutes = TotalMinutes + hours*60 + minutes
        
#compute total duration 
TotalMinutes = 0
for movie in Movies:
    duration = movie['Duration']
    hours = int(movie['Duration'].split(':')[0])
    minutes = int(movie['Duration'].split(':')[1])
    TotalMinutes = TotalMinutes + hours*60 + minutes
    
TotalHours = int(TotalMinutes/60)
FractionMinutes = int((TotalMinutes/60 - TotalHours)*60)

#print final report of total duration
print("-"*115)
print(f"The total play time duration is: {TotalHours} hours and {FractionMinutes} minutes")
print("-"*115)

#compute average duration
AveDuration = TotalMinutes/5
AveHours = int(AveDuration/60)
AveMinutes = int(AveDuration%60)

#print final report of average duration
print(f"The average play time duration is: {AveHours} hours and {AveMinutes} minutes")
print("-"*115)

#compute total investment 
TotalInvestment = 0
for movie in Movies:
    Investment = int(movie['Investment'].replace(',', ''))
    TotalInvestment = TotalInvestment + Investment

#print final report of the total investment
print(f"The total investment amount is: ${TotalInvestment:,d}")
print("-"*115)

#compute total revenue
TotalRevenue = 0
for movie in Movies:
    Revenue = int(movie['Revenue'].replace(',', ''))
    TotalRevenue = TotalRevenue + Revenue
    
#print final report of the total revenue
print(f"The total revenue amount is: ${TotalRevenue:,d}")
print('-'*115)

#calculate average ROI
AverageROI = 0
for movie in Movies:
    ROI = ((TotalRevenue - TotalInvestment)/TotalInvestment)
    AverageROI = ROI/5

#print final report of the average ROI
print(f"The average return on investment amount is: ${AverageROI:.0%}")
print("-"*115)

