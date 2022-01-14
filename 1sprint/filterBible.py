def filterBible(scripture, book, chapter):
    result=[]
    for i in range(len(scripture)):
        if scripture[i][:2]==book and scripture[i][2:5]==chapter:
            result.append(scripture[i])
    return result