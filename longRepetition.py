def longest_repetition(input):
    best=None #element
    current=None #element
    length=0
    cur_len=0
    for e in input:
        if current!=e: #element nd its predecessor are not same so we start ovr with this element
            current=e
            cur_len=1
        else: cur_len=cur_len+1 # we got two same elements
        if cur_len>length:
            best=current
            length=cur_len
    return best,length

print(longest_repetition([7,5,5,6,6,6,7,5,2,2]))