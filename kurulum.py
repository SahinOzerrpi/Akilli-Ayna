import os
import sys
from setuptools import setup, find_packages

# Root veya sudo olarak çalıştırılmalıdır
if os.getpid() != 0:
    print('HATA: Root veya sudo olarak çalıştırmanız gerekiyor')
    sys.exit(1)

# Sistemde kurulu değilse gereksinimleri yükleyin
print('BİLGİ: Gerekenleri kontrol et ve yükle')
os.system('! dpkg -S python-imaging-tk && apt-get -y install python-imaging-tk')

# Gerekli kütüphaneler için dosyadan gereksinimleri oluşturun
print('BİLGİ: Gerekenler.txt dosyasından indirilecek kütüphaneler vardır')
packages = []
for line in open('gerekenler.txt', 'r'):
    if not line.startswith('#'):
        packages.append(line.strip())

# pip için setuptools'u çalıştırın
setup(
    name='akilliayna',
    version='1.0',
    description='Haberleri, hava durumunu, takvim etkinliklerini görüntüleyebilen raspberry pi ile çalışan ayna projesi',
    author='SahinOzerrpi',
    url='https://github.com/SahinOzerrpi/Akilli-Ayna',
    install_requires=packages,
    packages=find_packages(),
)