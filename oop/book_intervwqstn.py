books={
       "alchemist":{"book_name":"alchemist","author":"paulo","price":200,"av_copies":100,"sold":10}
       "halfgirlfriend":{"book_name":"halfgirlfriend","author":"chetan","price":300,"av_copies":300,"sold":200}
       "rainrising":{"book_name":"rainrising","author":"nirupama","price":350,"av_copies":0,"sold":320}
}

#nirupama,chetan,paule
#find book
#bookname,nocopies
#alchemist

#sort based on items

#"alchemist":{"book_name":"alchemist","author":"paulo","price":200,"av_copies":100,"sold":10}
#x[0]=>alchemist
#x[1]["sold"]=>{"book_name":"alchemist","author":"paulo","price":200,"av_copies":100,"sold":10}

res=sorted(books.items(),key=lambda x:x[1]["sold"],reverse=True)
for val in res:
    print(val[1]["author"])

