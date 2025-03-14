%define __requires_exclude ^/(usr/)?bin/(ba)?sh$

Summary:        International Components for Unicode.
Name:           icu
Version:        68.2.0.6
Release:        2%{?dist}
License:        BSD and MIT and Public Domain and naist-2003
URL:            https://github.com/microsoft/icu
Group:          System Environment/Libraries
Vendor:         Microsoft Corporation
Distribution:   Mariner
#Source0:       %{url}/archive/v%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  python3
BuildRequires:  python3-xml
Provides:       libicu = %{version}-%{release}

%description
The International Components for Unicode (ICU) package is a mature, widely used set of C/C++ libraries providing Unicode and Globalization support for software applications.

%package    devel
Summary:        Header and development files
Requires:       %{name} = %{version}
Provides:       pkgconfig(icu-i18n)
Provides:       pkgconfig(icu-io)
Provides:       pkgconfig(icu-uc)
Provides:       libicu-devel = %{version}-%{release}

%description   devel
It contains the libraries and header files to create applications

%prep
%setup -q

%build
pushd icu/icu4c/source

autoconf
%configure --prefix=%{_prefix}
make %{?_smp_mflags}

popd

%install
make -C icu/icu4c/source DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%license LICENSE
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*.so.68
%{_libdir}/*.so.68.*
%exclude %{_libdir}/debug/
%exclude %{_libdir}/icu/

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_datadir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Mon Feb 28 2022 Pawel Winogrodzki <pawelwi@microsoft.com> - 68.2.0.6-2
- Removing dependcy on Bash.

* Fri Apr 16 2021 CBL-Mariner Service Account <cblmargh@microsoft.com> - 68.2.0.6-1
- Update to version  "68.2.0.6".
- Explicitly listing provided shared libraries' versions.

* Sun Apr 04 2021 CBL-Mariner Service Account <cblmargh@microsoft.com> - 68.2.0.1-1
- Update to version  "68.2.0.1".

* Tue Nov 03 2020 Joe Schmitt <joschmit@microsoft.com> - 64.2.0.2-2
- Provide libicu and libicu-devel.

*   Fri Jul 31 2020 Nick Samson <nisamson@microsoft.com> 64.2.0.2-1
-   Updated to 64.2.0.2.

*   Wed Jun 17 2020 Pawel Winogrodzki <pawelwi@microsoft.com> 64.2.0.1-1
-   Switching to Microsoft's fork of ICU and the 64.2.0.1 version.
-   Adding explicit pkgconfig 'Provides' tags.

*   Sat May 09 2020 Nick Samson <nisamson@microsoft.com> 61.2-2
-   Added %%license line automatically

*   Tue Apr 21 2020 Pawel Winogrodzki <pawelwi@microsoft.com> 61.2-1
-   Updated to version 61.2 (61-2 using project's version numbering)
-   Fixed "Source0" and "URL" tags.
-   Removed "%%define sha1".
-   Replaced tabs with spaces.
-   License verified.

*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 61.1-2
-   Initial CBL-Mariner import from Photon (license: Apache2).

*   Thu Sep 13 2018 Siju Maliakkal <smaliakkal@vmware.com> 61.1-1
-   Update to latest version

*   Wed Jan 31 2018 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 55.1-1
-   Initial build for photon
