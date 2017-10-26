#-*- coding:utf-8 -*-
#闭包
def outer():
    def inner():
        return 1
    return inner


def outer():
    def inner():
	return 1
    return inner()

print(outer())
