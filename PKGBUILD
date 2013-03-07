#Maintainer: Weitian Leung<weitianleung@gmail.com>

pkgname=wps-office
pkgver=PKG_VER
pkgrel=1
pkgdesc="Kingsoft Office is an office productivity suite. "
arch=('i686' 'x86_64')
license=("Custom")
url="http://www.wps.cn/"
install=${pkgname}.install 
pkgext=".pkg.tar"
sha1sums=('SHA1')
source=("file:///PKG_SOURCE")

if [ "$CARCH" = "i686" ]; then
    depends=('fontconfig' 'glib2' 'libpng12' 'libsm' 'libxext' 'libxdmcp' 'libxrender' 'libcups' 'glu' 'libgl')
elif [ "$CARCH" = "x86_64" ]; then
    depends=('lib32-fontconfig' 'lib32-glib2' 'lib32-libpng12' 'lib32-libsm' 'lib32-libxext' 'lib32-libxdmcp' 'lib32-libxrender' 'lib32-libcups' 'lib32-glu' 'lib32-libgl')
fi
depends+=('desktop-file-utils' 'shared-mime-info' 'xdg-utils')

package()
{
    cd "${srcdir}"
    tar azxvf data.tar.gz -C "${pkgdir}"
}
