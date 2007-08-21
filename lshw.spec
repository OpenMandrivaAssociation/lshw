%define name lshw
%define version 2.11.01
%define realversion B.0%{version}
%define release %mkrel 1

Summary: A hardware lister
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ezix.sourceforge.net/software/files/%{name}-%{realversion}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://ezix.sourceforge.net/software/lshw.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
lshw (Hardware Lister) is a tool to provide detailed information 
on the hardware configuration of the machine.

%package gui
Summary: HardWare LiSter (GUI version)
Group:  System/Kernel and hardware
Requires: %{name}
Requires: gtk2
BuildRequires: gtk2-devel
%description gui
This package provides a graphical user interface to lshw

%prep
%setup -q -n %{name}-%{realversion}
# Ugly since 2.07 default rights are messed
find -type f | xargs chmod 644
find -type d | xargs chmod 755

%build
make
make gui

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=$RPM_BUILD_ROOT
make PREFIX=%_prefix SBINDIR=%_sbindir MANDIR=%_mandir DESTDIR=$RPM_BUILD_ROOT install-gui

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/lshw
%dir %{_datadir}/lshw
%{_datadir}/lshw/*.txt
%{_datadir}/lshw/*.ids
%attr(644,root,root) %{_mandir}/man1/lshw.*

%files gui
%defattr(-,root,root)
%doc COPYING
%{_sbindir}/gtk-lshw
%{_datadir}/lshw/artwork


