Summary:	KLM - KDE app to monitor system health sensors
Name:		klm
Version:	0.5.0
Release:	2
Group:		X11/KDE/Applications
Group(de):	X11/KDE/Applikationen
Group(pl):	X11/KDE/Aplikacje
License:	GPL
Vendor:		Brendon Humphrey <brendy@swipnet.se>
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
