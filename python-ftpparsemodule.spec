%include	/usr/lib/rpm/macros.python
%define 	module ftpparsemodule

Summary:	Python package providing parse ftp LIST command
Name:		python-%{module}
Version:	0.93
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://c0re.23.nu/c0de/ftpparsemodule/ftpparsemodule-%{version}.tar.gz
# Source0-md5:	05735a02d74554f8895e9faf5e3b15d5
URL:		http://c0re.23.nu/c0de/ftpparsemodule/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FTP-Servers provide a wide range of responses to the LIST command.
ftpparsemodule allows you to parse most ftp-servers LIST responses
found in the wild. It does so by using Dan Bernsteins ftpparse package
and making it accessible to Python.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
        --root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc %{module}/doc %{module}/examples
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/common
%{py_sitedir}/%{module}/common/*.py[co]
%dir %{py_sitedir}/%{module}/xml
%{py_sitedir}/%{module}/xml/*.py[co]
