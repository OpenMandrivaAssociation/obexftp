%define major 0
%define mcobex_major 1
%define libname %mklibname %{name} %{major}
%define libbfb %mklibname bfb %{major}
%define libmulticobex %mklibname multicobex %{mcobex_major}
%define devname %mklibname %{name} -d

Summary:	Access devices via ObexFTP e.g. Siemens mobile equipment
Name:		obexftp
Version:	0.24
Release:	6
License:	GPLv2+
Group:		Communications
Url:		https://dev.zuckschwerdt.org/openobex/wiki/ObexFtp
Source0:	http://triq.net/obexftp/%{name}-%{version}-Source.tar.gz
Patch1:		obexftp-0.24-link.patch
Patch2:		obexftp-0.24-fix-absurd-install-path.patch
Patch3:		obexftp-pkgconfig_requires.patch
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(openobex)
BuildRequires:	pkgconfig(python3)
BuildRequires:	xmlto
BuildRequires:	cmake
BuilDrequires:	asciidoc
BuildRequires:	swig

%description
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%files
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%{_bindir}/*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains a shared library for %{name}.

%files -n %{libname}
%{_libdir}/libobexftp.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libbfb}
Summary:	Main library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}obexftp0 < 0.23-10

%description -n %{libbfb}
This package contains a shared library for %{name}.

%files -n %{libbfb}
%{_libdir}/libbfb.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libmulticobex}
Summary:	Main library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}obexftp0 < 0.23-10

%description -n %{libmulticobex}
This package contains a shared library for %{name}.

%files -n %{libmulticobex}
%{_libdir}/libmulticobex.so.%{mcobex_major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{libbfb} = %{EVRD}
Requires:	%{libmulticobex} = %{EVRD}

%description -n %{devname}
This package includes the development files for %{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%package -n python-%{name}
Summary:	Python binding for %{name}
Group:		Development/Python

%description -n python-%{name}
This package contains the python bindings for %{name}.

%files -n python-%{name}
%{py_platsitedir}/*

#----------------------------------------------------------------------------

%package -n ruby-%{name}
Summary:	Ruby binding for %{name}
Group:		Development/Other

%description -n ruby-%{name}
This package contains the ruby bindings for %{name}.

%files -n ruby-%{name}
%{ruby_vendorarchdir}/%{name}.so

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}-Source
%autopatch -p1

%build
%cmake -DENABLE_PERL=OFF -DENABLE_TCL=OFF
%make all doc

%install
pushd build
%makeinstall_std

