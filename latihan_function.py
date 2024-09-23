# Function -- Method

def sapa(): # non argument
    print("halo abang apa kabar?")

def sapa2(nama): # argument
    print(f"halo abang {nama} apa kabar?")

# sapa()
# sapa2('Adi')


def luas_segitiga(alas,tinggi):
    luas = alas * tinggi / 2
    return luas
    
# hasil = luas_segitiga(10,20)
# print(type(hasil))

# print(f'luas segitiga adalah: {hasil}')


def tambah2an(x,y):
    z = x + y
    return z

# hasil = tambah2an(5,5)
# print(hasil)

def penghasilan(fulltime,freelance):
    hasil_bruto = fulltime + freelance
    return hasil_bruto

# bruto = penghasilan(20000000,10000000)

# penghasilan_netto = bruto * 95/100 

# print(penghasilan_netto)

def kenalan(nama,pekerjaan,gaji): #positional argument
    print(f'perkenalkan nama saya adalah {nama}. saya seorang {pekerjaan}. Penghasilan saya {gaji}')
    
# # kenalan('Uno','Guru',10000000)
# kenalan(nama='Uno',gaji=100000000,pekerjaan='yutuber')

# nama = input('masukkan nama: ')
# #arbitary argument -> output argument tuple -> Args
# def bapack(*nama):
#     print('berikut ini nama warga RT 001:')
#     for bapak in nama:
#         print(f'bapak {bapak} warga RT 001')


# bapack(nama)

#Keywords Argument -> Dict - Kwargs
def data_diri(**data):
    print(f'nama saya adalah {data['nama']}. pekerjaan saya adalah {data['pekerjaan']}')
    
data_diri(nama='Uno',pekerjaan='QA',alamat='Jonggol')