from pyquery import PyQuery
url='https://www.mlb.com/stats'
mlb = PyQuery(url)
search = 'div.top-wrapper-1NLTqKbE'
name_list = mlb(search).text().split()
print(name_list)

t_search = 'span.short-3OJ0bTju'
name_l = mlb(t_search).text().split()
print(name_l)

team = 'td[scope="row"][data-col="1"]'
team_list = mlb(team).text().split()
print(team_list)