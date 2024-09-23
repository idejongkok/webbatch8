
# method / function untuk fitur luas segitiga
def luas_segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    return luas

print(luas_segitiga(10,20))

# unit test luas segitiga
def test_luas_segitiga():
    alas = 10
    tinggi = 20
    luas = luas_segitiga(alas,tinggi)
    
    assert luas == 100.0