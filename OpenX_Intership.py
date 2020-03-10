import urllib.request, json, math
import numpy as np

url1 = "https://jsonplaceholder.typicode.com/users"
userslist = json.loads(urllib.request.urlopen(url1).read())

url2 = "https://jsonplaceholder.typicode.com/posts"
postslist = json.loads(urllib.request.urlopen(url2).read())



#1
data = [dict() for number in range(len(postslist))]

for i in range (0,len(postslist)):
    for x,y in postslist[i].items():
        data[i][x]=y
    for j in range (0,len(userslist)):
        if data[i]["userId"]==userslist[j]["id"]:
            for x,y in userslist[j].items():
                data[i][x]=y
                data[i]["id"]=postslist[i]["id"]

#2
for i in range (0,len(userslist)):
    x=0
    for j in range (0,len(postslist)):
        if userslist[i]["id"]==postslist[j]["userId"]:
            x+=1
    print(userslist[i]["username"]," napisal(a) ",x," postow")


#3
print("\n Lista tytulow ktore nie sa unikalne: \n")

for i in range (0,len(postslist)):
    x=postslist[i]["title"]
    a=0
    for j in range (0,len(postslist)):
        if x==postslist[j]["title"]:
            a+=1
    if a==0:
        print(x)

#4
print("\n Uzytkownicy mieszkajacy najblizej siebie:")

for i in range (0,len(userslist)):
    dist=[]
    x=0
    for j in range (0,len(userslist)):
        if j==i:
            continue
        distance=math.sqrt((float(userslist[i]["address"]["geo"]["lat"])-float(userslist[j]["address"]["geo"]["lat"]))**2+(float(userslist[i]["address"]["geo"]["lng"])-float(userslist[j]["address"]["geo"]["lng"]))**2)
        dist.append(distance)
    index_min = np.argmin(dist)
    if index_min>=i:
        x=index_min+1
    else:
        x=index_min    
        
   # print(i,"   ",index_min,"  ")
    print("Najblizej ",userslist[i]["name"]," ----> ",userslist[x]["name"],"  (",dist[index_min],")")
            




