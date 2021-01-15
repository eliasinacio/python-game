re = int(input('Deseja transformar: \n 1. Celsius. \n 2. Fahrenheit. \n 3. Kelvin. \n >'))
pa = int(input('Em: \n 1. Celsius. \n 2. Fahrenheit. \n 3. Kelvin. \n >'))
if re == 1:
    vc = int(input(' Digite a temperatura em Celsius: '))
    if pa == 2:
        tf = (vc * 9/5) + 32
        print(' {}°C equivale a {:.2f}°F. '.format(vc, tf))
    elif pa == 3:
        tf = (vc + 273)
        print(' {}°C equivale a {} K. '.format(vc, tf))

elif re == 2:
    vf = int(input(' Digite a temperatura em Fahrenheit: '))
    if pa == 1:
        tf = (vf - 32) * 5/9
        print(' {}°F equivale a {:.1f}°C.'.format(vf, tf))
    elif pa == 3:
        tf = ((vf - 32) * 5/9) + 273
        print(' {}°F equivale a {:.1f} K. '.format(vf, tf))

elif re == 3:
    vk = int(input(' Digite a temperatura em Kelvin. '))
    if pa == 1:
        tf = (vk - 273)
        print(' {} K equivale a {:.1f}°C. '.format(vk, tf))
    elif pa == 2:
        tf = ((vk - 273) * 9/5) + 32
        print(' {} K equivale a {:.1f}°F. '.format(vk, tf))