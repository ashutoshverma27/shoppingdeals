from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from products.models import Product
from blogs.models import BlogPost
from django.utils import timezone

def base(request):
        return render(request,'base.html')

def index(request):
    pro1=Product.objects.get(pid=1)
    allpro=Product.objects.all()
    all=BlogPost.objects.get(postid=1)
    pro2=[]
    for i in allpro:
        print(i,"added")
        pro2.append(i)



    return render(request,'index.html',{'i':pro1,'pro2':pro2,'all':all})


def add(request):
    return  render(request,'add.html')
def added(request):
    url1=str(request.GET['link'])
    print(url1)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    page=requests.get(url1,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title1=soup.find('span', {'class' : 'a-size-large'}).get_text().strip()
    price1=soup.find('span', {'class' : 'a-size-medium a-color-price priceBlockBuyingPriceString'}).get_text()
    image1=soup.find('img', {'id' : 'landingImage'})['data-old-hires']   #find method only return single value
    mrp1=soup.find('span', {'class' : 'priceBlockStrikePriceString a-text-strike'}).get_text()
    saving1=soup.find('td', {'class' : 'a-span12 a-color-price a-size-base priceBlockSavingsString'}).get_text()
    label_tag=soup.find_all('td',class_= 'label')    #find_all return a list of all data with tags included
    value_tag=soup.find_all('td',class_= 'value')    #get_text method return the text inside the html tags
    ram1=soup.find('td',{'class' : 'value'}).get_text()
    specs={}
    for i,j in zip(label_tag,value_tag):
        specs[i.get_text().strip().lower()]=j.get_text()  #there is space around label tag that is why used strip method
        #used lower method to to lower all character as to avoid confusion which word will be capital and which not
    print(specs['ram'])

    product=Product()
    product.title=title1
    product.price=price1
    product.image=image1
    product.mrp=mrp1
    product.saving=saving1
    product.url=url1
    product.other_images="do something later"
    product.android=specs['os']
    product.ram=specs['ram']
    product.weight=specs['weight']
    product.battery=specs['battery power rating']+" mAh"
    product.display=specs['display technology']
    product.pub_date=timezone.datetime.now()
    product.save()

    print('saved')
    return render(request,'added.html')

def search(request):
    if request.method=="GET":
        s=request.GET['search']
        print(s)
        allpro=Product.objects.all()
        allpost=BlogPost.objects.all()
        pro=[]
        posts=[]
        if allpro:
            for pros in allpro:
                if s.lower() in pros.title.lower():
                    pro.append(pros)
        if allpost:
            for post in allpost:
                if s.lower() in post.title.lower():
                    posts.append(post)

        return render(request,'search.html',{'pro':pro,'posts':posts})

def random(request):
    pro=Product.objects.get(pid=1)
    new=pro.other_images.split('\'')
    imagess=[]
    for i in new:
        if i.startswith('https'):
             imagess.append(i)
    return render(request,'random.html',{'pro':pro,'imagess':imagess})
