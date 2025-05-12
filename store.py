class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Словарь для хранения товаров

# Добавление товаров
    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} добавлен в магазин {self.name}")

# Удаление товара
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удален из магазина {self.name}")
        else:
            print(f"Товар {item_name} не найден в магазине {self.name}")

# Получение цены
    def get_price(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        else:
            print(f"Товар {item_name} не найден в магазине {self.name}")
            return None

# Изменение цены
    def change_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} в магазине {self.name} изменена на {new_price}")
        else:
            print(f"Товар {item_name} не найден в магазине {self.name}")


# Создание экземпляров магазинов
store1 = Store("Перекресток", "ул. Пушкина 40")
store2 = Store("5+", "ул. Лесная 40")
store3 = Store("Рэмми", "ул. Ладыгина 40")

# Добавление товаров (исправлены имена методов)
store1.add_item("молоко", 50)
store2.add_item("Сахар", 120)
store3.add_item("Крупа", 60)

# Удаление товара
store1.remove_item("молоко")

# Изменение цен
store1.change_price("молоко", 70)  # Товар уже удален, будет сообщение об ошибке
store2.change_price("Сахар", 150)
store3.change_price("Крупа", 90)

# Получение цены
print(store2.get_price("Сахар"))









