%define name curl
%define version 5.11
%define release 3
%define prefix /usr

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: A utility for getting files from remote servers (FTP, HTTP, and others).
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: MPL
Vendor: Daniel Stenberg <Daniel.Stenberg@sth.frontec.se>
Packager: Troy Engel <tengel@sonic.net>
Group: Applications/Internet
Source: %{name}-%{version}.tar.gz
URL: http://www.fts.frontec.se/~dast/curl/
BuildRoot: /var/tmp/%{name}-%{version}-root

%description
cURL is a tool for getting files from FTP, HTTP, Gopher, Telnet, and
Dict servers, using any of the supported protocols. cURL is designed
to work without user interaction or any kind of interactivity. cURL
offers many useful capabilities, like proxy support, user
authentication, FTP upload, HTTP post, and file transfer resume.  Note
that while cURL also supports the SSL protocol, this version is
compiled without SSL (https:) support.

%prep
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%setup -q 

%build
export CFLAGS=$RPM_OPT_FLAGS 
./configure --prefix=%{prefix}
make 

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install-strip

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{prefix}/bin/curl
/usr/man/man1/curl.1
%doc curl.1 README* CHANGES CONTRIBUTE FAQ INSTALL LEGAL MPL-1.0.txt RESOURCES TODO perl/

%changelog 
* Mon Aug 30 1999 Tim Powers <timp@redhat.com>
- changed group

* Thu Aug 26 1999 Tim Powers <timp@redhat.com>
- changelog started
- general cleanups, changed prefix to /usr, added manpage to files section
- including in Powertools
