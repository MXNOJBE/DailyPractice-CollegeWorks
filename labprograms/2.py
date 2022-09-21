def split(s):
    #after = ""
    rem = ". "
    rem2 = "?"
    #for x in range (len(s)):
    #    if(". " == x or "?" == x or "!" == x):
    #       after = s.split(x)
    after = s.split(rem)
    after = s.split(rem2)

    res = dict()
    for x, ele in enumerate(after):
        res[x+1] = ele

    print(str(res))

#split("I bought a new laptop for $3.5k. The medel was recommended by my friend, Dr. Smith. I like its functionalities, but found that the same model is sold for only $2.8k at amazon .com... Lessons learned? It’s worth checking online prices before shopping!")
