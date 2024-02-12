#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : baloo
Version  : 5.115.0
Release  : 72
URL      : https://download.kde.org/stable/frameworks/5.115/baloo-5.115.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.115/baloo-5.115.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.115/baloo-5.115.0.tar.xz.sig
Summary  : A framework for searching and managing metadata
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 bzip2-1.0.6
Requires: baloo-bin = %{version}-%{release}
Requires: baloo-data = %{version}-%{release}
Requires: baloo-lib = %{version}-%{release}
Requires: baloo-license = %{version}-%{release}
Requires: baloo-locales = %{version}-%{release}
Requires: baloo-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig
BuildRequires : kconfig-dev
BuildRequires : kfilemetadata-dev
BuildRequires : kidletime-dev
BuildRequires : kio-dev
BuildRequires : lmdb-dev
BuildRequires : qt6base-dev
BuildRequires : solid-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Baloo
## Introduction
Baloo is the file indexing and file search framework for KDE Plasma. It focuses
on speed and a very small memory footprint. It maintains an index of your files
and optionally their contents which [you can search](./docs/user/searching.md).

%package bin
Summary: bin components for the baloo package.
Group: Binaries
Requires: baloo-data = %{version}-%{release}
Requires: baloo-license = %{version}-%{release}
Requires: baloo-services = %{version}-%{release}

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


%package services
Summary: services components for the baloo package.
Group: Systemd services
Requires: systemd

%description services
services components for the baloo package.


%prep
%setup -q -n baloo-5.115.0
cd %{_builddir}/baloo-5.115.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707763143
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707763143
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/baloo
cp %{_builddir}/baloo-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/baloo/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/baloo-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/baloo/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/baloo-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/baloo/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/baloo-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/baloo/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/baloo-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/baloo/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/baloo-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/baloo/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/baloo-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/baloo/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/baloo-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/baloo/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/baloo-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/baloo/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/baloo-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/baloo/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/baloo-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/baloo/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/baloo-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/baloo/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/baloo-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/baloo/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/baloo-%{version}/LICENSES/bzip2-1.0.6.txt %{buildroot}/usr/share/package-licenses/baloo/c86f08afa3409f52c8811ac27764e50469ef0bb0 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang baloo_file5
%find_lang baloo_file_extractor5
%find_lang balooctl5
%find_lang baloodb5
%find_lang balooengine5
%find_lang baloosearch5
%find_lang balooshow5
%find_lang kio5_baloosearch
%find_lang kio5_tags
%find_lang kio5_timeline
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/baloo_file
/V3/usr/lib64/libexec/baloo_file_extractor
/usr/lib64/libexec/baloo_file
/usr/lib64/libexec/baloo_file_extractor

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/balooctl
/V3/usr/bin/baloosearch
/V3/usr/bin/balooshow
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
/usr/share/qlogging-categories5/baloo.categories
/usr/share/qlogging-categories5/baloo.renamecategories
/usr/share/xdg/autostart/baloo_file.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Baloo/Baloo/File
/usr/include/KF5/Baloo/Baloo/FileMonitor
/usr/include/KF5/Baloo/Baloo/IndexerConfig
/usr/include/KF5/Baloo/Baloo/Query
/usr/include/KF5/Baloo/Baloo/QueryRunnable
/usr/include/KF5/Baloo/Baloo/ResultIterator
/usr/include/KF5/Baloo/Baloo/TagListJob
/usr/include/KF5/Baloo/baloo/baloosettings.h
/usr/include/KF5/Baloo/baloo/core_export.h
/usr/include/KF5/Baloo/baloo/file.h
/usr/include/KF5/Baloo/baloo/filemonitor.h
/usr/include/KF5/Baloo/baloo/indexerconfig.h
/usr/include/KF5/Baloo/baloo/query.h
/usr/include/KF5/Baloo/baloo/queryrunnable.h
/usr/include/KF5/Baloo/baloo/resultiterator.h
/usr/include/KF5/Baloo/baloo/taglistjob.h
/usr/include/KF5/Baloo/baloo_version.h
/usr/lib64/cmake/KF5Baloo/KF5BalooConfig.cmake
/usr/lib64/cmake/KF5Baloo/KF5BalooConfigVersion.cmake
/usr/lib64/cmake/KF5Baloo/KF5BalooTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Baloo/KF5BalooTargets.cmake
/usr/lib64/libKF5Baloo.so
/usr/lib64/pkgconfig/Baloo.pc
/usr/lib64/qt5/mkspecs/modules/qt_Baloo.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5Baloo.so.5.115.0
/V3/usr/lib64/libKF5BalooEngine.so.5.115.0
/V3/usr/lib64/qt5/plugins/kf5/kded/baloosearchmodule.so
/V3/usr/lib64/qt5/plugins/kf5/kio/baloosearch.so
/V3/usr/lib64/qt5/plugins/kf5/kio/tags.so
/V3/usr/lib64/qt5/plugins/kf5/kio/timeline.so
/V3/usr/lib64/qt5/qml/org/kde/baloo/experimental/libbaloomonitorplugin.so
/V3/usr/lib64/qt5/qml/org/kde/baloo/libbalooplugin.so
/usr/lib64/libKF5Baloo.so.5
/usr/lib64/libKF5Baloo.so.5.115.0
/usr/lib64/libKF5BalooEngine.so.5
/usr/lib64/libKF5BalooEngine.so.5.115.0
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
/usr/share/package-licenses/baloo/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/baloo/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/baloo/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/baloo/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/baloo/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/baloo/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/baloo/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/baloo/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/baloo/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/baloo/c86f08afa3409f52c8811ac27764e50469ef0bb0
/usr/share/package-licenses/baloo/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/baloo/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/kde-baloo.service

%files locales -f baloo_file5.lang -f baloo_file_extractor5.lang -f balooctl5.lang -f baloodb5.lang -f balooengine5.lang -f baloosearch5.lang -f balooshow5.lang -f kio5_baloosearch.lang -f kio5_tags.lang -f kio5_timeline.lang
%defattr(-,root,root,-)

