%define name klm
%define	version 0.5.0
%define release 2
%define prefix /opt/kde

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: KLM - KDE app to monitor system health sensors
Name: %{name}
Version: %{version}
Release: %{release}
Prefix: %{prefix}
Group: X11/KDE/Apps
Copyright: GPL
Vendor: Brendon Humphrey <brendy@swipnet.se>
Packager: Troy Engel <tengel@sonic.net>
Distribution: none
Source: %{name}-%{version}.tar.bz2
Url: http://www.wantree.com.au/~brendy/sofware.html
BuildRoot: /tmp/build-%{name}-%{version}
Patch: %{name}-%{version}.patch

%description
Klm is a KDE application that can be used to display and configure the
hardware health monitoring sensors that are present in most modern PCs. Klm
uses the lm_sensors kernel module to access these sensors.

%changelog
* Fri Jun 04 1999 Troy Engel <tengel@sonic.net>
  - Updated SPEC a whole bunch
* Sat Feb 13 1999 Brendon Humphrey <brendy@swipnet.se>
  - Updated for klm 0.5.0.
* Thu Jan 21 1999 Bert de Bruijn <bob@ccl.kuleuven.ac.be>
  - first version of the SPEC file. Klm version 0.4.0.

%prep
rm -rf %{builddir}

%setup
%patch -p1
touch `find . -type f`

%build
if [ -z "$KDEDIR" ]; then
	export KDEDIR=%{prefix}
fi
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
make

%install
make install
cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}
rm -f $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}
