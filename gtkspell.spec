Summary:	GTK+ Spell Checker Interface Library
Summary(pl):	Biblioteka z interfejsem do narzêdzia sprawdzaj±cego pisowniê dla GTK+
Name:		gtkspell
Version:	2.0.4
Release:	1
Epoch:		1
License:	GPL
Vendor:		Evan Martin <martine@cs.washington.edu>
Group:		X11/Libraries
Source0:	http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	4ded985b8eefdf9ac6fbf79cad69ccbd
URL:		http://gtkspell.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	pspell-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words
in a GtkTextView widget. Right-clicking a misspelled word pops up a
menu of suggested replacements.

%description -l pl
GtkSpell udostêpnia podobne do MS Worda lub MacOSX pod¶wietlanie
b³êdnie napisanych s³ów w widgecie GtkTextView. Klikniêcie prawym
przyciskiem na b³êdne s³owo otwiera menu z sugerowanymi poprawkami.

%package devel
Summary:	Header files for gtkspell
Summary(pl):	Pliki nag³ówkowe dla gtkspella
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Header files for gtkspell.

%description devel -l pl
Pliki nag³ówkowe dla gtkspella.

%package static
Summary:	Static libraries for gtkspell
Summary(pl):	Biblioteki statyczne dla gtkspella
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static libraries for gtkspell.

%description static -l pl
Biblioteki statyczne dla gtkspella.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
/usr/share/gtk-doc/*/%{name}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
