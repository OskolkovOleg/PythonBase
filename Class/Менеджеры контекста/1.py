try:
    with open("myfile.txt") as f:
        for t in f:
            print(t)
            
except Exception as e:
    print(e)