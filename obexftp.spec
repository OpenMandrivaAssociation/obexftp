%define name		obexftp
%define version		0.22
%define beta		rc3
%if %beta
%define release		%mkrel 0.%beta.2
%else
%define release		%mkrel 1
%endif

%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:			%{name}
Version:		%{version}
Release:		%{release}
License:		GPL
%if %beta
Source0:		http://triq.net/obexftp/%name-%version-%beta.tar.bz2
%else
Source0:		http://triq.net/obexftp/%name-%version.tar.bz2
%endif
Patch0:         obexftp-0.22-rc3-python.patch
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

%package -n		%{develname}
Summary:		Headers for developing programs that will use %{name}
Group:			Development/Other
Obsoletes:		%mklibname %name 0 -d
Provides:		%{name}-devel		= %{version}-%{release}
Provides:		lib%{name}-devel	= %{version}-%{release}
Requires:		%{libname}		= %{version}
Requires:		libopenobex-devel

%description -n		%{develname}
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
%if "%{_lib}" != "lib"
%patch0 -p1 -b .lib64python
aclocal && libtoolize -c && autoheader && automake -a -c && autoconf
%endif

%build
%configure \
    --disable-perl \
    --disable-tcl \
    --disable-ruby

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

%files -n %{develname}
%defattr(-,root,root)

%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a

%files -n python-%name
%py_platsitedir/%name
%py_puresitedir/%name
