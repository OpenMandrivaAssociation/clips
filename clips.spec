%define	name	clips 
%define	version	6.21
%define	release	%mkrel 10

Summary:	Clips language for expert systems
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD style
Group:		Development/Other
Url:		http://www.ghg.net/clips/download/source/
Source0:	http://www.ghg.net/clips/download/source/clipssrc.tar.bz2
Source1:	http://www.ghg.net/clips/download/source/x-prjct.tar.bz2
Source2:	http://www.ghg.net/clips/download/source/makefile.bz2
Source3:	http://www.ghg.net/clips/download/source/clips.hlp
Source4:	http://www.ghg.net/clips/download/documentation/abstract.pdf
Source5:	http://www.ghg.net/clips/download/documentation/apg.pdf
Source6:	http://www.ghg.net/clips/download/documentation/arch5-1.pdf
Source7:	http://www.ghg.net/clips/download/documentation/bpg.pdf
Source8:	http://www.ghg.net/clips/download/documentation/ig.pdf
Source9:	http://www.ghg.net/clips/download/documentation/usrguide.pdf
Patch0:		clips-setup.patch
Patch1:		clips-6.21-lib64.patch
Patch3:         clips-6.21-gcc4.patch
Patch4:		clips-6.21-link.patch
BuildRequires:	libx11-devel
BuildRequires:	libxaw-devel
BuildRequires:	libxt-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%package	X11
Summary:	X interface to Clips
Group:		Development/Other
Requires:	clips

%description
This is the Clips expert systems language.

%description	X11
X interface to Clips.

%prep
%setup -q -a 1 -c
mv x-prjct/makefile/makefile.x clipssrc
mv x-prjct/xinterface/* clipssrc
%patch0 -p0 -b .setup
%patch1 -p1 -b .lib64
%patch3 -p1 -b .gcc4
bzcat %SOURCE2 > clipssrc/makefile
%patch4 -p0 -b .link
#(peroyvind) invalid flag for C, drop it to avoid lots of warning
perl -pi -e "s#-Woverloaded-virtual ##g" clipssrc/makefile
perl -pi -e "s#gcc #gcc %optflags %ldflags #g" clipssrc/makefile*

%build
pushd clipssrc 
%make
%make -f makefile.x LIB=%{_lib}
popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 0755 $RPM_BUILD_ROOT%{_prefix}/{X11R6/bin,bin,doc,share/clips}
install -m 0755 -s clipssrc/clips $RPM_BUILD_ROOT%{_prefix}/bin/
install -m 0755 -s clipssrc/xclips $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/
install -m 0644 %SOURCE3 $RPM_BUILD_ROOT%{_datadir}/clips/
cp %SOURCE3 .
mkdir -p $RPM_BUILD_ROOT%{_docdir}/clips-%PACKAGE_VERSION
for i in %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9; do
install -m 0644 $i $RPM_BUILD_ROOT%{_docdir}/clips-%PACKAGE_VERSION
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root) %{_bindir}/clips
%attr(-,root,root) %{_docdir}/clips-%PACKAGE_VERSION
%attr(-,root,root) %{_datadir}/clips

%files X11
%attr(-,root,root) %{_prefix}/X11R6/bin/xclips
%attr(-,root,root) %doc clips.hlp
 


%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 6.21-10mdv2011.0
+ Revision: 635042
- rebuild
- bunzip2 the patches

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 6.21-9mdv2011.0
+ Revision: 617041
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 6.21-8mdv2010.0
+ Revision: 437057
- rebuild

* Wed Apr 01 2009 Funda Wang <fwang@mandriva.org> 6.21-7mdv2009.1
+ Revision: 363123
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 6.21-7mdv2009.0
+ Revision: 243529
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 6.21-5mdv2008.1
+ Revision: 123226
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import clips


* Sat Jul 30 2005 Nicolas Lécureuil <neoclust@mandriva.org>  6.21-5mdk
- Remove Packager tag
- Patch 3 : Fix build with Gcc4

* Sun Jan 23 2005 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 6.21-4mdk
- rebuild
- get rid of compile warnings

* Thu Nov 06 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 6.21-3mdk
- don't rm -rf $RPM_BUILD_ROOT in %%prep
- drop P2, do _NOT_ link against Xaw3d, makes xclips segfault, link against Xaw in stead
- cosmetics

* Fri Sep 26 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 6.21-2mdk
- lib64 fixes

* Fri Jul 11 2003 Per Ã˜yvind Karlsen <peroyvind@sintrax.net> 6.21-1mdk
- 6.21
- bzip2 sources
- regenerated P0 & P2
- dropped P1 (merged upstream)

* Tue Jan 22 2002 Stefan van der Eijk <stefan@eijk.nu> 6.10-6mdk
- replaced "make -j2" with "%%make"
- BuildRequires

* Wed Oct 17 2001 Daouda LO <daouda@mandrakesoft.com> 6.10-5mdk
- spec cleanup
- rpmlint compliant

* Mon Oct 08 2001 Stefan van der Eijk <stefan@eijk.nu> 6.10-4mdk
- BuildRequires: ncompress

* Sat Jul 07 2001 Stefan van der Eijk <stefan@eijk.nu> 6.10-3mdk
- BuildRequires:	libtermcap-devel
- BuildRequires:	Xaw3d-devel
- BuildRequires:	XFree86-devel

* Fri Jul  6 2001 Daouda LO <daouda@mandrakesoft.com> 6.10-2mdk
- s|Linux-Mandrake|Mandrake Linux|
- s|Copyright|License|

* Tue Nov 21 2000 Daouda Lo <daouda@mandrakesoft.com> 6.10-1mdk
- fisrt mdk package .
- add packager tag .
