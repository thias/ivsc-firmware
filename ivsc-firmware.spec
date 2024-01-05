%global debug_package %{nil}

%global commit 10c214fea5560060d387fbd2fb8a1af329cb6232
%global commitdate 20230811
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           ivsc-firmware
Summary:        Intel iVSC firmware
URL:            https://github.com/intel/ivsc-firmware
Version:        0.0
Release:        6.%{commitdate}git%{shortcommit}%{?dist}
License:        Proprietary

Source0:        https://github.com/intel/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

ExclusiveArch:  x86_64

%description
This provides the necessary firmware for Intel iVSC.

%prep
%autosetup -n %{name}-%{commit}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1
mkdir -p %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod
pushd firmware/
for i in *.bin; do
  cp -a "$i" %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1/`echo "$i" | sed 's|\.bin|_a1\.bin|'`;
  cp -a "$i" %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/`echo "$i" | sed 's|\.bin|_a1_prod\.bin|'`;
done
popd

%files
%license LICENSE
%{_prefix}/lib/firmware/vsc/

%changelog
* Tue Oct 10 2023 Matthias Saou <matthias@saou.eu> 0.0-6.20230811git10c214f
- Update to 10c214fea5560060d387fbd2fb8a1af329cb6232.

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0-5.20221102git29c5eff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 1 2023 Kate Hsuan <hpa@redhat.com> - 0.0-4.20221102git29c5eff
- Install debug firmware too
- Simplified firmware installation

* Fri Feb 17 2023 Kate Hsuan <hpa@redhat.com> - 0.0-3.20221102git29c5eff
- Sepcfile update

* Tue Dec 20 2022 Kate Hsuan <hpa@redhat.com> - 0.0-2.20221102git29c5eff
- Style and format fixes.

* Tue Nov 15 2022 Kate Hsuan <hpa@redhat.com> - 0.0
- Firmware for Intel iVSC
