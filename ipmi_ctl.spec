Summary:	Utilities to interface with IPMI based managment hardware
Summary(pl):	Narzêdzia sprzêgaj±ce ze sprzêtem zarz±dzanym w oparciu o IPMI
Name:		ipmi_ctl
Version:	2.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/ipmitools/%{name}-%{version}.tar.gz
# Source0-md5:	f3509448ef8dbe4374e7b19638ba2964
Patch0:		%{name}-debian.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User utilities to interface with IPMI based management hardware
available on many motherboards. IPMI stands for Intelligent Platform
Management Interface. Supports features such as watchdogs, FRU
download. ethtool is a small utility for examining and tuning your
ethernet-based network interface.

%description -l es
Grupos de herramientas Ethernet para tarjetas SPARC HME.

%description -l pl
Pakiet ten zawiera narzêdzia sprzêgaj±ce ze sprzêtem zarz±dzanym w
oparciu o IPMI. IPMI oznacza Intelligent Platform Management Interface
(inteligentny interfejs do zarz±dzania platform±). Wspiera on takie
mo¿liwo¶ci, jak watchdogi czy pobieranie FRU. ethtool to niewielkie
narzêdzie do kontroli i tuningu sieciowych kart ethernet.

%description -l pt_BR
Este utilitário permite consulta e alteração da configuração de placas
ethernet, como velocidade, porta, negociação automática e localização
PCI.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
