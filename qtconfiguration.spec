Summary:	Settings API with change notifications for Qt
Name:		qtconfiguration
Version:	0.2.1
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/Other
URL:		https://github.com/mauios/qtaconfiguration
Source0:	http://downloads.sourceforge.net/project/mauios/hawaii/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt5)

%track
prog %{name} = {
	url = http://downloads.sourceforge.net/project/mauios/hawaii/qtaconfiguration
	regex = "%{name}-(__VER__)\.tar\.gz"
	version = %{version}
}

%description
Settings API with change notifications for Qt.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files