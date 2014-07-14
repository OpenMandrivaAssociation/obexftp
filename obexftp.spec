%define major 0
%define mcobex_major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		obexftp
Summary:	Access devices via ObexFTP e.g. Siemens mobile equipment
Version:	0.23
Release:	11
License:	GPLv2+
Group:		Communications
URL:		http://dev.zuckschwerdt.org/openobex/wiki/ObexFtp
Source0:	http://triq.net/obexftp/%{name}-%{version}.tar.bz2
# From Gentoo bug #250210: fix a missing include that breaks build -
# AdamW 2009/01
Patch0:		obexftp-0.22-include.patch
# Fix a string literal error - AdamW 2009/01
Patch1:		obexftp-0.22-literal.patch
Patch2:		obexftp-0.23-ruby1.9.patch
Patch3:		obexftp-0.23-sfmt.patch
Patch4:         obexftp-change-api-new-openobx.patch
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(openobex)
BuildRequires:	python-devel
BuildRequires:	ruby
BuildRequires:	ruby-devel

%description
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n	%{libname}
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(openobex)

%description -n	%{develname}
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%package -n	python-%{name}
Summary:	Python binding for %{name}
Group:		Development/Python
Requires:	python
Requires:	python-devel

%description -n	python-%{name}
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%package -n	ruby-%{name}
Summary:	Ruby binding for %{name}
Group:		Development/Other
Requires:	ruby
Requires:	ruby-devel

%description -n	ruby-%{name}
The overall goal of this project is to make mobile devices featuring 
the OBEX protocol and adhering to the OBEX FTP standard accessible. 
The most common use for ObexFTP is to access your mobile phones memory 
to store and retrieve e.g. your phonebook, logos, ringtones, music, 
pictures and the like.

%prep
%setup -q
%patch0 -p1 -b .include
%patch1 -p1 -b .literal
%patch2 -p1 -b .ruby1.9
%patch3 -p1 -b .sfmt
%patch4 -p1 -b .api

%build
%configure2_5x \
    --disable-tcl \
    --disable-perl

%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/libmulticobex.so.%{mcobex_major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc

%files -n python-%{name}
%{py_platsitedir}/%{name}
%{py_platsitedir}/%{name}-%version-py%{py_ver}.egg-info

%files -n ruby-%{name}
%{ruby_sitearchdir}/%{name}.so


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.23-5mdv2011.0
+ Revision: 666937
- mass rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.23-4mdv2011.0
+ Revision: 523451
- rebuilt for 2010.1

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 0.23-3mdv2010.0
+ Revision: 439983
- rebuild for new libusb

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.23-2mdv2010.0
+ Revision: 426264
- rebuild

* Tue Mar 03 2009 Emmanuel Andry <eandry@mandriva.org> 0.23-1mdv2009.1
+ Revision: 347752
- New version 0.23
- protect majors

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.22-3mdv2009.1
+ Revision: 325208
- bump rel

  + Adam Williamson <awilliamson@mandriva.org>
    - rebuild with python 2.6
    - add literal.patch: fix a string literal error
    - add include.patch: fix a missing include (from Gentoo)

* Mon Jun 16 2008 Funda Wang <fwang@mandriva.org> 0.22-1mdv2009.0
+ Revision: 219366
- New version 0.22 final

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jan 12 2008 Emmanuel Andry <eandry@mandriva.org> 0.22-0.rc10.1mdv2008.1
+ Revision: 149811
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 0.22-0.rc7.1mdv2008.0
+ Revision: 80673
- use Fedora license policy
- drop the patch (merged upstream)
- new pre-release rc7

* Fri Jun 22 2007 Adam Williamson <awilliamson@mandriva.org> 0.22-0.rc4.2mdv2008.0
+ Revision: 42795
- no longer installs anything to puresitedir
- bump for BS
- guessed wrong where the egg-info wound up
- one more fix to python build
- new release 0.22rc4; new patch0 to fix different python install problems

* Wed Jun 20 2007 Adam Williamson <awilliamson@mandriva.org> 0.22-0.rc3.4mdv2008.0
+ Revision: 41656
- correct group
- build and package ruby binding
- build and package ruby binding; add some requires

* Tue Jun 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.22-0.rc3.3mdv2008.0
+ Revision: 41644
- cleaner way to fix the python detection

* Tue Jun 19 2007 Helio Chissini de Castro <helio@mandriva.com> 0.22-0.rc3.2mdv2008.0
+ Revision: 41595
- Since new autotools aren't so friendly, change the patch target..
- Added patch for detect python on lib64

* Tue Jun 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.22-0.rc3.1mdv2008.0
+ Revision: 41564
- new release 0.22rc3; unversioned devel package
- Import obexftp



* Thu Aug 31 2006 Couriousous <couriousous@mandriva.org> 0.20-1mdv2007.0
- 0.20

* Fri Jun 16 2006 Austin Acton <austin@mandriva.org> 0.19-1mdv2007.0
- Rebuild

* Sat Mar 18 2006 Couriousous <couriousous@mandriva.org> 0.19-3mdk
- Really fix python macro

* Fri Mar 17 2006 Couriousous <couriousous@mandriva.org> 0.19-2mdk
- Fix python macro

* Fri Mar 17 2006 Couriousous <couriousous@mandriva.org> 0.19-1mdk
- 0.19

* Tue Dec 28 2004 Couriousous <couriousous@mandrake.org> 0.10.7-2mdk
- fix directory ownership

* Tue Dec 28 2004 Austin Acton <austin@mandrake.org> 0.10.7-1mdk
- based on spec from Marc Koschewski <marc@osknowledge.org>
