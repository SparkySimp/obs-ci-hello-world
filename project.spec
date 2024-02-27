Name:           hello-world
Version:        1.0
Release:        1
Summary:        A simple "Hello World" program
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/SparkySimp/obs-ci-hello-world
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake gcc clang

%description
This package provides a simple "Hello World" program written in C.

%prep
%setup -q

%build
cmake .
make

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 hello %{buildroot}/usr/bin

%files
/usr/bin/hello

%changelog
