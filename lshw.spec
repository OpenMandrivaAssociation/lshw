%define realversion B.0%{version}

%bcond_without gui

Summary:	A hardware lister
Name:		lshw
Version:	2.20
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
Url:		https://ezix.org/project/wiki/HardwareLiSter
Source0:	https://www.ezix.org/software/files/%{name}-%{realversion}.tar.gz
Source1:	https://salsa.debian.org/openstack-team/third-party/lshw/raw/debian/stein/debian/patches/lshw-gtk.1
Patch1:		lshw-B.02.18-scandir.patch
Patch4:		lshw-B.02.20-cmake.patch
BuildRequires:	cmake
BuildRequires:	gettext
BuildRequires:	ninja
%if %{with gui}
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(appstream-glib)
%endif
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(sqlite)

Requires:	hwdata >= 0.314

%description
lshw (Hardware Lister) is a tool to provide detailed information 
on the hardware configuration of the machine.

%files
%license COPYING
%doc README.md
%{_bindir}/lshw
%{_mandir}/man1/lshw.1*

#----------------------------------------------------------------------

%if %{with gui}
%package gui
Summary:	HardWare LiSter (GUI version)
Group:		System/Kernel and hardware
#Requires:	%{name} = %{EVRD}
#Requires:	gtk+3.0
Requires:	polkit

%description gui
This package provides a graphical user interface to lshw

%files gui
%doc COPYING
%{_bindir}/lshw-gui
%{_bindir}/gtk-lshw
%dir %{_datadir}/lshw
%{_datadir}/lshw/artwork
%dir %{_datadir}/lshw/ui
%{_datadir}/lshw/ui/gtk-lshw.ui
%{_datadir}/pixmaps/gtk-lshw.svg
%{_datadir}/applications/gtk-lshw.desktop
%{_datadir}/appdata/gtk-lshw.appdata.xml
%{_datadir}/polkit-1/actions/org.ezix.lshw.gui.policy
%{_mandir}/man1/lshw-gui.1*
%endif

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{realversion}

# fix sbin path
sed -i -e 's,DESTINATION sbin,DESTINATION bin,g' \
	src/CMakeLists.txt \
	src/gui/CMakeLists.txt

%build
%cmake \
	-DCMAKE_INSTALL_FULL_SBINDIR:PATH=%{_bindir} \
	-DNOLOGO:BOOL=ON \
	-DHWDATA:BOOL=OFF \
	-DPOLICYKIT:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DGUI:BOOL=%{?with_gui:ON}%{!?with_gui:OFF} \
	-GNinja
%ninja_build

%install
%ninja_install -C build

# packaged as part of ldetect-lst
#rm -f %{buildroot}%{_datadir}/lshw/{oui.txt,*.ids}

%if %{with gui}
# man page
install -pm 0644 -D %{SOURCE1} %{buildroot}%{_mandir}/man1/lshw-gui.1

# translations seems borken, remove for now
#find_lang %{name}-gui
rm -rf %{buildroot}%{_datadir}/locale/*/
%endif

