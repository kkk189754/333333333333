class Animal:#基类
    
    def __init__(self,name,age):

        self._name = name#封装:protected

        self._age = age
    
    def sound(self):#基类方法

        print(f"{self._name}发出声音")
    
    def display(self):

        print(f"动物名称:{self._name},年龄:{self._age}岁")

class Dog(Animal):#狗类继承自动物类

    def __init__(self,name,age,breed):

        super().__init__(name,age)#复写后调用父类方法

        self._breed=breed#封装
    
    def sound(self):#重写基类方法

        print(f"{self._name}汪汪")
    
    def display(self):

        print(f"狗狗{self._name},品种:{self._breed},年龄:{self._age}岁")
    
    def move1(self):

        print(f"{self._name}会接飞盘")

class Cat(Animal):#猫类继承自动物类

    def __init__(self,name,age,color):

        super().__init__(name,age)#复写后调用父类方法

        self._color=color#封装

    def sound(self):#重写基类方法

        print(f"{self._name}喵喵")
    
    def display(self):

        print(f"猫咪{self._name},颜色:{self._color},年龄:{self._age}岁")
    
    def move2(self):

        print(f"{self._name}会爬树")
    
dog = Dog("a",2,"金毛")#创建对象

cat = Cat("b",1,"白色")#创建对象
    
animals=[Dog("a",3,"拉布拉多"),Cat("b",2,"三花")]
    
for animal in animals:#用循环写不同对象的不同行为

    animal.sound()

    animal.display()

    print()
    
dog.move1()#子类特有的

cat.move2()#子类特有的
    