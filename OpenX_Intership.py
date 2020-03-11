import urllib.request, json, requests
from math import sqrt
import numpy as np


def check_url_exists(url):
    r = requests.get(url)
    if r.status_code == 200:
        return True
    elif r.status_code == 404:
        return False

def url_not_empty(url):
    r = requests.get(url)
    if r.content:
        return True
    else:
        return False


def read_data(url):
    read_data = urllib.request.urlopen(url).read()
    return json.loads(read_data)

#1
def data(users,posts):
    data = [dict() for number in range(len(posts))]

    for i in range (0,len(posts)):
        for x,y in posts[i].items():
            data[i][x]=y
        for j in range (0,len(users)):
            if data[i]["userId"]==users[j]["id"]:
                for x,y in users[j].items():
                    data[i][x]=y
                    data[i]["id"]=posts[i]["id"]

    return data


#2
def number_of_posts(users,posts):
    postsnumber=[]
    for i in range (0,len(users)):
        x=0
        for j in range (0,len(posts)):
            if users[i]["id"]==posts[j]["userId"]:
                x+=1
        postsnumber.append(str(users[i]["username"])+' napisal(a) '+str(x)+ ' postow')
        
    return postsnumber


#3
def unique_posts(posts):
    ununique_post=[]
    number_of_unique_posts=0
    for i in range (0,len(posts)):
        x=posts[i]["title"]
        a=0
        for j in range (0,len(posts)):
            if j==i:
                continue
            if x==posts[j]["title"]:
                a+=1
        if a==0:
            number_of_unique_posts+=1
        else:
            ununique_post.append(x)
        
    return [list(set(ununique_post)), number_of_unique_posts]

   
#4
def users_distance(users):
    users_dist=[]
    for i in range (0,len(users)):
        dist=[]
        x=0
        for j in range (0,len(users)):
            if j==i:
                continue
            distance=sqrt((float(users[i]["address"]["geo"]["lat"])-float(users[j]["address"]["geo"]["lat"]))**2+(float(users[i]["address"]["geo"]["lng"])-float(users[j]["address"]["geo"]["lng"]))**2)
            dist.append(distance)
        index_min = np.argmin(dist)
        if index_min>=i:
            x=index_min+1
        else:
            x=index_min    
           
        users_dist.append("Najblizej "+str(users[i]["name"])+" ----> "+str(users[x]["name"])+"  ("+str(dist[index_min])+")")
    return users_dist


##################################################################


users_url = "https://jsonplaceholder.typicode.com/users"
posts_url = "https://jsonplaceholder.typicode.com/posts"


if check_url_exists(users_url)==True and url_not_empty(users_url)==True:
    userslist=read_data(users_url)
else:
    print("Bledne dane")

if check_url_exists(users_url)==True and url_not_empty(posts_url)==True:
    postslist=read_data(posts_url)
else:
    print("Bledne dane")
        
print("\n",data(userslist,postslist)[34])
print("\n\nIle postow napisali uzytkownicy:")
for x in number_of_posts(userslist,postslist):
    print(x)
print("\n\nLiczba unikalnych tytulow: ",unique_posts(postslist)[1])
print("\nLista tytulow ktore nie sa unikalne: \n",unique_posts(postslist)[0])
print("\n\nUzytkownicy mieszkajacy najblizej siebie:")
for x in users_distance(userslist):
    print(x)
