from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from products.models import Product
from django.utils import timezone
from .models import Product

def compare(request):
    pro1=Product.objects.all()
    pro2=Product.objects.all()
    k=Product.objects.get(pid=1)

    return render(request,'products/compare.html',{'pro1':pro1,'pro2':pro2,'k':k})

def add(request):
    return  render(request,'products/add.html')
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
    all_other_images=soup.find('img', {'id' : 'landingImage'})['data-a-dynamic-image']
    new=all_other_images.split('\"')
    other_images=[]
    for i in new:
       if i.startswith("https"):
           other_images.append(i)
           print(i)
    specs={}
    for i,j in zip(label_tag,value_tag):
        specs[i.get_text().strip().lower()]=j.get_text()  #there is space around label tag that is why used strip method
        #used lower method to to lower all character as to avoid confusion which word will be capital and which not
    print(specs['ram'])

    product=Product()
    product.title=title1
    product.price_on_amazon=price1
    product.image=image1
    product.mrp=mrp1
    product.saving=saving1
    product.amazon_url=url1
    product.other_images=other_images
    product.android=specs['os']
    product.ram=specs['ram']
    product.weight=specs['weight']
    product.battery=specs['battery power rating']+" mAh"
    product.display=specs['display technology']
    product.pub_date=timezone.datetime.now()
    product.save()

    print('saved')
    return render(request,'products/added.html')
