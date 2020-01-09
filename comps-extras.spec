Summary: Images for package groups
Name: comps-extras
Version: 7
Release: 2%{?dist}
URL: http://git.fedorahosted.org/git/?p=comps-extras.git;a=summary
Source0: http://fedorahosted.org/releases/c/o/comps-extras/%{name}-%{version}.tar.gz
Epoch: 1
# while GPL isn't normal for images, it is the case here
# No version specified.
# KDE logo is LGPLv2+
# Ruby logos is CC-BY-SA
# See COPYING for more details
License: GPL+ and LGPLv2+ and CC-BY-SA
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
This package contains images for the components included in this distribution.

%prep
%setup -q

%build
# nothing to do

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc comps.dtd comps-cleanup.xsl
%dir %{_datadir}/pixmaps/comps
%{_datadir}/pixmaps/comps/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:7-2
- Mass rebuild 2013-12-27

* Tue Oct 29 2013 Bill Nottingham <notting@redhat.com> - 7-1
- new version for EL 7 (#983163, #1024325)
