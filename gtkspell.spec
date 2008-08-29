Summary:	GTK+ Spell Checker Interface Library
Summary(pl.UTF-8):	Biblioteka z interfejsem do narzędzia sprawdzającego pisownię dla GTK+
Name:		gtkspell
Version:	2.0.14
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Libraries
Source0:	http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	da168e9b69e70454ba04d0f1fd82686e
URL:		http://gtkspell.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	docbook-dtd42-xml
BuildRequires:	enchant-devel >= 0.4.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.13.3
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words
in a GtkTextView widget. Right-clicking a misspelled word pops up a
menu of suggested replacements.

%description -l pl.UTF-8
GtkSpell udostępnia podobne do MS Worda lub MacOSX podświetlanie
błędnie napisanych słów w widgecie GtkTextView. Kliknięcie prawym
przyciskiem na błędne słowo otwiera menu z sugerowanymi poprawkami.

%package devel
Summary:	Header files for gtkspell
Summary(pl.UTF-8):	Pliki nagłówkowe dla gtkspella
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	enchant-devel >= 0.4.0
Requires:	gtk+2-devel >= 2:2.10.0

%description devel
Header files for gtkspell.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gtkspella.

%package static
Summary:	Static libraries for gtkspell
Summary(pl.UTF-8):	Biblioteki statyczne dla gtkspella
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libraries for gtkspell.

%description static -l pl.UTF-8
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
%attr(755,root,root) %{_libdir}/libgtkspell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkspell.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkspell.so
%{_libdir}/libgtkspell.la
%{_includedir}/%{name}-2.0
%{_pkgconfigdir}/gtkspell-2.0.pc
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkspell.a
