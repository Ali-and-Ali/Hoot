import requests
import boto3
import json
import csv
import datetime
from re import sub
from decimal import Decimal
from bs4 import BeautifulSoup

def scrape(event, context):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket='frootyloops-static', Key='products.csv')
    file = obj['Body'].read().decode('UTF-8').split()
    file_Preparer(file)

def scrape_personal(url):
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    price = content.select('.price')[1].get_text()
    return price

def scrape_foreign(url):
    page = requests.get(url)
    content = BeautifulSoup(page.content, 'html.parser')
    price = content.select('.price-new')[0].get_text()
    return price

def file_Preparer(file):
    compiled = []
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        personal_price = scrape_personal(row[1])
        foreign_price = scrape_foreign(row[2])
        compiled.append([row[0], personal_price, foreign_price])
    file_Writer(compiled)

def file_Writer(compiled):
    s3 = boto3.client('s3')
    date = datetime.datetime.now()
    key = "Report_" + date.strftime("%Y-%m-%d") + ".csv"
    file = '/tmp/' + key
    
    with open(file, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Product Number', 'Our Price', 'Competitor Price', 'Difference'])
        for row in compiled:
            row.append("$" + str(Decimal(sub(r'[^\d.]', '', row[1])) - Decimal(sub(r'[^\d.]', '', row[2]))))
            csv_writer.writerow(row)
    
    s3.upload_file(file, 'frootyloops-static', key, ExtraArgs={'ACL':'public-read'})
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:867184866553:Scraper',
        Subject='Price Report for ' + date.strftime("%Y-%m-%d"),
        Message="Link to report: https://s3.us-east-2.amazonaws.com/frootyloops-static/" + key
    )
