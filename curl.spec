Summary:	A utility for getting files from remote servers (FTP, HTTP, and others)
Summary(pl):	Narzêdzie do ¶ci±gania plików z serwerów (FTP, HTTP i innych)
Name:		curl
Version:	7.9
Release:	1
License:	MPL
Vendor:		Daniel Stenberg <Daniel.Stenberg@sth.frontec.se>
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://curl.haxx.se/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-no_strip.patch
URL:		http://curl.haxx.se/
%{!?_without_ssl:BuildRequires:	openssl-devel >= 0.9.6a}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cURL is a tool for getting files with URL syntax, supporting FTP,
HTTP, HTTPS, GOPHER, TELNET, DICT, FILE and LDAP. cURL supports HTTP
POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies,
cookies, user+password authentication and a busload of other useful
tricks. The main use for curl is when you want to get or send files
automatically to or from a site using one of the supported protocols.

cURL is a tool for getting files from FTP, HTTP, Gopher, Telnet, and
Dict servers, using any of the supported protocols. cURL is designed
to work without user interaction or any kind of interactivity. cURL
offers many useful capabilities, like proxy support, user
authentication, FTP upload, HTTP post, and file transfer resume.

%description -l pl
cURL jest narzêdziem do ¶ci±gania plików o sk³adni URL. Obs³uguje FTP,
HTTP, HTTPS, GOPHER, TELNET, DICT, FILE i LDAP. cURL obs³uguje równie¿
HTTP POST, HTTP PUT, za³adowywanie (uploading) FTP, za³adowywanie HTTP
oparte na formularzu, serwery proksy, ciasteczka, autoryzacja
u¿ytkownik/has³o oraz wiele innych u¿ytecznych sztuczek. Curla u¿ywa
siê g³ównie wtedy, kiedy chce siê automatycznie ¶ci±gn±æ lub wys³aæ
pliki z/na serwer u¿ywaj±c jednego z dostêpnych protoko³ów.

%package devel
Summary:	Header files and development documentation for curl library
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki curl
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for curl library.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do biblioteki curl.

%package static
Summary:	Static version of curl library
Summary(pl):	Statyczna wersja biblioteki curl
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static version of curl library.

%description -l pl static
Statyczna wersja biblioteki curl.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	%{!?_without_ssl:--with-ssl=%{_prefix}} \
	--with-ipv6

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf docs/{BUGS,RESOURCES,CONTRIBUTE,FEATURES,FAQ,INTERNALS,README*,TODO,TheArtOfHttpScripting}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/*.gz
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_mandir}/man3/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
