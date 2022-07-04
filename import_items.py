import csv

from class_items import Item

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

def objectify_itemsList(itemsListCsv):
    itemsList = [] 
    for row in itemsListCsv:
        itemsList.append(Item(row[0], row[1], row[2], row[3], row[4], row[5], row[6])) 
    return itemsList

itemsListCsv = import_itemsList() 
itemsList = objectify_itemsList(itemsListCsv)