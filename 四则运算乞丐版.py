import random


def Farithmetic(m):
    print("小学四则运算测试(共%d道,答案保留两位小数):" % m)
    ysf = ['+', '-', '*', '/']

    i = 1 #题号
    n = 0 #记录答题正确个数
    while i <= m:
        add1 = random.randint(1, 100)  #数
        add2 = random.randint(1, 100)
        add3 = random.randint(1, 100)
        op1 = random.randint(0, 3)     #随机运算符
        op2 = random.randint(0, 3)
        eq = str(add1)+ysf[op1]+str(add2)+ysf[op2]+str(add3) #算式
        eq1 = str(add1)+ysf[op1]+str(add2)
        eq2 = str(add2)+ysf[op2]+str(add3)
        val1 = eval(eq1)
        val2 = eval(eq2)
        val = eval(eq)     # 算式答案
        if ysf[3] in eq:   #判断是否出现真分数
            if ysf[3] in eq1:
                if val1 > 1:
                    tmp = add1
                    add1 = add2
                    add2 = tmp
                if val1 == 1:
                    continue
            else:
                if val2 > 1:
                    tmp = add2
                    add2 = add3
                    add3 = tmp
                if val2 == 1:
                    continue
            eq = str(add1)+ysf[op1]+str(add2)+ysf[op2]+str(add3) #算式重置
            val = eval(eq)
        if val1 < 0 or val2 < 0 or val < 0: #判断答案是否为负数
            continue
        if val > 1000:  # 限制答案在合理范围
            continue
        print("题目%d:%s=" % (i, eq))
        ans = input("用户回答:")

        if val == int(ans):
            print("Congratulation,you are right!")
            n += 1
        else:
            print("Sorry,your answer is error.The right answer is %.2f" % val)
        if i == m:  # 退出循环
            y = n / (i - 1)
            print("本次答题结束，答题正确率是：%.2f" % y)
        i += 1


m = int(input('输入需要出的题目数：'))
Farithmetic(m)
