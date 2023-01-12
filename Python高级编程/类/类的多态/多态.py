# coding:utf-8
# author：我本善良
# create_time：2021/5/31 20:55

'''
1、什么是类的多态?
    例子：
        小穆爸爸：平淡说话
        小穆哥哥：说话，语速很快
        小   穆：说话，语速很慢
    同一个功能，表现出了多状态化，叫做多态

2、多态的用法
    子类中，重写父类的方法


'''
#1、书写一个父类
class XiaomuFather(object):
    def talk(self):
        print('小幕的爸爸说了一句话')

    def jump(self):
        print('大家都可以跳')

#2、书写一个子类，并且继承一个父类
class XiaomuBrother(XiaomuFather):
    def run(self):
        print('小幕哥哥在奔跑……')

    def talk(self):
        print('小幕哥哥在说话…')


class Xiaomu(XiaomuFather):
    def talk(self):
        print('haha 小幕也可以开心说自己的观点')





if __name__ == '__main__':
    xiaomu_brother = XiaomuBrother()
    xiaomu_brother.talk()
    xiaomu_brother.jump()
    father = XiaomuFather()
    father.talk()
    xiaomu = Xiaomu()
    xiaomu.talk()
    xiaomu.jump()


'''
1、为什么要去多态?
    答案：为了使用已经写好的类中的函数
    
2、为什么要去继承多态?
    为了保留子类中某个和父类名称一样的函数的功能，
    这时候，我们就用到了类的多态，可以帮助我们保留子类中的函数功能


    关于类的多态描述正确的是:关于多态是一个比较抽象的概念，简单的理解，
多态就是一个类继承了父类并重写父类的方法。即一个类的多种状态就是多态
    
'''

