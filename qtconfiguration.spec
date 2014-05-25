%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Settings API with change notifications for Qt
Name:		qtconfiguration
Version:	0.2.1
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		https://github.com/mauios/qtconfiguration
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
Source1:	qtconfiguration.rpmlintrc
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(dconf)

%track
prog %{name} = {
	url = http://downloads.sourceforge.net/project/mauios/hawaii/qtconfiguration
	regex = "%{name}-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Settings API with change notifications for Qt.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
Library for settings API with change notifications for Qt.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{libname}
Development files and headers for %{name}.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libqtconfiguration.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/QtConfiguration
%dir %{_libdir}/cmake/QtConfiguration
%{_includedir}/QtConfiguration/QConfiguration
%{_includedir}/QtConfiguration/QConfigurationBackend
%{_includedir}/QtConfiguration/*.h
%{_libdir}/cmake/QtConfiguration/*.cmake
%{_libdir}/libqtconfiguration.so

