from datetime import date
d1=date(1997,10,24)
print(d1)
t=date.today()
print(t)
age=t.year-d1.year-((t.month,t.day)<(d1.month,d1.day))
print(age)