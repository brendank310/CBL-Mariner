Summary:        CBL-Mariner release files
Name:           mariner-release
Version:        2.0
Release:        11%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          System Environment/Base
URL:            https://aka.ms/cbl-mariner
# Allows package management tools to find and set the default value
# for the "releasever" variable from the RPM database.
Provides:       system-release(releasever)
BuildArch:      noarch

%description
Azure CBL-Mariner release files such as yum configs and other %{_sysconfdir}/ release related files

%install
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}/%{_libdir}

echo "CBL-Mariner %{mariner_release_version}" > %{buildroot}%{_sysconfdir}/mariner-release
echo "MARINER_BUILD_NUMBER=%{mariner_build_number}" >> %{buildroot}%{_sysconfdir}/mariner-release

cat > %{buildroot}%{_sysconfdir}/lsb-release <<- "EOF"
DISTRIB_ID="Mariner"
DISTRIB_RELEASE="%{mariner_release_version}"
DISTRIB_CODENAME=Mariner
DISTRIB_DESCRIPTION="CBL-Mariner %{mariner_release_version}"
EOF

version_id=`echo %{mariner_release_version} | grep -o -E '[0-9]+.[0-9]+' | head -1`
cat > %{buildroot}/%{_libdir}/os-release << EOF
NAME="Common Base Linux Mariner"
VERSION="%{mariner_release_version}"
ID=mariner
VERSION_ID="$version_id"
PRETTY_NAME="CBL-Mariner/Linux"
ANSI_COLOR="1;34"
HOME_URL="%{url}"
BUG_REPORT_URL="%{url}"
SUPPORT_URL="%{url}"
EOF

ln -sv ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release

cat > %{buildroot}%{_sysconfdir}/issue <<- EOF
Welcome to CBL-Mariner %{mariner_release_version} (%{_arch}) - Kernel \r (\l)
EOF

cat > %{buildroot}%{_sysconfdir}/issue.net <<- EOF
Welcome to CBL-Mariner %{mariner_release_version} (%{_arch}) - Kernel %r (%t)
EOF

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/mariner-release
%config(noreplace) %{_sysconfdir}/lsb-release
%config(noreplace) %{_libdir}/os-release
%config(noreplace) %{_sysconfdir}/os-release
%config(noreplace) %{_sysconfdir}/issue
%config(noreplace) %{_sysconfdir}/issue.net

%changelog
* Tue Apr 19 2022 Jon Slobodzian <joslobo@microsoft.com> - 2.0-11
- Updating version for GA Release Candidate

* Sat Apr 16 2022 Jon Slobodzian <joslobo@microsoft.com> - 2.0-10
- Updating version for Preview-H Release.

* Sat Apr 09 2022 Jon Slobodzian <joslobo@microsoft.com> - 2.0-9
- Updating version for Preview-G Release.

* Wed Mar 30 2022 Jon Slobodzian <joslobo@microsoft.com> - 2.0-8
- Updating version for Preview-F Release.

* Fri Mar 4 2022 Jon Slobodzian <joslobo@microsoft.com> - 2.0-7
- Updating version for Preview-E Release

* Thu Feb 24 2022 Pawel Winogrodzki <pawelwi@microsoft.com> - 2.0-6
- Surrounding 'VERSION_ID' inside 'os-release' with double quotes.

* Sun Feb 06 2022 Jon Slobodzian <joslobo@microsoft.com> - 2.0-5
- Updating version for Preview D-Release

* Wed Jan 19 2022 Jon Slobodzian <joslobo@microsoft.com> - 2.0-4
- CBL-Mariner 2.0 Public Preview C Release.
- License verified

* Thu Dec 16 2021 Jon Slobodzian <joslobo@microsoft.com> - 2.0-3
- CBL-Mariner 2.0 Public Preview B Release version with fixed repo configuration files.

* Mon Dec 13 2021 Jon Slobodzian <joslobo@microsoft.com> - 2.0-2
- CBL-Mariner 2.0 Public Preview A Release version.

* Thu Jul 29 2021 Jon Slobodzian <joslobo@microsoft.com> - 2.0-1
- Updating version and distrotag for future looking 2.0 branch.  Formatting fixes.
- Remove %%clean section, buildroot cleaning step (both automatically done by RPM)

* Wed Apr 27 2021 Jon Slobodzian <joslobo@microsoft.com> - 1.0-16
- Updating version for April update

* Tue Mar 30 2021 Jon Slobodzian <joslobo@microsoft.com> - 1.0-15
- Updating version for March update

* Mon Feb 22 2021 Jon Slobodzian <joslobo@microsoft.com> - 1.0-14
- Updating version for February update

* Sun Jan 24 2021 Jon Slobodzian <joslobo@microsoft.com> - 1.0-13
- Updating version for January update

* Mon Dec 21 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.0-12
- Updating version for December update.

* Fri Nov 20 2020 Nicolas Guibourge <nicolasg@microsoft.com> - 1.0-11
- Updating version for November update

* Sat Oct 24 2020 Jon Slobodzian <joslobo@microsoft.com> - 1.0-10
- Updating version for October update

* Fri Sep 04 2020 Mateusz Malisz <mamalisz@microsoft.com> - 1.0-9
- Remove empty %%post section, dropping dependency on /bin/sh

* Tue Aug 24 2020 Jon Slobodzian <joslobo@microsoft.com> - 1.0-8
- Changing CBL-Mariner ID from "Mariner" to "mariner" to conform to standard.  Also updated Distrib-Description and Name per internal review.

* Tue Aug 18 2020 Jon Slobodzian <joslobo@microsoft.com> - 1.0-7
- Restoring correct Name, Distribution Name, CodeName and ID.

* Fri Jul 31 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.0-6
- Updating distribution name.

* Wed Jul 29 2020 Nick Samson <nisamson@microsoft.com> - 1.0-5
- Updated os-release file and URL to reflect project naming

* Wed Jun 24 2020 Jon Slobodzian <joslobo@microsoft.com> - 1.0-4
- Updated license for 1.0 release.

* Mon May 04 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.0-3
- Providing "system-release(releasever)" for the sake of DNF
- and other package management tools.

* Thu Jan 30 2020 Jon Slobodzian <joslobo@microsoft.com> 1.0-2
- Remove Microsoft name from distro version.

* Wed Sep 04 2019 Mateusz Malisz <mamalisz@microsoft.com> 1.0-1
- Original version for CBL-Mariner.
