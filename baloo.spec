#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : baloo
Version  : 5.59.0
Release  : 17
URL      : https://download.kde.org/stable/frameworks/5.59/baloo-5.59.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.59/baloo-5.59.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.59/baloo-5.59.0.tar.xz.sig
Summary  : A framework for searching and managing metadata
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: baloo-bin = %{version}-%{release}
Requires: baloo-data = %{version}-%{release}
Requires: baloo-lib = %{version}-%{release}
Requires: baloo-license = %{version}-%{release}
Requires: baloo-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : kbookmarks-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kfilemetadata-dev
BuildRequires : ki18n-dev
BuildRequires : kidletime-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : kservice-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : lmdb-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : solid-dev

%description
# Baloo
## Introduction
Baloo is the file indexing and file search framework for KDE Plasma. It focuses
on speed and a very small memory footprint. It maintains an index of your files
and optionally their contents which [you can search](@ref searching).

%package bin
Summary: bin components for the baloo package.
Group: Binaries
Requires: baloo-data = %{version}-%{release}
Requires: baloo-license = %{version}-%{release}

%description bin
bin components for the baloo package.


%package data
Summary: data components for the baloo package.
Group: Data

%description data
data components for the baloo package.


%package dev
Summary: dev components for the baloo package.
Group: Development
Requires: baloo-lib = %{version}-%{release}
Requires: baloo-bin = %{version}-%{release}
Requires: baloo-data = %{version}-%{release}
Provides: baloo-devel = %{version}-%{release}
Requires: baloo = %{version}-%{release}
Requires: baloo = %{version}-%{release}

%description dev
dev components for the baloo package.


%package lib
Summary: lib components for the baloo package.
Group: Libraries
Requires: baloo-data = %{version}-%{release}
Requires: baloo-license = %{version}-%{release}

%description lib
lib components for the baloo package.


%package license
Summary: license components for the baloo package.
Group: Default

%description license
license components for the baloo package.


%package locales
Summary: locales components for the baloo package.
Group: Default

%description locales
locales components for the baloo package.


%prep
%setup -q -n baloo-5.59.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560033132
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1560033132
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/baloo
cp COPYING %{buildroot}/usr/share/package-licenses/baloo/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/baloo/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang baloo_file5
%find_lang baloo_file_extractor5
%find_lang balooctl5
%find_lang baloodb5
%find_lang balooengine5
%find_lang baloomonitorplugin
%find_lang baloosearch5
%find_lang balooshow5
%find_lang kio5_baloosearch
%find_lang kio5_tags
%find_lang kio5_timeline

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/baloo_file
/usr/bin/baloo_file_extractor
/usr/bin/balooctl
/usr/bin/baloosearch
/usr/bin/balooshow

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.BalooWatcherApplication.xml
/usr/share/dbus-1/interfaces/org.kde.baloo.file.indexer.xml
/usr/share/dbus-1/interfaces/org.kde.baloo.fileindexer.xml
/usr/share/dbus-1/interfaces/org.kde.baloo.main.xml
/usr/share/dbus-1/interfaces/org.kde.baloo.scheduler.xml
/usr/share/icons/hicolor/128x128/apps/baloo.png
/usr/share/kservices5/baloosearch.protocol
/usr/share/kservices5/tags.protocol
/usr/share/kservices5/timeline.protocol
/usr/share/xdg/autostart/baloo_file.desktop
/usr/share/xdg/baloo.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Baloo/Baloo/File
/usr/include/KF5/Baloo/Baloo/FileMonitor
/usr/include/KF5/Baloo/Baloo/IndexerConfig
/usr/include/KF5/Baloo/Baloo/Query
/usr/include/KF5/Baloo/Baloo/QueryRunnable
/usr/include/KF5/Baloo/Baloo/ResultIterator
/usr/include/KF5/Baloo/Baloo/TagListJob
/usr/include/KF5/Baloo/baloo/core_export.h
/usr/include/KF5/Baloo/baloo/file.h
/usr/include/KF5/Baloo/baloo/filemonitor.h
/usr/include/KF5/Baloo/baloo/indexerconfig.h
/usr/include/KF5/Baloo/baloo/query.h
/usr/include/KF5/Baloo/baloo/queryrunnable.h
/usr/include/KF5/Baloo/baloo/resultiterator.h
/usr/include/KF5/Baloo/baloo/taglistjob.h
/usr/include/KF5/baloo_version.h
/usr/lib64/cmake/KF5Baloo/KF5BalooConfig.cmake
/usr/lib64/cmake/KF5Baloo/KF5BalooConfigVersion.cmake
/usr/lib64/cmake/KF5Baloo/KF5BalooTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Baloo/KF5BalooTargets.cmake
/usr/lib64/libKF5Baloo.so
/usr/lib64/pkgconfig/Baloo.pc
/usr/lib64/qt5/mkspecs/modules/qt_Baloo.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Baloo.so.5
/usr/lib64/libKF5Baloo.so.5.59.0
/usr/lib64/libKF5BalooEngine.so.5
/usr/lib64/libKF5BalooEngine.so.5.59.0
/usr/lib64/qt5/plugins/kf5/kded/baloosearchmodule.so
/usr/lib64/qt5/plugins/kf5/kio/baloosearch.so
/usr/lib64/qt5/plugins/kf5/kio/tags.so
/usr/lib64/qt5/plugins/kf5/kio/timeline.so
/usr/lib64/qt5/qml/org/kde/baloo/experimental/libbaloomonitorplugin.so
/usr/lib64/qt5/qml/org/kde/baloo/experimental/qmldir
/usr/lib64/qt5/qml/org/kde/baloo/libbalooplugin.so
/usr/lib64/qt5/qml/org/kde/baloo/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/baloo/COPYING
/usr/share/package-licenses/baloo/COPYING.LIB

%files locales -f baloo_file5.lang -f baloo_file_extractor5.lang -f balooctl5.lang -f baloodb5.lang -f balooengine5.lang -f baloomonitorplugin.lang -f baloosearch5.lang -f balooshow5.lang -f kio5_baloosearch.lang -f kio5_tags.lang -f kio5_timeline.lang
%defattr(-,root,root,-)

