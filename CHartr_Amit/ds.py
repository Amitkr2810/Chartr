with open('flag.txt') as f:
        count =0
        for routes in f:
            if '(NS)' in routes:
                count+=1
        print(count)
