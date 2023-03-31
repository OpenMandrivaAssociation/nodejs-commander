Name: nodejs-commander
Version: 9.4.1
Release: 2
Source0: https://github.com/tj/commander.js/archive/refs/tags/v%{version}.tar.gz
Summary: Node.js command line interface library
URL: https://github.com/tj/commander.js
License: MIT
Group: Development/Other
BuildRequires: nodejs
BuildRequires: nodejs-packaging
BuildRequires: rsync
BuildArch: noarch

%description
Node.js command line interface library

%prep
%autosetup -p1 -n commander.js-%{version}

%build

%install
npm -g --omit=dev --prefix=/tmp/INSTROOT.$$%{_prefix} install
# Using rsync to dereference symlinks
rsync -rptgoDLk /tmp/INSTROOT.$$/ %{buildroot}
rm -rf /tmp/INSTROOT.$$

%files
%{nodejs_sitelib}/commander
