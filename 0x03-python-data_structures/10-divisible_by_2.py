def divisible_by_2(my_list=[]):
    tf = []
    for i in my_list:
        if i % 2 == 0:
            tf.append(True)
        else:
            tf.append(False)
    return tf
