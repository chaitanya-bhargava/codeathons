from collections import namedtuple

c,p=map(int,input().split())
namelist=[]
projectlist=[]
for i in range(c):
  name,n=input().split()
  n=eval(n)
  nametuple=namedtuple('Names','name skillno skilltuple')
  for j in range(n):
    skill,l=input().split()
    l=eval(l)
    skilltuple=namedtuple('Skill','name level')
    s1=skilltuple(name=skill,level=l)
    n1=nametuple(name,j,s1)
    namelist.append(n1)
print(namelist)
for z in range(p):
  project,d,s,b,r=input().split()
  d=eval(d)
  s=eval(s)
  b=eval(b)
  r=eval(r)
  projects=namedtuple('Projects','project skillno skilltuple')
  for y in range(r):
    x,lk=input().split()
    lk=eval(lk)
    skilltuple2=namedtuple('Skill','name level')
    s2=skilltuple2(name=x,level=lk)
    n2=projects(project,y,s2)
    projectlist.append(n2)
print(projectlist)