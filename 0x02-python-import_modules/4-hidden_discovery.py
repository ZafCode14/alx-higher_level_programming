#!/usr/bin/python3
import hidden_4
for i in range(len(dir(hidden_4))):
    if dir(hidden_4)[i][0] == '_' and dir(hidden_4)[i][1] == '_':
        continue
    print(dir(hidden_4)[i])
