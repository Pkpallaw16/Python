# Import classes from your brand new package
import sys
print(sys.path)
sys.path.append(r'C:\Users\PALLAW-PC\PycharmProjects\Cars')
sys.path.append(r'C:\Users\PALLAW-PC\PycharmProjects\Cars\subpack')
sys.path.append(r'C:\Users\PALLAW-PC\PycharmProjects')
import calc_subpack
import Bmw
import Audi
from Cars.Nissan import Nissan

print(calc_subpack.add(4,5))
# Create an object of Bmw class & call its method
ModBMW = Bmw.Bmw()
ModBMW.outModels()

# Create an object of Audi class & call its method
ModAudi = Audi.Audi()
ModAudi.outModels()

# Create an object of Nissan class & call its method
ModNissan = Nissan()
ModNissan.outModels()
