#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sROC
Version  : 0.1.2
Release  : 21
URL      : https://cran.r-project.org/src/contrib/sROC_0.1-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sROC_0.1-2.tar.gz
Summary  : Nonparametric Smooth ROC Curves for Continuous Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-sROC-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
nonparametric estimation of receiver operating characteristic
        (ROC) curves for continuous data.

%package lib
Summary: lib components for the R-sROC package.
Group: Libraries

%description lib
lib components for the R-sROC package.


%prep
%setup -q -c -n sROC

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552940537

%install
export SOURCE_DATE_EPOCH=1552940537
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sROC
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sROC
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sROC
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  sROC || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sROC/DESCRIPTION
/usr/lib64/R/library/sROC/INDEX
/usr/lib64/R/library/sROC/LICENSE
/usr/lib64/R/library/sROC/Meta/Rd.rds
/usr/lib64/R/library/sROC/Meta/features.rds
/usr/lib64/R/library/sROC/Meta/hsearch.rds
/usr/lib64/R/library/sROC/Meta/links.rds
/usr/lib64/R/library/sROC/Meta/nsInfo.rds
/usr/lib64/R/library/sROC/Meta/package.rds
/usr/lib64/R/library/sROC/NAMESPACE
/usr/lib64/R/library/sROC/NEWS
/usr/lib64/R/library/sROC/R/sROC
/usr/lib64/R/library/sROC/R/sROC.rdb
/usr/lib64/R/library/sROC/R/sROC.rdx
/usr/lib64/R/library/sROC/help/AnIndex
/usr/lib64/R/library/sROC/help/aliases.rds
/usr/lib64/R/library/sROC/help/paths.rds
/usr/lib64/R/library/sROC/help/sROC.rdb
/usr/lib64/R/library/sROC/help/sROC.rdx
/usr/lib64/R/library/sROC/html/00Index.html
/usr/lib64/R/library/sROC/html/R.css
/usr/lib64/R/library/sROC/script/.Rapp.history
/usr/lib64/R/library/sROC/script/Example_codes.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sROC/libs/sROC.so
/usr/lib64/R/library/sROC/libs/sROC.so.avx2
