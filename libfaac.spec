Name:           libfaac
Version:        1.28
Release:        1%{?dist}
Summary:        An MPEG-4 and MPEG-2 AAC encoder

License:        LGPLv2+
URL:            http://www.audiocoding.com/
Source0:        http://downloads.sourceforge.net/project/faac/faac-src/faac-%{version}/faac-%{version}.tar.bz2

# Patch from the srpm at
# http://li.nux.ro/download/nux/dextop/el7/SRPMS/faac-1.28-6.0.el7.nux.src.rpm
Patch0:         faac-strcasestr.patch

%description
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        -n faac
Summary:        FAAC cli encoder

%description    -n faac
This package contains the frontend.


%prep
%setup -q -n faac-%{version}
%patch0 -p1


%build
%configure \
    --with-mp4v2 \
    --enable-shared=yes \
    --enable-static=no

sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so

%files -n faac
%{_bindir}/*
%{_mandir}/man1/*.1*


%changelog
* Wed Aug 10 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.28-1
- Public release
