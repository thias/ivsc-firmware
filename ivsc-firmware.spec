%global debug_package %{nil}

%global commit 29c5eff4cdaf83e90ef2dcd2035a9cdff6343430
%global commitdate 20221102
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           ivsc-firmware
Summary:        Intel iVSC firmware
URL:            https://github.com/intel/ivsc-firmware
Version:        0.0
Release:        4.%{commitdate}git%{shortcommit}%{?dist}
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
* Wed Mar 1 2023 Kate Hsuan <hpa@redhat.com> - 0.0-4.20221102git29c5eff
- Install debug firmware too
- Simplified firmware installation

* Fri Feb 17 2023 Kate Hsuan <hpa@redhat.com> - 0.0-3.20221102git29c5eff
- Sepcfile update

* Tue Dec 20 2022 Kate Hsuan <hpa@redhat.com> - 0.0-2.20221102git29c5eff
- Style and format fixes.

* Tue Nov 15 2022 Kate Hsuan <hpa@redhat.com> - 0.0
- Firmware for Intel iVSC
