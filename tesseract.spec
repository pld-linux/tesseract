# TODO:
# - warnings at compile stage about pointer size on amd64 - needs check
Summary:	Tesseract Open Source OCR Engine
Summary(pl.UTF-8):	Tesseract - silnik OCR o otwartych źródłach
Name:		tesseract
Version:	3.00
Release:	1
License:	Apache v2.0
Group:		Applications/Graphics
#Source0Download: http://code.google.com/p/tesseract-ocr/downloads/list
Source0:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	cc812a261088ea0c3d2da735be35d09f
Patch0:		%{name}-missing.patch
Patch1:		%{name}-link.patch
URL:		http://code.google.com/p/tesseract-ocr/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	leptonlib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
Suggests:	tesseract-data >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A commercial quality OCR engine originally developed at HP between
1985 and 1995. In 1995, this engine was among the top 3 evaluated by
UNLV. It was open-sourced by HP and UNLV in 2005.

%description -l pl.UTF-8
Silnik OCR o komercyjnej jakości oryginalnie stworzony przez HP w
latach 1985-1995. W 1995 roku był jednym z 3 najlepszych wg UNLV.
Źródła zostały uwolnione przez HP i UNLV w 2005 roku.

%package devel
Summary:	Header files for Tesseract libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Tesseracta
Group:          Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	leptonlib-devel
Requires:	libstdc++-devel
Requires:	libtiff-devel

%description devel
This package contains the development header files necessary to
develop applications using Tesseract API.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów
wykorzystujących API Tesseracta.

%package static
Summary:	Static Tesseract libraries
Summary(pl.UTF-8):	Statyczne biblioteki Tesseracta
Group:          Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Tesseract libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Tesseracta.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README ReleaseNotes
%attr(755,root,root) %{_bindir}/cntraining
%attr(755,root,root) %{_bindir}/combine_tessdata
%attr(755,root,root) %{_bindir}/mftraining
%attr(755,root,root) %{_bindir}/tesseract
%attr(755,root,root) %{_bindir}/unicharset_extractor
%attr(755,root,root) %{_bindir}/wordlist2dawg
%attr(755,root,root) %{_libdir}/libtesseract_api.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_api.so.3
%attr(755,root,root) %{_libdir}/libtesseract_ccstruct.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_ccstruct.so.3
%attr(755,root,root) %{_libdir}/libtesseract_ccutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_ccutil.so.3
%attr(755,root,root) %{_libdir}/libtesseract_classify.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_classify.so.3
%attr(755,root,root) %{_libdir}/libtesseract_cutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_cutil.so.3
%attr(755,root,root) %{_libdir}/libtesseract_dict.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_dict.so.3
%attr(755,root,root) %{_libdir}/libtesseract_image.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_image.so.3
%attr(755,root,root) %{_libdir}/libtesseract_main.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_main.so.3
%attr(755,root,root) %{_libdir}/libtesseract_textord.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_textord.so.3
%attr(755,root,root) %{_libdir}/libtesseract_training.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_training.so.3
%attr(755,root,root) %{_libdir}/libtesseract_viewer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_viewer.so.3
%attr(755,root,root) %{_libdir}/libtesseract_wordrec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract_wordrec.so.3
%dir %{_datadir}/tessdata
%dir %{_datadir}/tessdata/configs
%{_datadir}/tessdata/configs/*
%dir %{_datadir}/tessdata/tessconfigs
%{_datadir}/tessdata/tessconfigs/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtesseract_api.so
%attr(755,root,root) %{_libdir}/libtesseract_ccstruct.so
%attr(755,root,root) %{_libdir}/libtesseract_ccutil.so
%attr(755,root,root) %{_libdir}/libtesseract_classify.so
%attr(755,root,root) %{_libdir}/libtesseract_cutil.so
%attr(755,root,root) %{_libdir}/libtesseract_dict.so
%attr(755,root,root) %{_libdir}/libtesseract_image.so
%attr(755,root,root) %{_libdir}/libtesseract_main.so
%attr(755,root,root) %{_libdir}/libtesseract_textord.so
%attr(755,root,root) %{_libdir}/libtesseract_training.so
%attr(755,root,root) %{_libdir}/libtesseract_viewer.so
%attr(755,root,root) %{_libdir}/libtesseract_wordrec.so
%{_libdir}/libtesseract_api.la
%{_libdir}/libtesseract_ccstruct.la
%{_libdir}/libtesseract_ccutil.la
%{_libdir}/libtesseract_classify.la
%{_libdir}/libtesseract_cutil.la
%{_libdir}/libtesseract_dict.la
%{_libdir}/libtesseract_image.la
%{_libdir}/libtesseract_main.la
%{_libdir}/libtesseract_textord.la
%{_libdir}/libtesseract_training.la
%{_libdir}/libtesseract_viewer.la
%{_libdir}/libtesseract_wordrec.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libtesseract_api.a
%{_libdir}/libtesseract_ccstruct.a
%{_libdir}/libtesseract_ccutil.a
%{_libdir}/libtesseract_classify.a
%{_libdir}/libtesseract_cutil.a
%{_libdir}/libtesseract_dict.a
%{_libdir}/libtesseract_image.a
%{_libdir}/libtesseract_main.a
%{_libdir}/libtesseract_textord.a
%{_libdir}/libtesseract_training.a
%{_libdir}/libtesseract_viewer.a
%{_libdir}/libtesseract_wordrec.a
