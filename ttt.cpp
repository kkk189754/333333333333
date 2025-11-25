#include <iostream>
#include <string>
using namespace std;

class Animal {//基类

protected:

    string name;

    int age;

public:

    Animal(string n,int a):name(n),age(a)//初始化列表
    {

    }
    
    virtual void Sound()=0;//纯虚函数，具体由子类实现
    
    virtual void display()=0;//纯虚函数，具体由子类实现
    
    virtual ~Animal(){}//虚析构函数
};

class Dog:public Animal{//继承：狗类继承自动物类

private:

    string breed;//狗的品种

public:

    Dog(string n,int a,string b):Animal(n,a),breed(b)//初始化列表
    {

    }
    
    virtual void Sound(){//多态：重写基类方法

        cout<<name<<"在汪汪叫"<<endl;
    }
    
    virtual void display(){

        cout<<"狗狗:"<<name<<",品种:"<<breed<<",年龄:"<<age<<"岁"<<endl;

    }
    
    void move1() {

        cout<<name<<"会接飞盘"<<endl;

    }
};

class Cat:public Animal{//继承：猫类继承自动物类
    
private:

    string color;//猫的颜色

public:

    Cat(string n,int a,string c):Animal(n,a),color(c)//初始化列表
    {

    }
    
    virtual void Sound(){//多态：重写基类方法

        cout<<name<<"在喵喵叫"<<endl;
    }
    
    virtual void display(){

        cout<<"猫:"<<name<<",颜色:"<<color<<",年龄:"<<age<<"岁"<<endl;
    }
    
    void move2() {

        cout<<name<<"会爬树"<<endl;

    }
};

int main() {

    Dog dog("lll",1,"拉布拉多");//创建对象

    Animal*animal1=new Dog("lll",1,"拉布拉多");

    animal1->display();

    animal1->Sound();

    dog.move1();//调用子类独有的方法

    Cat cat("ttt",2,"三花");//创建对象

    Animal*animal2=new Cat("ttt",2,"三花");

    animal2->display();

    animal2->Sound();

    cat.move2();//调用子类独有的方法

    delete animal1,animal2;//堆区的对象手动删除

    return 0;
}