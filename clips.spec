%define	name	clips 
%define	version	6.21
%define	release	%mkrel 5

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
Patch0:		clips-setup.patch.bz2
Patch1:		clips-6.21-lib64.patch.bz2
#Patch2:	clips-Xaw3d.patch.bz2
Patch3:         clips-6.21-gcc4.patch.bz2
BuildRequires:	termcap-devel XFree86 XFree86-devel
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
#%patch2 -p0 -b .Xaw3d
%patch3 -p1 -b .gcc4
bzcat %SOURCE2 > clipssrc/makefile
#(peroyvind) invalid flag for C, drop it to avoid lots of warning
perl -pi -e "s#-Woverloaded-virtual ##g" clipssrc/makefile

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
 
