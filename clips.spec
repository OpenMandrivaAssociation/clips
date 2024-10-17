Summary:	Clips language for expert systems
Name:		clips
Version:	6.21
Release:	15
License:	BSD
Group:		Development/Other
Url:		https://www.ghg.net/clips/download/source/
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
Patch3:		clips-6.21-gcc4.patch
Patch4:		clips-6.21-link.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xt)

%description
This is the Clips expert systems language.

%files
%{_bindir}/clips
%{_docdir}/clips-%{version}
%{_datadir}/clips

#----------------------------------------------------------------------------

%package	X11
Summary:	X interface to Clips
Group:		Development/Other
Requires:	clips

%description	X11
X interface to Clips.

%files X11
%{_prefix}/X11R6/bin/xclips
%doc clips.hlp

#----------------------------------------------------------------------------

%prep
%setup -q -a 1 -c
mv x-prjct/makefile/makefile.x clipssrc
mv x-prjct/xinterface/* clipssrc
%patch0 -p0 -b .setup
%patch1 -p1 -b .lib64
%patch3 -p1 -b .gcc4
bzcat %{SOURCE2} > clipssrc/makefile
%patch4 -p0 -b .link
#(peroyvind) invalid flag for C, drop it to avoid lots of warning
perl -pi -e "s#-Woverloaded-virtual ##g" clipssrc/makefile
perl -pi -e "s#gcc #gcc %{optflags} %{ldflags} #g" clipssrc/makefile*

%build
pushd clipssrc
%make
%make -f makefile.x LIB=%{_lib}
popd

%install
mkdir -p -m 0755 %{buildroot}%{_prefix}/{X11R6/bin,bin,doc,share/clips}
install -m 0755 clipssrc/clips %{buildroot}%{_prefix}/bin/
install -m 0755 clipssrc/xclips %{buildroot}%{_prefix}/X11R6/bin/
install -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/clips/
cp %{SOURCE3} .
mkdir -p %{buildroot}%{_docdir}/clips-%{version}
for i in %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9}; do
install -m 0644 $i %{buildroot}%{_docdir}/clips-%{version}
done

