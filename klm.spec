Summary:	KLM - KDE app to monitor system health sensors
Name:		klm
Version:	0.5.0
Release:	2
Group:		X11/KDE/Applications
Copyright:	GPL
Vendor:		Brendon Humphrey <brendy@swipnet.se>
Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}-%{version}.patch
URL:		http://www.wantree.com.au/~brendy/sofware.html
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Klm is a KDE application that can be used to display and configure the
hardware health monitoring sensors that are present in most modern PCs. Klm
uses the lm_sensors kernel module to access these sensors.

%prep
%setup -q
%patch -p1

%build
if [ -z "$KDEDIR" ]; then
	export KDEDIR=%{prefix}
fi
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
make

%install
rm -rf $RPM_BUILD_ROOT
make install
cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}
