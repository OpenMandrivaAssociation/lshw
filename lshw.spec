%define name lshw
%define version 2.16
%define realversion B.0%{version}
%define release %mkrel 1

Summary: A hardware lister
Name: %{name}
Version: %{version}
Release: %{release}
# To get sources tarball use command
# svn co http://ezix.org/source/packages/lshw/releases/%{realversion} %{name}-%{realversion} && tar -czf %{name}-%{realversion}.tar.gz --exclude .svn %{name}-%{realversion}
Source0: %{name}-%{realversion}.tar.gz
License: GPLv2
Group: System/Kernel and hardware
Url: http://ezix.org/project/wiki/HardwareLiSter
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
%makeinstall_std
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
%{_datadir}/lshw/ui/gtk-lshw.ui
