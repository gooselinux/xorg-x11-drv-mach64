%define tarball xf86-video-mach64
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:    Xorg X11 mach64 video driver
Name:	    xorg-x11-drv-mach64
Version:    6.8.2
Release:    1.1%{?dist}
URL:	    http://www.x.org
License:    MIT
Group:	    User Interface/X Hardware Support
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:    http://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:    mach64.xinf

Patch0:	    mach64-6.8.1-defaultdepth.patch

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.4.99.1
BuildRequires: mesa-libGL-devel >= 6.4-4
BuildRequires: libdrm-devel >= 2.0-1
BuildRequires: automake autoconf libtool pkgconfig
BuildRequires: xorg-x11-util-macros >= 1.1.5

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.4.99.1

%description 
X.Org X11 mach64 video driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch0 -p1 -b .defaultdepth

%build
# aclocal ; automake -a ; autoconf
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.ati
%{driverdir}/mach64_drv.so
%{_datadir}/hwdata/videoaliases/mach64.xinf
#{_mandir}/man4/mach64.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 6.8.2-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 6.8.2-1
- mach64 6.8.2

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> 6.8.1-1
- mach64 6.8.1
- mach64-6.8.1-defaultdepth.patch: Default to depth 16 (#472687)

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 6.8.0-3.1
- ABI bump

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 6.8.0-2
- update for latest server API

* Mon Aug 04 2008 Adam Jackson <ajax@redhat.com> 6.8.0-1
- Initial build of separate mach64 driver.

