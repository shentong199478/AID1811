#!/usr/bin/python3
print("   *\n  ***\n *****\n*******")
print("古代的216两是古代的",216//16,"斤",216%16,"两")
print("现在是",63320//(60*60),"时",(63320-(63320//(60*60))*60*60)//60,"分",63320%60,"秒")
def __ster__(x):
	return(5.0/9.0*(x - 32))
def __kter__(x):
	return(__ster__(x) + 273.15)
x = 100
print("华氏温度为",'%.2f' % __ster__(x),"度")
print("开氏温度为",'%.2f' % __kter__(x),"度")
