Summary:	A utility for getting files from remote servers (FTP, HTTP, and others)
Name:		curl
Version:	6.5.2
Release:	1
License:	MPL
Vendor:		Daniel Stenberg <Daniel.Stenberg@sth.frontec.se>
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	http://curl.haxx.nu/stuff/%{name}-%{version}.tar.gz
URL:		http://curl.haxx.nu/
BuildRequires:	openssl-devel
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
authentication, FTP upload, HTTP post, and file transfer resume. Note
that while cURL also supports the SSL protocol, this version is
compiled without SSL (https:) support.

%description -l pl
cURL jest narzêdziem do ¶ci±gania plików o sk³adni URL. Obs³uguje FTP,
HTTP, HTTPS, GOPHER, TELNET, DICT, FILE i LDAP. cURL obs³uguje równie¿
HTTP POST, HTTP PUT, za³adowywanie (uploading) FTP, za³adowywanie HTTP
oparte na formularzu, serwery proksy, ciasteczka, autoryzacja
u¿ytkownik/has³o oraz wiele innych u¿ytecznych sztuczek. Curla u¿ywa
siê g³ównie wtedy, kiedy chce siê automatycznie ¶ci±gn±æ lub wys³aæ
pliki z/na serwer u¿ywaj±c jednego z dostêpnych protoko³ów. Chocia¿
cURL obs³uguje równie¿ protokó³ SSL, wersja ta jest skompilowana bez
obs³ugi SSL (https:).

%prep
%setup -q 

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-ssl=/usr
make 

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README* CHANGES CONTRIBUTE FAQ LEGAL MPL-1.0.txt RESOURCES TODO
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/curl
%{_mandir}/man1/*
