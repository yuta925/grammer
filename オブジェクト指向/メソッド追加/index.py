# メソッド追加

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self): # オブジェクトを文字列に変換する特殊メソッド
        return self.first_name + ", " + self.last_name

person1 = Person("John", "Smith")
print(person1.get_name())
print(person1)