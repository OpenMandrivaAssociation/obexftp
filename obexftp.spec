%define __libtoolize /bin/true
%define __cputoolize /bin/true

%define name		obexftp
%define version		0.20
%define release		%mkrel 1

%define major		0
%define libname		%mklibname %{name} %{major}

Name:			%{name}
Version:		%{version}
Release:		%{release}
License:		GPL
Source0:		http://triq.net/obexftp/%name-%version.tar.bz2
Group:			Communications
URL:			http://triq.net/obex/
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
Summary:		Access devices via ObexFTP e.g. Siemens mobile equipment
BuildRequires:		bluez-devel bluez-sdp-devel openobex-devel python-devel

%description
The overall goal of this project is to make mobile devices featuring the OBEX
protocol and adhering to the OBEX FTP standard accessible by an open source
implementation. The common usage for ObexFTP is to access your mobile phones
memory to store and retrieve e.g. your phonebook, logos, ringtones, music,
pictures and alike

%package -n		%{libname}
Summary:		Main library for %{name}
Group:			System/Libraries

%description -n		%{libname}
The overall goal of this project is to make mobile devices featuring the OBEX
protocol and adhering to the OBEX FTP standard accessible by an open source
implementation. The common usage for ObexFTP is to access your mobile phones
memory to store and retrieve e.g. your phonebook, logos, ringtones, music,
pictures and alike

%package -n		%{libname}-devel
Summary:		Headers for developing programs that will use %{name}
Group:			Development/Other
Provides:		%{name}-devel		= %{version}-%{release}
Provides:		lib%{name}-devel	= %{version}-%{release}
Requires:		%{libname}		= %{version}
Requires:		libopenobex-devel

%description -n		%{libname}-devel
The overall goal of this project is to make mobile devices featuring the OBEX
protocol and adhering to the OBEX FTP standard accessible by an open source
implementation. The common usage for ObexFTP is to access your mobile phones
memory to store and retrieve e.g. your phonebook, logos, ringtones, music,
pictures and alike

%package -n		python-%name
Summary:		Python binding for obexftp
Group:			Development/Python

%description -n         python-%name
Python binding for obexftp

%prep
%setup -q

%build
%configure2_5x --disable-perl --disable-tcl
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)

%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a

%files -n python-%name
%py_platsitedir/%name
%py_puresitedir/%name
