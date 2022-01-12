import os
import sys
from setuptools import setup, find_packages

# Must be ran as root or as sudo
if os.getuid() != 0:
    print('HATA: Root veya sudo olarak çalıştırmanız gerekiyor')
    sys.exit(1)

# Install the requirements if the system does not have it installed
print('BİLGİ: Gerekenleri kontrol et ve yükle')
os.system('! dpkg -S python-imaging-tk && apt-get -y install python-imaging-tk')

# Generate the requirements from the file for old instructions
print('BİLGİ: Gerekenler.txt dosyasından indirilecek kütüphaneler vardır')
packages = []
for line in open('gerekenler.txt', 'r'):
    if not line.startswith('#'):
        packages.append(line.strip())

# Run setuptools for pip
setup(
    name='akilliayna',
    version='1.0',
    description='Haberleri, hava durumunu, takvim etkinliklerini görüntüleyebilen raspberry pi ile çalışan ayna projesi',
    author='SahinOzerrpi',
    url='https://github.com/SahinOzerrpi/Akilli-Ayna',
    install_requires=packages,
    packages=find_packages(),
)