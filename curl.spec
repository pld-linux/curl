Summary:	A utility for getting files from remote servers (FTP, HTTP, and others)
Summary(es):	Busca URL (soporta FTP, TELNET, LDAP, GOPHER, DICT, HTTP y HTTPS)
Summary(pl):	Narzêdzie do ¶ci±gania plików z serwerów (FTP, HTTP i innych)
Summary(pt_BR):	Busca URL (suporta FTP, TELNET, LDAP, GOPHER, DICT, HTTP e HTTPS)
Name:		curl
Version:	7.9.5
Release:	1
License:	MPL
Vendor:		Daniel Stenberg <Daniel.Stenberg@sth.frontec.se>
Group:		Applications/Networking
Source0:	http://curl.haxx.se/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-no_strip.patch
URL:		http://curl.haxx.se/
%{!?_without_ssl:BuildRequires:	openssl-devel >= 0.9.6a}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libcurl2

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

%description -l es
Curl es un cliente para bajar documentos/archivos de servidores usando
uno de los protocolos soportados. Está proyectado para funcionar sin
interacción del usuario.

Curl trabaja con proxy, autenticación, ftp put, HTTP post, y puede
continuar transferencias interrumpidas, y además...

%description -l pl
cURL jest narzêdziem do ¶ci±gania plików o sk³adni URL. Obs³uguje FTP,
HTTP, HTTPS, GOPHER, TELNET, DICT, FILE i LDAP. cURL obs³uguje równie¿
HTTP POST, HTTP PUT, za³adowywanie (uploading) FTP, za³adowywanie HTTP
oparte na formularzu, serwery proksy, ciasteczka, autoryzacja
u¿ytkownik/has³o oraz wiele innych u¿ytecznych sztuczek. Curla u¿ywa
siê g³ównie wtedy, kiedy chce siê automatycznie ¶ci±gn±æ lub wys³aæ
pliki z/na serwer u¿ywaj±c jednego z dostêpnych protoko³ów.

Uwaga: ten pakiet wspiera takze SSL.

%description -l pt_BR
Curl é um cliente para baixar/enviar arquivos de/para servidores
usando um dos protocolos suportados. É projetado para funcionar sem a
interação do usuário.

Curl trabalha com proxy, autenticação, ftp put, HTTP post, e pode
continuar transferências interrompidas, e mais...

%package devel
Summary:	Header files and development documentation for curl library
Summary(pl):	Pliki nag³ówkowe i dokumentacja do biblioteki curl
Summary(pt_BR):	Arquivos de cabeçalho e bibliotecas de desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libcurl2-devel

%description devel
Header files and development documentation for curl library.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do biblioteki curl.

%description devel -l pt_BR
Arquivos de cabeçalho e bibliotecas de desenvolvimento.

%package static
Summary:	Static version of curl library
Summary(pl):	Statyczna wersja biblioteki curl
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com o curl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of curl library.

%description static -l pl
Statyczna wersja biblioteki curl.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com o curl.

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

gzip -9nf CHANGES LEGAL README docs/TheArtOfHttpScripting \
	docs/{BUGS,CONTRIBUTE,FAQ,FEATURES,INTERNALS,MANUAL,README*,RESOURCES,THANKS,TODO}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.gz
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
