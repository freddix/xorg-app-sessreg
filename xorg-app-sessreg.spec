Summary:	sessreg application
Name:		xorg-app-sessreg
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/sessreg-%{version}.tar.bz2
# Source0-md5:	e238c89dabc566e1835e1ecb61b605b9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	sed
BuildRequires:	xorg-proto
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sessreg application.

%prep
%setup -qn sessreg-%{version}

# xproto is sufficient
sed -i -e 's/ x11/ xproto/' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/sessreg
%{_mandir}/man1/sessreg.1x*

