Summary:	GTK+ Spell Checker Interface Library
Summary(pl):	Biblioteka z interfejsem do narzêdzia sprawdzaj±cego pisowniê dla GTK+
Name:		gtkspell
Version:	2.0.10
Release:	1
Epoch:		1
License:	GPL
Vendor:		Evan Martin <martine@cs.washington.edu>
Group:		X11/Libraries
Source0:	http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	329d5a85a0a1847cb17336115ad94891
URL:		http://gtkspell.sourceforge.net/
BuildRequires:	aspell-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	docbook-dtd42-xml
BuildRequires:	gtk+2-devel >= 1:2.2.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.4.0
BuildRequires:	pkgconfig
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	aspell-devel
Requires:	gtk+2-devel >= 1:2.2.0

%description devel
Header files for gtkspell.

%description devel -l pl
Pliki nag³ówkowe dla gtkspella.

%package static
Summary:	Static libraries for gtkspell
Summary(pl):	Biblioteki statyczne dla gtkspella
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libraries for gtkspell.

%description static -l pl
Biblioteki statyczne dla gtkspella.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}-2.0
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
