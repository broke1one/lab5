jewelery_inventory = {
    "Золотое кольцо с бриллиантом":{
        "описание": "Золотое кольцо с бриллиантом весом 0.5 карат",
        "цена": "1300",
        "количество": "7"
    },
    "Серебрянная подвеска":{
        "описание": "Подвеска из серебра 925 пробы",
        "цена": "700",
        "количество": "5"
    },
    "Мужская цепь АРГО":{
        "описание": "Стильная мужская цепь из серебра, которая выделит вас среди остальных",
        "цена": "200",
        "количество": "24",
    },
    "Браслет CARTIER":{
        "описание": "Сияющий лучами солнца браслет Cartier изготовлен из золота 585 пробы",
        "цена": "7800",
        "количество": "2",
    },
    "Золотое обручальное кольцо с рубином":{
        "описание": "Кольцо из золота 585 пробы с инкрустированным рубином",
        "цена": "920",
        "количество": "11",
    }
}

print ("Добро пожаловать в ювелирный магазин \n выберите действие \n1 - Просмотр описания\n2 - Просмотр цены \n3 - Просмотр количества\n4 - Просмотр всей информации\n5 - Покупака \n0 - Выход из магазина\n")
while True:
    choice = input("Выберите действие: ")
    if choice == '1':
        print("Описание изделий: ")
        for product_name, product_info in jewelery_inventory.items():
            print("Название товара: ",product_name)
            print("Описание товара: ",product_info["описание"])
            print("")
    elif choice == '2':
        for product_name, product_info in jewelery_inventory.items():
            print("Название товара: ",product_name)
            print("Цена товара: ",product_info["цена"],"$")
            print()
    elif choice == '3':
        print("Колиство товаров: ")
        for product_name,product_info in jewelery_inventory.items():
            print("Название товара:", product_name)
            print("Количество товара: ", product_info["количество"])
            print("")
    elif choice == '4': 
        print("Вся инфорамция о товарах: ")
        for product_name, product_info in jewelery_inventory.items():
            print("Название товара: ", product_name)
            print("Описание товара: ", product_info["описание"] )
            print("Цена товара: ", product_info["цена"],"$")
            print("Количество товара: ", product_info["количество"])
            print()
    elif choice == '5':
        print("Выберите товар(ы) для покупки: ")
        i = 1
        for product_name, product_info, in jewelery_inventory.items():

            print(f"{i}: {product_name} -", product_info["цена"],"$")
            i += 1
            print("")
        final_price = 0
        while True:
            choice = input("Введите название товара из списка или 0 для выхода: ")
            if choice in jewelery_inventory:
                product_info = jewelery_inventory[choice]
                avaliable_amount = int(product_info["количество"])
                amount = int(input("Введите сколько позиций товара вы хотите приобрести: "))
                price = 0
                if amount > avaliable_amount:
                    print("Нет такого колиства товара, всего в наличии " + str(avaliable_amount) + " штук(и)")
                elif amount < avaliable_amount:
                     print("нельязя выбирать такие значения" + str(avaliable_amount) + " штук(и)")
                else:
                    price = int(amount) * int(product_info["цена"])
                    final_price += price
                    print("Товар добавлен в корзину")
                    product_info["количество"] = avaliable_amount - amount
            elif choice == "0":
                if final_price > 0:
                    print(f"К оплате {final_price} $")
                    print("Возврат в предыдущему меню")
                    break
                else:
                    print("Возврат в предыдущееменю")
                    break
            else:
                print("Такого товара не существует")

    elif choice == '0':
        print("До свидания, заходите еще!!!")
        break
    else:
        print("Неверный выобр, выберите корректный выбор")