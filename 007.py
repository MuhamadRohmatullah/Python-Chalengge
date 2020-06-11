import json
import datetime
import locale
def problem_1(data, month):
    for i in data:
        created_at = i['created_at']
        date_time_object = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S")
        month = date_time_object.month
        if month == month:
            id = i["order_id"]
            customer = i["customer"]
            items = i["items"]            
            print("{Order id : %s Customer : %s and Items : %s}\n" % (id,customer,items))

def problem_2(data, userName):
    price = 0
    for i in data:
        name = i["customer"]["name"]
        items = i["items"]
        if name == userName:
            for x in items:
                count = x['price']
                price += count
    print("Total ", price)
def problem_3(data,min=300000):
    sub_total = 0
    for i in data:
        items = i['items']
        for x in items:
            count = x['price']
            sub_total += count
        if sub_total <= min:
            print("Customer", i['customer']['name'], "Total", sub_total)
data = [
    {
        "order_id": "SO-921",
        "created_at": "2018-02-17T03:24:12",
        "customer": { "id": 33, "name": "Ari" },
        "items": [
        { "id": 24, "name": "Sapu Lidi", "qty": 2, "price": 13200 }, 
        { "id": 73, "name": "Sprei 160x200 polos", "qty": 1, "price": 149000 }
        ]
    },
    {
        "order_id": "SO-922",
        "created_at": "2018-02-20T13:10:32",
        "customer": { "id": 40, "name": "Ririn" },
        "items": [
        { "id": 83, "name": "Rice Cooker", "qty": 1, "price": 258000 },
        { "id": 24, "name": "Sapu Lidi", "qty": 1, "price": 13200 }, 
        { "id": 30, "name": "Teflon", "qty": 1, "price": 190000 }
        ]
    },
    {
        "order_id": "SO-923",
        "created_at": "2018-02-28T15:20:43",
        "customer": { "id": 33, "name": "Ari" },
        "items": [
        { "id": 303, "name": "Pematik Api", "qty": 1, "price": 12000 }, 
        { "id": 49, "name": "Panci", "qty": 2, "price": 70000 }
        ]
    },
    {
        "order_id": "SO-924",
        "created_at": "2018-03-02T14:30:54",
        "customer": { "id": 40, "name": "Ririn" },
        "items": [
        { "id": 986, "name": "TV LCD 40 inch", "qty": 1, "price": 6000000 }
        ]
    },
    {
        "order_id": "SO-925",
        "created_at": "2018-03-03T14:52:22",
        "customer": { "id": 33, "name": "Ari" },
        "items": [
        { "id": 1033, "name": "Nintendo Switch", "qty": 1, "price": 4990000 }, 
        { "id": 2003, "name": "Macbook Air 11 inch 128 GB", "qty": 1, "price": 12000000 },
        { "id": 23, "name": "Pocari Sweat 600ML", "qty": 5, "price": 7000 }
        ]
    },
    {
        "order_id": "SO-926",
        "created_at": "2018-03-05T16:23:20",
        "customer": { "id": 58, "name": "Annis" },
        "items": [
        { "id": 24, "name": "Sapu Lidi", "qty": 3, "price": 13200 }
        ]
    }
]
problem_1(data,2)
problem_2(data, 'Ari')
problem_3(data)