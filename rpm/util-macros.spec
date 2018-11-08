Name:       util-macros
Summary:    X.org macros utilities
Version:    1.19.2
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://dri.sourceforge.net
Source0:    http://dri.freedesktop.org/libdrm/%{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig

%description
%{summary}


%prep
%setup -q -n %{name}-%{version}/upstream

%build
unset LD_AS_NEEDED

%reconfigure --disable-static \
    --enable-omap-experimental-api

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/util-macros
%{_datadir}/aclocal
%{_datadir}/pkgconfig
