# -*- coding: utf-8 -*-
out =[]
with open('nederlands.txt','r') as file:
	out=[decode(i,'utf-8').split(" ")[:2] for i in file]
for i in out[:20]:
	print(i)
