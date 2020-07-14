from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class TwitterBot: 
   def __init__(self, email, password):
      self.email = email
      self.password = password
      self.bot = webdriver.Firefox()

   def login(self):
      bot = self.bot
      bot.get('https://twitter.com/login')
      time.sleep(2)      
      email = bot.find_element_by_name('session[username_or_email]')
      password = bot.find_element_by_name('session[password]')     
      email.send_keys(self.email)
      password.send_keys(self.password)     
      password.send_keys(Keys.RETURN)
      time.sleep(2)

   def search(self, searchquery):
      bot = self.bot
      bot.get('https://twitter.com/search?q=' + searchquery + '&src=typed_query')   

   def advsearch(self, account, m, d, y, mend, dend, yend):
      bot = self.bot
      bot.get('https://twitter.com/search-advanced')
      time.sleep(2)
      searchbox = bot.find_element_by_name('fromTheseAccounts') 
      searchbox.send_keys(account)
      time.sleep(1)
      month = Select(bot.find_element_by_css_selector("[aria-label = 'Μήνας']"))
      month.select_by_value(m)     
      day = Select(bot.find_element_by_css_selector("[aria-label = 'Ημέρα']"))
      day.select_by_value(d)     
      year = Select(bot.find_element_by_css_selector("[aria-label = 'Έτος']"))
      year.select_by_value(y)      
      monthend = Select(bot.find_elements_by_css_selector("[aria-label = 'Μήνας']")[1])
      monthend.select_by_value(mend)      
      dayend = Select(bot.find_elements_by_css_selector("[aria-label = 'Ημέρα']")[1])
      dayend.select_by_value(dend)      
      yearend = Select(bot.find_elements_by_css_selector("[aria-label = 'Έτος']")[1])
      yearend.select_by_value(yend)     
      searchbox.send_keys(Keys.RETURN)
      time.sleep(1)
      bot.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div[2]/div[2]/a').click()


print('Hello!')
time.sleep(1)
print('Would you like to do a simple search or an advanced search?')
time.sleep(1)
flag = int(input('Please input 0 for a simple search or 1 for an advanced search: '))
mainflag = 0
while mainflag == 0:
  if flag == 0:
    searchflag = 0
    while searchflag == 0:
      print('You can choose among the following accounts or search about anything: PrimeMinisterGR...')
      time.sleep(2)
      searchquery = input('Please input your search query with no spaces: ')
      user = TwitterBot('example@mail.com', 'example')
      user.login()
      user.search(searchquery)
      print('Would you like to search for anything else or proceed to an advanced search?')
      time.sleep(1)
      searchflag = int(input('Please input 0 for another search query, 1 to execute an advanced search or any other number to quit the program: '))     
      if searchflag == 0:
        print('You can choose among the following accounts or search about anything: PrimeMinisterGR, Zourabichvili_S...')
        time.sleep(2)
        searchquery = input('Please input your search query with no spaces: ')
      elif searchflag == 1:
        flag = 1 
      else:
        mainflag = 1
  if flag == 1:
    advsearchflag = 0   
    while advsearchflag == 0:
      print('You can choose among the following accounts or search about anything: @PrimeMinisterGR, @Zourabichvili_S...')
      time.sleep(2)
      account = input('If you would like to input more than one search query, please use a space in between e.g @account1 @account2: ' )
      time.sleep(2)      
      print('In order to search for tweets in a certain time frame please input the earliest date first.')
      time.sleep(1)
      m = input('In order to choose the month, please input a number between 1-12: ') 
      d = input('In order to choose the day, please input a number between 1-31: ')
      y = input('In order to choose the year, please input a number between 2006-2020: ')
      time.sleep(1)
      print('Then, please input the latest date.')
      time.sleep(1)
      mend = input('In order to choose the month, please input a number between 1-12: ')
      dend = input('In order to choose the day, please input a number between 1-31: ')
      yend = input('In order to choose the year, please input a number between 2006-2020: ')
      user = TwitterBot('vpaklatzis@gmail.com', '0406xp')
      user.login()
      user.advsearch(account, m, d, y, mend, dend, yend)
      print('Would you like to execute another advanced search?')
      time.sleep(1)
      advsearchflag = int(input('Please input 0 for another advanced search, 1 to execute a search query or any other number to quit the program: '))     
      if advsearchflag == 0:
        print('You can choose among the following accounts or search about anything: @PrimeMinisterGR, @Zourabichvili_S...')
        time.sleep(2)
        account = input('If you would like to input more than one search query, please use a space in between e.g @account1 @account2: ')
      elif advsearchflag == 1:
        flag = 0
      else:
        mainflag = 1

#Need to login with Iliana's fake twitter account
#Need to create an array in order to output the account names

