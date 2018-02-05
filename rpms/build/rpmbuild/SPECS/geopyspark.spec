%define _topdir   /tmp/rpmbuild
%define name      geopyspark-deps
%define release   13
%define version   0.0.0

%define debug_package %{nil}

BuildRoot: %{buildroot}
Summary:   GeoPySpark dependencies
License:   ?
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    geopyspark.tar
Prefix:    /
Group:     Azavea
AutoReq:   no

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%description
GeoPySpark dependencies

%prep
%setup -q -n geopyspark

%build
echo

%install
find /usr/local/lib /usr/local/lib64 | sort > before.txt
pip3 install -r requirements.txt
find /usr/local/lib /usr/local/lib64 | sort > after.txt
tar cvf /tmp/packages.tar $(diff before.txt after.txt | grep '^>' | cut -f2 '-d ')
cd %{buildroot}
tar axvf /tmp/packages.tar

%files
%defattr(-,root,root)
/usr/local/lib/*
/usr/local/lib64/*
