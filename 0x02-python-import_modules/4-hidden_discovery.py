#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    c = dir(hidden_4)
    for i in range(len(c)):
        if c[i][0] != "_" and c[i][1] != "_":
            print(c[i])
