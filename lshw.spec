%define name lshw
%define version 2.16
%define realversion B.0%{version}
%define release 1

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


%changelog
* Wed Jan 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.16-1mdv2012.0
+ Revision: 760149
- new version 2.16

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.15-2
+ Revision: 666099
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.15-1mdv2011.0
+ Revision: 606689
- fix deps and file list
- B.02.15
- rebuild

* Fri Jan 08 2010 Frederic Crozat <fcrozat@mandriva.com> 2.14-3mdv2010.1
+ Revision: 487695
- ids file and oui.txt are now in ldetect-lst

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.14-2mdv2010.0
+ Revision: 426011
- rebuild

* Mon Feb 16 2009 Erwan Velu <erwan@mandriva.org> 2.14-1mdv2009.1
+ Revision: 340775
- Removing patch0 (upstream)
- 2.14

* Mon Aug 18 2008 Emmanuel Andry <eandry@mandriva.org> 2.13-2mdv2009.0
+ Revision: 273415
- fix gcc4.3 build with P0 from gentoo

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Sun May 11 2008 Frederik Himpe <fhimpe@mandriva.org> 2.13-1mdv2009.0
+ Revision: 205945
- New version, remove patch integrated upstream
- Adapt to new license policy

* Mon Mar 10 2008 Olivier Blin <blino@mandriva.org> 2.12.01-2mdv2008.1
+ Revision: 183678
- fix hang in PCI capabilities read (#36696, upstream ticket 340)
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 Erwan Velu <erwan@mandriva.org> 2.12.01-1mdv2008.1
+ Revision: 111046
- Adding source
- 2.12.01

* Tue Aug 21 2007 Erwan Velu <erwan@mandriva.org> 2.11.01-1mdv2008.0
+ Revision: 68450
- 2.11

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

* Mon Apr 23 2007 Erwan Velu <erwan@mandriva.org> 2.10-1mdv2008.0
+ Revision: 17461
- 2.10


* Mon Jan 15 2007 Erwan Velu <erwan@mandriva.org> 2.09-1mdv2007.0
+ Revision: 109237
- 2.09
- Import lshw

* Fri Jun 23 2006 Erwan Velu <erwan@seanodes.com> 2.08-1mdk
- 2.08

* Thu Mar 16 2006 Erwan Velu <erwan@seanodes.com> 2.07-2mdk
- Oups, fixing some rights

* Thu Mar 16 2006 Erwan Velu <erwan@seanodes.com> 2.07-1mdk
- 2.0.7

* Fri Oct 21 2005 Erwan Velu <erwan@seanodes.com> 2.06-1mdk
- 2.06

* Sat Aug 27 2005 Pixel <pixel@mandriva.com> 2.05-2mdk
- .svg files are not the text version (are they used by the gui?)

* Sat Jul 23 2005 Erwan Velu <velu@seanodes.com> 2.05-1mdk
- 2.05

* Thu May 12 2005 Erwan Velu <velu@seanodes.com> 2.04-1mdk
- 2.04

* Sun Feb 13 2005 Erwan Velu <velu@seanodes.com> 2.03-2mdk
- REbuild

* Sat Feb 05 2005 Erwan Velu <velu@seanodes.com> 2.03-1mdk
- 2.03

* Fri Jan 21 2005 Erwan Velu <velu@seanodes.com> 2.02-1mdk
- 2.02

* Wed Jan 05 2005 Erwan Velu <velu@seanodes.com> 2.00-1mdk
- Happy new year
- 2.00 \o/
- Adding gui

* Sun Dec 19 2004 Erwan Velu <velu@seanodes.com> 1.09-1mdk
- 1.09

* Wed Sep 15 2004 Erwan Velu <erwan@mandrakesoft.com> 1.08-1mdk
- 1.08
- Removing patches 0 & 1

* Fri Aug 20 2004 Erwan Velu <erwan@mandrakesoft.com> 1.07-6mdk
- Bzipping cpuinfos
- Adding dmi patch (now supporting chassis informations)

* Sat Jun 05 2004 <lmontel@mandrakesoft.com> 1.07-5mdk
- Rebuild

* Fri Jun 04 2004 Erwan Velu <erwan@mandrakesoft.com> 1.07-4mdk
- Adding patch for reading physical id & sibling on /proc/cpuinfo

* Wed May 19 2004 Robert Vojta <robert.vojta@mandrake.org> 1.07-3mdk
- ChangeLog entry fixed (1.0.7 -> 1.07)

* Wed May 19 2004 Robert Vojta <robert.vojta@mandrake.org> 1.07-2mdk
- Summary fix (#9793)

* Sat May 15 2004 Erwan Velu <erwan@mandrakesoft.com> 1.07-1mdk
- 1.07

* Wed Apr 21 2004 Erwan Velu <erwan@mandrakesoft.com> 1.06-1mdk
- 1.06

* Wed Feb 18 2004 Erwan Velu <erwan@mandrakesoft.com> 1.05-1mdk
- Initial mdk release

