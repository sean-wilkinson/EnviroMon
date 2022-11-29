from machine import Pin, I2C

i2c0 = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
i2c1 = I2C(1, scl=Pin(19), sda=Pin(18), freq=400000)




print('Scan i2c0 bus...')
devices = i2c0.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
    
    
    

print('Scan i2c1 bus...')
devices = i2c1.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))