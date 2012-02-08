# TODO:
# - warnings at compile stage about pointer size on amd64 - needs check
Summary:	Tesseract Open Source OCR Engine
Summary(pl.UTF-8):	Tesseract - silnik OCR o otwartych źródłach
Name:		tesseract
Version:	3.01
Release:	2
License:	Apache v2.0
Group:		Applications/Graphics
#Source0Download: http://code.google.com/p/tesseract-ocr/downloads/list
Source0:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	1ba496e51a42358fb9d3ffe781b2d20a
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

rm -f $RPM_BUILD_ROOT%{_libdir}/libtesseract.la

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
%attr(755,root,root) %{_libdir}/libtesseract.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtesseract.so.3
%dir %{_datadir}/tessdata
%dir %{_datadir}/tessdata/configs
%{_datadir}/tessdata/configs/*
%dir %{_datadir}/tessdata/tessconfigs
%{_datadir}/tessdata/tessconfigs/*
%{_mandir}/man1/cntraining.1*
%{_mandir}/man1/combine_tessdata.1*
%{_mandir}/man1/mftraining.1*
%{_mandir}/man1/tesseract.1*
%{_mandir}/man1/unicharset_extractor.1*
%{_mandir}/man1/wordlist2dawg.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtesseract.so
%{_includedir}/%{name}
%{_mandir}/man5/unicharambigs.5*
%{_mandir}/man5/unicharset.5*

%files static
%defattr(644,root,root,755)
%{_libdir}/libtesseract.a
