Summary:	A utility for getting files from remote servers (FTP, HTTP, and others).
Name:		curl
Version:	6.3.1
Release:	1
Copyright:	MPL
Vendor:		Daniel Stenberg <Daniel.Stenberg@sth.frontec.se>
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source:		http://curl.haxx.nu/stuff/%{name}-%{version}.tar.gz
URL:		http://curl.haxx.nu/
BuildRequires:	openssl-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
cURL is a tool for getting files with URL syntax, supporting FTP, HTTP,
HTTPS, GOPHER, TELNET, DICT, FILE and LDAP. cURL supports HTTP POST, HTTP
PUT, FTP uploading, HTTP form based upload, proxies, cookies, user+password
authentication and a busload of other useful tricks. The main use for curl
is when you want to get or send files automatically to or from a site using
one of the supported protocols.

cURL is a tool for getting files from FTP, HTTP, Gopher, Telnet, and Dict
servers, using any of the supported protocols. cURL is designed to work
without user interaction or any kind of interactivity. cURL offers many
useful capabilities, like proxy support, user authentication, FTP upload,
HTTP post, and file transfer resume. Note that while cURL also supports the
SSL protocol, this version is compiled without SSL (https:) support.

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
