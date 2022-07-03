import csv

from class_items import *

def import_itemsList():
    itemsList = [] 
    with open('itemsList.csv', newline='') as csvfile:
        itemsList_csv = csv.reader(csvfile, delimiter=',') 
        row_count = 0 
        for row in itemsList_csv:
            itemsList.append([str(row_count)]) 
            for i in row:
                itemsList[row_count].append(i) 
            row_count += 1 
    return itemsList 

def objectify_itemsList(itemsList):
    itemsListObj = [] 
    for row in itemsList:
        itemsListObj.append(ItemsList(row[0], row[1], row[2], row[3], row[4], row[5], row[6])) 
    return itemsListObj 

itemsList = import_itemsList() 
itemsListObj = objectify_itemsList(itemsList) 