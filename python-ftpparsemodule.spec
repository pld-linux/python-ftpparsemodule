%define 	module	ftpparsemodule

Summary:	Python package providing parse FTP LIST command
Summary(pl.UTF-8):	Pakiet Pythona do analizy polecenia FTP LIST
Name:		python-%{module}
Version:	0.93
Release:	4
License:	BSD
Group:		Development/Languages/Python
Source0:	http://c0re.23.nu/c0de/ftpparsemodule/ftpparsemodule-%{version}.tar.gz
# Source0-md5:	05735a02d74554f8895e9faf5e3b15d5
Patch0:		%{module}-gcc.patch
URL:		http://c0re.23.nu/c0de/ftpparsemodule/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTP-Servers provide a wide range of responses to the LIST command.
ftpparsemodule allows you to parse most FTP-servers LIST responses
found in the wild. It does so by using Dan Bernstein's ftpparse
package and making it accessible to Python.

%description -l pl.UTF-8
Serwery FTP dostarczają dużego rozrzutu odpowiedzi na polecenie LIST.
ftpparsemodule pozwala przeanalizować odpowiedzi na LIST pochodzące od
większości serwerów FTP istniejących na świecie. Robi to przy użyciu
pakietu ftpparse Dana Bersteina, czyniąc go dostępnym z poziomu
Pythona.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
