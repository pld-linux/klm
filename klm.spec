Summary:	KLM - KDE app to monitor system health sensors
Summary(pl):	KLM - aplikacja KDE do monitorowania sensorów
Name:		klm
Version:	0.5.0
Release:	2
License:	GPL
Vendor:		Brendon Humphrey <brendy@swipnet.se>
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/unstable/apps/utils/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}.patch
URL:		http://www.wantree.com.au/~brendy/sofware.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Klm is a KDE application that can be used to display and configure the
hardware health monitoring sensors that are present in most modern
PCs. Klm uses the lm_sensors kernel module to access these sensors.

%description -l pl
Klm jest aplikacj± KDE, która mo¿e byæ u¿ywana do wy¶wietlania stanu i
konfigurowania sensorów monitoruj±cych stan sprzêtu obecnych w
wiêkszo¶ci wspó³czesnych PC. Klm do komunikacji z sensorami u¿ywa
modu³ów j±dra lm_sensors.

%prep
%setup -q
%patch -p1

%build
if [ -z "$KDEDIR" ]; then
	KDEDIR=%{_prefix} ; export KDEDIR
fi
CXXFLAGS="%{rpmcflags}" CFLAGS="%{rpmcflags}" ./configure \
	--prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install
cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}
%defattr(644,root,root,755)
