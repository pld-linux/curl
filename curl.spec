#
# Conditional build:
%bcond_without	ssh		# without SSH support
%bcond_without	ssl		# without SSL support
%bcond_without	kerberos5	# without Heimdal Kerberos 5 support
%bcond_without	ldap		# without LDAP support
%if "%{pld_release}" != "ac"
%bcond_without	ares		# with c-ares (asynchronous DNS operations) library
%bcond_without	gnutls		# use GnuTLS instead of OpenSSL
%bcond_without	rtmp		# without Real Time Media Protocol
%else
%bcond_with	ares		# with c-ares (asynchronous DNS operations) library
%bcond_with	gnutls		# use GnuTLS instead of OpenSSL
%bcond_with	rtmp		# without Real Time Media Protocol
%endif

Summary:	A utility for getting files from remote servers (FTP, HTTP, and others)
Summary(es.UTF-8):	Un cliente para bajar archivos de servidores (FTP, HTTP, y otros)
Summary(pl.UTF-8):	Narzędzie do ściągania plików z serwerów (FTP, HTTP i innych)
Summary(pt_BR.UTF-8):	Busca URL (suporta FTP, TELNET, LDAP, GOPHER, DICT, HTTP e HTTPS)
Summary(ru.UTF-8):	Утилита для получения файлов с серверов FTP, HTTP и других
Summary(uk.UTF-8):	Утиліта для отримання файлів з серверів FTP, HTTP та інших
Name:		curl
Version:	7.28.1
Release:	1
License:	MIT-like
Group:		Applications/Networking
Source0:	http://curl.haxx.se/download/%{name}-%{version}.tar.lzma
# Source0-md5:	b716ab1103fd4bef99b98f5ff2c7b638
Patch1:		%{name}-ac.patch
Patch2:		%{name}-pc.patch
Patch3:		%{name}-krb5flags.patch
Patch4:		%{name}-gnutls.patch
URL:		http://curl.haxx.se/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
%{?with_ares:BuildRequires:	c-ares-devel >= 1.7.0}
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	libidn-devel >= 0.4.1
%{?with_rtmp:BuildRequires:	librtmp-devel}
%{?with_ssh:BuildRequires:	libssh2-devel >= 1.2.8}
BuildRequires:	libtool
BuildRequires:	nettle-devel
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.453
%if %{with ssl}
%if %{with gnutls}
BuildRequires:	gnutls-devel
%else
BuildRequires:	openssl-devel >= 0.9.7d
%endif
%endif
BuildRequires:	tar >= 1:1.22
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libidn >= 0.4.1
%{?with_ssh:Requires:	libssh2 >= 1.2.8}
Obsoletes:	libcurl2
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

%description -l pl.UTF-8
cURL jest narzędziem do ściągania plików o składni URL. Obsługuje FTP,
HTTP, HTTPS, GOPHER, TELNET, DICT, FILE i LDAP. cURL obsługuje również
HTTP POST, HTTP PUT, załadowywanie (uploading) FTP, załadowywanie HTTP
oparte na formularzu, serwery proksy, ciasteczka, autoryzacja
użytkownik/hasło oraz wiele innych użytecznych sztuczek. Curla używa
się głównie wtedy, kiedy chce się automatycznie ściągnąć lub wysłać
pliki z/na serwer używając jednego z dostępnych protokołów.
%{?with_ssl:Ten pakiet obsługuje także SSL.}

%description -l pt_BR.UTF-8
Curl é um cliente para baixar/enviar arquivos de/para servidores
usando um dos protocolos suportados. É projetado para funcionar sem a
interação do usuário.

Curl trabalha com proxy, autenticação, FTP put, HTTP post, e pode
continuar transferências interrompidas, e mais...

%description -l ru.UTF-8
curl - это клиент с множеством поддерживаемых протоколов для получения
файлов с серверов, спроектированный для работы как в неинтерактивном
режиме, так и с возможностью диалога с пользователем.

curl поддерживает много полезных возможностей, среди которых поддержка
прокси, авторизация пользователя, закачивание по FTP, поддержка HTTP
POST, восстановление прерванной пересылки и многое другое.

curl - це кл╕╓нт з багатьма п╕дтримуваними протоколами для отримання
файл╕в з сервер╕в, спроектований для роботи як в не╕нтерактивному
режим╕, так ╕ з можлив╕стю д╕алогу з користувачем.

