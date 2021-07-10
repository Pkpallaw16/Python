# Import classes from your brand new package
import sys
print(sys.path)
sys.path.append(r'C:\Users\PALLAW-PC\PycharmProjects\Cars')
import Bmw
import Audi
import Nissan

# Create an object of Bmw class & call its method
ModBMW = Bmw.Bmw()
ModBMW.outModels()

# Create an object of Audi class & call its method
ModAudi = Audi.Audi()
ModAudi.outModels()

# Create an object of Nissan class & call its method
ModNissan = Nissan.Nissan()
ModNissan.outModels()
