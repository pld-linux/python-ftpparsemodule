%include	/usr/lib/rpm/macros.python
%define 	module	ftpparsemodule

Summary:	Python package providing parse ftp LIST command
Summary(pl):	Pakiet Pythona do analizy polecenia ftp LIST
Name:		python-%{module}
Version:	0.93
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://c0re.23.nu/c0de/ftpparsemodule/ftpparsemodule-%{version}.tar.gz
# Source0-md5:	05735a02d74554f8895e9faf5e3b15d5
Patch0:		%{module}-gcc.patch
URL:		http://c0re.23.nu/c0de/ftpparsemodule/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTP-Servers provide a wide range of responses to the LIST command.
ftpparsemodule allows you to parse most ftp-servers LIST responses
found in the wild. It does so by using Dan Bernstein's ftpparse
package and making it accessible to Python.

%description -l pl
Serwery FTP dostarczaj± du¿ego rozrzutu odpowiedzi na polecenie LIST.
ftpparsemodule pozwala przeanalizowaæ odpowiedzi na LIST pochodz±ce od
wiêkszo¶ci serwerów FTP istniej±cych na ¶wiecie. Robi to przy u¿yciu
pakietu ftpparse Dana Bersteina, czyni±c go dostêpnym z poziomu
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