curl п╕дтриму╓ багато корисних можливостей, серед яких п╕дтримка
прокс╕, авторизац╕я користувача, в╕двантаження по FTP, HTTP POST,
в╕дновлення перервано╖ пересилки та багато ╕ншого.

%package libs
Summary:	curl library
Summary(pl.UTF-8):	Biblioteka curl
Group:		Libraries
%{?with_ares:Requires:	c-ares >= 1.7.0}
Suggests:	ca-certificates
Conflicts:	ca-certificates < 20080809-4

%description libs
curl library.

%description libs -l pl.UTF-8
Biblioteka curl.

%package devel
Summary:	Header files and development documentation for curl library
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do biblioteki curl
Summary(pt_BR.UTF-8):	Arquivos de cabeçalho e bibliotecas de desenvolvimento
Summary(ru.UTF-8):	Файлы для разработки с использованием библиотеки curl
Summary(uk.UTF-8):	Файли для розробки з використанням бібліотеки curl
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
%{?with_ares:Requires:	c-ares-devel}
%{?with_kerberos5:Requires:	heimdal-devel}
Requires:	libidn-devel >= 0.4.1
%{?with_rtmp:Requires:	librtmp-devel}
%{?with_ssh:Requires:	libssh2-devel >= 1.2.8}
%{?with_ldap:Requires:	openldap-devel}
%if %{with ssl}
%if %{with gnutls}
Requires:	gnutls-devel
%else
Requires:	openssl-devel >= 0.9.7c
%endif
%endif
Requires:	zlib-devel
Obsoletes:	libcurl2-devel

%description devel
Header files and development documentation for curl library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do biblioteki curl.

%description devel -l pt_BR.UTF-8
Arquivos de cabeçalho e bibliotecas de desenvolvimento.

%description devel -l ru.UTF-8
Этот пакет содержит файлы, необходимые для разработки программ с
использованием библиотеки curl.

%description devel -l uk.UTF-8
Цей пакет містить файли, необхідні для розробки програм з
використанням бібліотеки curl.

%package static
Summary:	Static version of curl library
Summary(pl.UTF-8):	Statyczna wersja biblioteki curl
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com o curl
Summary(ru.UTF-8):	Статические библиотеки для разработки с использованием библиотеки curl
Summary(uk.UTF-8):	Статичні бібліотеки для розробки з використанням бібліотеки curl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of curl library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki curl.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com o curl.

%description static -l ru.UTF-8
Этот пакет содержит статическую библиотеку для разработки программ с
использованием библиотеки curl.

%description static -l uk.UTF-8
Цей пакет містить статичну бібліотеку для розробки програм з
використанням бібліотеки curl.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%{__rm} -v m4/lt*.m4 m4/libtool.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_header_gss_h=no \
%if %{with ssl}
	--with-ca-bundle=/etc/certs/ca-certificates.crt \
%if %{with gnutls}
	--with-gnutls --without-ssl \
%else
	--with-ssl=%{_prefix} \
%endif
%endif
	%{?with_kerberos5:--with-gssapi=%{_prefix}} \
	%{?with_rtmp:--with-librtmp} \
	%{?with_ares:--enable-ares} \
	%{?with_ldap:--enable-ldaps} \
	%{!?with_ldap:--disable-ldap} \
	--enable-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no longer in upstream but a lot of apps tries to include it so we create fake one
[ -e $RPM_BUILD_ROOT%{_includedir}/curl/types.h ] && exit 1
echo '#warning curl/types.h IS OBSOLETE FROM 2004. STOP USING IT' > $RPM_BUILD_ROOT%{_includedir}/curl/types.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README docs/{BUGS,FAQ,FEATURES,HISTORY,KNOWN_BUGS,MANUAL,SSLCERTS,THANKS,TODO,TheArtOfHttpScripting}
%attr(755,root,root) %{_bindir}/curl
%{_mandir}/man1/curl.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcurl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcurl.so.4

%files devel
%defattr(644,root,root,755)
%doc docs/{CONTRIBUTE,INTERNALS,LICENSE-MIXING,RESOURCES}
%attr(755,root,root) %{_bindir}/curl-config
%attr(755,root,root) %{_libdir}/libcurl.so
%{_libdir}/libcurl.la
%{_includedir}/curl
%{_pkgconfigdir}/libcurl.pc
%{_mandir}/man1/curl-config.1*
%{_mandir}/man3/curl_*.3*
%{_mandir}/man3/libcurl*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcurl.a
