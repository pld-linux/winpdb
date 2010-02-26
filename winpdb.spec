Summary:	Python debugger in wxGTK
Summary(pl.UTF-8):	Debugger pythona w wxGTK
Name:		winpdb
Version:	1.4.6
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/winpdb/%{name}-%{version}.tar.gz
Patch0:     	%{name}-rpdb2.patch
URL:		http://www.winpdb.org/
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpm-pythonprov
Requires:	rpdb2 = %{version}-%{release}
Requires:	python-wxPython
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Winpdb is a platform independent GPL Python debugger with support for
multiple threads, namespace modification, embedded debugging,
encrypted communication and is up to 20 times faster than pdb.

Winpdb provides the GUI for Rpdb2.

%description -l pl.UTF-8
Winpdb jest niezależnym od platformy odpluskwiaczem języka Python na
licencji GPL ze wsparciem wielu wątków, modyfikacji przestrzeni nazw,
zagnieżdżonego odpluskwiania, szyfrowanej komunikacji i jest do
dwudziestu razy szybszy od pdb.

Winpdb zapewnia graficzny interfejs użytkownika dla Rpdb2.

%package -n rpdb2
Summary:	Python console based debugger
Summary(pl.UTF-8):	Debugger pythona na konsolę tesktową
Group:		Development/Languages/Python
%pyrequires_eq	python-modules

%description -n rpdb2
Rpdb2 is a platform independent GPL Python debugger with support for
multiple threads, namespace modification, embedded debugging,
encrypted communication and is up to 20 times faster than pdb.

Rpdb2 is Winpdb without the GUI.

%description -n rpdb2 -l pl.UTF-8
Rpdb2 jest niezależnym od platformy odpluskwiaczem języka Python na
licencji GPL ze wsparciem wielu wątków, modyfikacji przestrzeni nazw,
zagnieżdżonego odpluskwiania, szyfrowanej komunikacji i jest do
dwudziestu razy szybszy od pdb.

Rpdb2 to Winpdb bez swojego graficznego interfejsu użytkownika.

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/winpdb
%{py_sitescriptdir}/winpdb.py[co]

%files -n rpdb2
%doc README.txt
%attr(755,root,root) %{_bindir}/rpdb2
%{py_sitescriptdir}/rpdb2.py[co]
%{py_sitescriptdir}/%{name}-*.egg-info
