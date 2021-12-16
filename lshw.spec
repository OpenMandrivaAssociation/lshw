%define realversion B.0%{version}
%define _disable_lto 1

Summary:	A hardware lister
Name:		lshw
Version:	2.19.2
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://ezix.org/project/wiki/HardwareLiSter
Source0:	https://www.ezix.org/software/files/lshw-%{realversion}.tar.gz
Patch1:		lshw-B.02.18-scandir.patch
#Patch2:		lshw-B.02.18-20cda77.patch

BuildRequires:	cmake
BuildRequires:	gettext
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	ninja
BuildRequires:	pkgconfig(python3)
Requires:	hwdata >= 0.314

%description
lshw (Hardware Lister) is a tool to provide detailed information 
on the hardware configuration of the machine.

%package gui
Summary:	HardWare LiSter (GUI version)
Group:		System/Kernel and hardware
Requires:	%{name} = %{EVRD}
Requires:	gtk+2.0
Requires:	polkit

%description gui
This package provides a graphical user interface to lshw

%prep
%setup -qn %{name}-%{realversion}
%autopatch -p1

# Ugly since 2.07 default rights are messed
find -type f | xargs chmod 644
find -type d | xargs chmod 755

%cmake -DNOLOGO=ON -DHWDATA=OFF -DPOLICYKIT=ON -DBUILD_SHARED_LIBS=OFF  -GNinja

%build
pushd build
%ninja_build

%install
pushd build
%ninja_install

ln -s gtk-lshw %{buildroot}%{_sbindir}/lshw-gui

# packaged as part of ldetect-lst
rm -f %{buildroot}%{_datadir}/lshw/{oui.txt,*.ids}

# translations seems borken, remove for now
#find_lang %{name}
rm -rf %{buildroot}%{_datadir}/locale/fr/

%files
%license COPYING
%doc README.md
%{_sbindir}/lshw
%{_mandir}/man1/lshw.1*

%files gui
%doc COPYING
%{_bindir}/lshw-gui
%{_sbindir}/gtk-lshw
%{_sbindir}/lshw-gui
%dir %{_datadir}/lshw
%{_datadir}/lshw/artwork
%{_datadir}/appdata/gtk-lshw.appdata.xml
%dir %{_datadir}/lshw/ui
%{_datadir}/lshw/ui/gtk-lshw.ui
%{_datadir}/pixmaps/gtk-lshw.svg
%{_datadir}/applications/gtk-lshw.desktop
%{_datadir}/polkit-1/actions/org.ezix.lshw.gui.policy
