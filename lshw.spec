%define name lshw
%define version 2.15
%define realversion B.0%{version}
%define release %mkrel 2

Summary: A hardware lister
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ezix.sourceforge.net/software/files/%{name}-%{realversion}.tar.gz
License: GPLv2
Group: System/Kernel and hardware
Url: http://ezix.sourceforge.net/software/lshw.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: ldetect-lst >= 0.1.282
BuildRequires: sqlite3-devel

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
rm -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}
make PREFIX=%_prefix SBINDIR=%_sbindir MANDIR=%_mandir DESTDIR=%{buildroot} install-gui

# packaged as part of ldetect-lst
rm -f %{buildroot}%{_datadir}/lshw/{oui.txt,*.ids}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_sbindir}/lshw
%dir %{_datadir}/lshw
%{_datadir}/lshw/*.txt
%attr(644,root,root) %{_mandir}/man1/lshw.*

%files gui
%defattr(-,root,root)
%doc COPYING
%{_sbindir}/gtk-lshw
%{_datadir}/lshw/artwork


