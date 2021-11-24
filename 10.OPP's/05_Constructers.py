class BookStore:
    companyName: 'IT Series'

    def __init__(self, bookName, bookPrice, bookEdition, storeName):
        print("I am a constructor")
        self.bookName = bookName
        self.bookPrice = bookPrice
        self.bookEdition = bookEdition
        self.storeName = storeName

    def byerDetails(self):
        print(f"BookName:{self.bookName}")
        print(f"BookPrice:{self.bookPrice}")
        print(f"BookEdition:{self.bookEdition}")
        print(f"StoreName:{self.storeName}")


Byer1 = BookStore("C++ with OPP's", "600PKR",
                  "4rth Edition", "Saeed Book Center")
Byer1.byerDetails()
