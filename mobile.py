mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

list_data = mobile_data['data']

for x in list_data:
    phone_model = x.get('name')
    phone_price =x.get('price')
    phone_made = x.get('made')
    sentence = f'{phone_model} is made in {phone_made}. The price is {phone_price} USD which is almost equal to 30975 BDT'
    print(sentence)

#ভাই অনেক বার ট্রাই করে ও কারেন্সী কনভার্ট করতে পারি নাই 