Summary:	Ini-File Handling
Name:		c-ini
Version:	1.1.0
Release:	1
License:	Apache 2.0 or LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/c-util/c-ini/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	87e8140b88b2382dd59dcbf2075e350c
URL:		https://c-util.github.io/c-ini/
BuildRequires:	c-list-devel >= 3
BuildRequires:	c-rbtree-devel >= 3
BuildRequires:	c-stdaux-devel >= 1.5.0
BuildRequires:	c-utf8-devel
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
Requires:	c-rbtree >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The c-ini project implements APIs to deal with ini-files. Different
formats can be supported, but all share common ini-file properties,
mainly that they are human-readable, grouped key-value pairs.

%package devel
Summary:	Header files for c-ini library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for c-ini library.

%package static
Summary:	Static c-ini library
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static c-ini library.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS.md README.md
%attr(755,root,root) %{_libdir}/libcini-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcini-1.so
%{_includedir}/c-ini.h
%{_pkgconfigdir}/libcini-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcini-1.a
