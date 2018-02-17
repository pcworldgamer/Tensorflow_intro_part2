# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 15:14:11 2018

@author: pjcfe
"""

#TensorFlow variables and placeholders
import tensorflow as tf

tf.reset_default_graph()
sess=tf.Session()

x = tf.Variable(2.0,tf.float32)
y = tf.Variable(3.0,tf.float32)

init = tf.global_variables_initializer()
sess.run(init)

a = tf.placeholder(tf.float32)

sumnodes = x*a + y

print(sess.run(sumnodes,{a: range(10)}))

#sess.run(x.assign(5))
#NewX = x.assign(5)
#NewY = y.assign(10)

#sess.run([NewX,NewY])

#print(sess.run(sumnodes))

sess.close()