# http://github.com/hashicorp/serf
%global provider_prefix github.com/hashicorp/serf
%global gobaseipath     %{provider_prefix}
%global commit          a72c0453da2ba628a013e98bf323a76be4aa1443
%global commitdate      20151109

%gocraftmeta -i

Name:           %{goname}
Version:        0.6.4
Release:        0.9.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Service orchestration and management tool http://www.serfdom.io
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/armon/circbuf)
BuildRequires: golang(github.com/armon/go-metrics)
BuildRequires: golang(github.com/hashicorp/go-msgpack/codec)
BuildRequires: golang(github.com/hashicorp/go-syslog)
BuildRequires: golang(github.com/hashicorp/logutils)
BuildRequires: golang(github.com/hashicorp/mdns)
BuildRequires: golang(github.com/hashicorp/memberlist)
#BuildRequires: golang(github.com/mitchellh/cli)
BuildRequires: golang-github-mitchellh-cli-devel-temporary
BuildRequires: golang(github.com/mitchellh/mapstructure)
BuildRequires: golang(github.com/ryanuber/columnize)

#Requires:      golang(github.com/mitchellh/cli)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup

%install
%goinstall

%check
%gochecks %{gobaseipath}/{command,command/agent,serf}

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc CHANGELOG.md README.md

%changelog
* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.6.4-0.9.20151109gita72c045
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-0.8.gita72c045
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-0.7.gita72c045
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-0.6.gita72c045
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-0.5.gita72c045
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-0.4.gita72c045
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-0.3.gita72c045
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-0.2.gita72c045
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 jchaloup <jchaloup@redhat.com> - 0.6.4-0.1.gita72c045
- Bump to upstream a72c0453da2ba628a013e98bf323a76be4aa1443
  related: #1250477

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git4bd6183
- Update to spec-2.1
  related: #1250477

* Mon Aug 24 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git4bd6183
- Update spec file to spec-2.0
  resolves: #1250477

* Thu Jul 16 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git4bd6183
- Disable command test
  related: #1212318

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git4bd6183
- First package for Fedora
  resolves: #1212318

