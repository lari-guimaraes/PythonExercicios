l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
ar = l*a
print ('Sua tem a dimensão de {}x{} e sua área é de {}m²'.format(l,a,ar))
t = (ar/2)
print('Sera necessario {} litros de tinta para pintar a parede'.format(t))
