Summary:	KLM - KDE app to monitor system health sensors
Summary(pl.UTF-8):	KLM - aplikacja KDE do monitorowania sensorów
Name:		klm
Version:	0.5.0
Release:	2
License:	GPL
Vendor:		Brendon Humphrey <brendy@swipnet.se>
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/unstable/apps/KDE1.x/utils/%{name}-%{version}.tar.gz
# Source0-md5:	50dc0236d7efb166d831f6f713ee23d0
Patch0:		%{name}-%{version}.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Klm is a KDE application that can be used to display and configure the
hardware health monitoring sensors that are present in most modern
PCs. Klm uses the lm_sensors kernel module to access these sensors.

%description -l pl.UTF-8
Klm jest aplikacją KDE, która może być używana do wyświetlania stanu i
konfigurowania sensorów monitorujących stan sprzętu obecnych w
większości współczesnych PC. Klm do komunikacji z sensorami używa
modułów jądra lm_sensors.

%prep
%setup -q
%patch0 -p1

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
