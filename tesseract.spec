# TODO:
# - warnings at compile stage about pointer size on amd64 - needs check
# - warning: Installed (but unpackaged) file(s) found:
#        /usr/bin/language-specific.sh
#        /usr/bin/tesstrain.sh
#        /usr/bin/tesstrain_utils.sh
#
# Conditional build:
%bcond_without	openmp	# OpenMP support
%bcond_with	opencl	# OpenCL support
Summary:	Tesseract Open Source OCR Engine
Summary(pl.UTF-8):	Tesseract - silnik OCR o otwartych źródłach
Name:		tesseract
Version:	4.1.1
Release:	3
License:	Apache v2.0
Group:		Applications/Graphics
#Source0Download: https://github.com/tesseract-ocr/tesseract/releases
Source0:	https://github.com/tesseract-ocr/tesseract/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	51fe2bcbff1bbce77a25d180fd247f7d
URL:		https://github.com/tesseract-ocr/
%{?with_opencl:BuildRequires:	OpenCL-devel}
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	curl-devel
BuildRequires:	leptonlib-devel >= 1.74
BuildRequires:	libarchive-devel
%{?with_openmp:BuildRequires:	libgomp-devel}
BuildRequires:	libicu-devel >= 52.1
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pango-devel >= 1:1.22.0
Requires:	leptonlib >= 1.74
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

%package training
Summary:	Tesseract training tools
Summary(pl.UTF-8):	Narzędzia treningowe Tesseracta
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	pango >= 1:1.22.0

%description training
This package contains the Tesseract training tools.

%description training -l pl.UTF-8
Ten pakiet zawiera programy do trenowania Tesseracta.

%package devel
Summary:	Header files for Tesseract libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Tesseracta
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	leptonlib-devel >= 1.74
Requires:	libarchive-devel
Requires:	libstdc++-devel >= 6:4.7

%description devel
This package contains the development header files necessary to
develop applications using Tesseract API.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów
wykorzystujących API Tesseracta.

%package static
Summary:	Static Tesseract libraries
Summary(pl.UTF-8):	Statyczne biblioteki Tesseracta
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Tesseract libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Tesseracta.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_opencl:--enable-opencl} \
	%{!?with_openmp:--disable-openmp}
%{__make}
%{__make} training

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} training-install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtesseract.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %{_bindir}/tesseract
%attr(755,root,root) %{_libdir}/libtesseract.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract.so.4
%{_datadir}/tessdata
%{_mandir}/man1/tesseract.1*

%files training
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ambiguous_words
%attr(755,root,root) %{_bindir}/classifier_tester
%attr(755,root,root) %{_bindir}/cntraining
%attr(755,root,root) %{_bindir}/combine_lang_model
%attr(755,root,root) %{_bindir}/combine_tessdata
%attr(755,root,root) %{_bindir}/dawg2wordlist
%attr(755,root,root) %{_bindir}/lstmeval
%attr(755,root,root) %{_bindir}/lstmtraining
%attr(755,root,root) %{_bindir}/merge_unicharsets
%attr(755,root,root) %{_bindir}/mftraining
%attr(755,root,root) %{_bindir}/set_unicharset_properties
%attr(755,root,root) %{_bindir}/shapeclustering
%attr(755,root,root) %{_bindir}/text2image
%attr(755,root,root) %{_bindir}/unicharset_extractor
%attr(755,root,root) %{_bindir}/wordlist2dawg
%{_mandir}/man1/ambiguous_words.1*
%{_mandir}/man1/classifier_tester.1*
%{_mandir}/man1/cntraining.1*
%{_mandir}/man1/combine_lang_model.1*
%{_mandir}/man1/combine_tessdata.1*
%{_mandir}/man1/dawg2wordlist.1*
%{_mandir}/man1/lstmeval.1*
%{_mandir}/man1/lstmtraining.1*
%{_mandir}/man1/merge_unicharsets.1*
%{_mandir}/man1/mftraining.1*
%{_mandir}/man1/set_unicharset_properties.1*
%{_mandir}/man1/shapeclustering.1*
%{_mandir}/man1/text2image.1*
%{_mandir}/man1/unicharset_extractor.1*
%{_mandir}/man1/wordlist2dawg.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtesseract.so
%{_includedir}/%{name}
%{_pkgconfigdir}/tesseract.pc
%{_mandir}/man5/unicharambigs.5*
%{_mandir}/man5/unicharset.5*

%files static
%defattr(644,root,root,755)
%{_libdir}/libtesseract.a
