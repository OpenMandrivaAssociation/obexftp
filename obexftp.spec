%define name		obexftp
%define version		0.22

#release is called uctest, rename it to rc10 for upgrade reason
%define beta		0
%define rel		2
%if %beta
%define release		%mkrel 0.%{beta}.%{rel}
%define distname	%{name}-%{version}-uctest.tar.bz2
%else
%define release		%mkrel %{rel}
%define distname	%{name}-%{version}.tar.bz2
%endif

%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:			%{name}
Summary:		Access devices via ObexFTP e.g. Siemens mobile equipment
Version:		%{version}
Release:		%{release}
License:		GPLv2+
Source0:		http://triq.net/obexftp/%{distname}
# From Gentoo bug #250210: fix a missing include that breaks build -
# AdamW 2009/01
Patch0:			obexftp-0.22-include.patch
# Fix a string literal error - AdamW 2009/01
Patch1:			obexftp-0.22-literal.patch
Group:			Communications
URL:			http://dev.zuckschwerdt.org/openobex/wiki/ObexFtp
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
BuildRequires:		bluez-devel
BuildRequires:		bluez-sdp-devel
BuildRequires:		openobex-devel
BuildRequires:		python-devel
BuildRequires:		ruby
BuildRequires:		ruby-devel

%description
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%package -n		%{libname}
Summary:		Main library for %{name}
Group:			System/Libraries

%description -n		%{libname}
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%package -n		%{develname}
Summary:		Headers for developing programs that will use %{name}
Group:			Development/Other
Obsoletes:		%mklibname %{name} 0 -d
Provides:		%{name}-devel		= %{version}-%{release}
Provides:		lib%{name}-devel	= %{version}-%{release}
Requires:		%{libname}		= %{version}
Requires:		libopenobex-devel

%description -n		%{develname}
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%package -n		python-%{name}
Summary:		Python binding for %{name}
Group:			Development/Python
Requires:		python
Requires:		python-devel

%description -n         python-%{name}
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%package -n		ruby-%{name}
Summary:		Ruby binding for %{name}
Group:			Development/Other
Requires:		ruby
Requires:		ruby-devel

%description -n         ruby-%{name}
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%prep
%setup -q
%patch0 -p1 -b .include
%patch1 -p1 -b .literal

%build

%configure2_5x \
    --disable-tcl \
    --disable-perl

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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
%{_libdir}/pkgconfig/*.pc

%files -n python-%{name}
%defattr(-,root,root)

%{py_platsitedir}/%{name}
%{py_platsitedir}/%{name}-%version-py%{pyver}.egg-info

%files -n ruby-%{name}
%defattr(-,root,root)
%ruby_sitearchdir/%{name}.so
