#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

# my_file = open('notes.txt', 'w')
# # lines = my_file.readlines()
# # first_line = my_file.readline()
# # second_line = my_file.readline()
# # print('first_line=%s' % first_line)
# # print('second_line=%s' % second_line)
# # print(type(first_line))
# # my_file.write('\n星期一')
# print >> my_file, "Hello there,neighbor!"
# my_file.close()
# my_list = ['Fred', 73, '你好', 81.9876e-13]
# pickle_file = open('my_pickled_list.pkl', 'w')
# pickle.dump(my_list, pickle_file)
# pickle_file.close()
pickle_file = open('my_pickled_list.pkl', 'r')
reconvered_list = pickle.load(pickle_file)
pickle_file.close()
print(reconvered_list)