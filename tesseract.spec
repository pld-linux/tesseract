# TODO:
# - warnings at compile stage about pointer size on amd64 - needs check
# - build dynamic library, not the static one
#
%define		lang_version	2.00

Summary:	Tesseract Open Source OCR Engine
Summary(pl.UTF-8):	Tesseract - silnik OCR o otwartych źródłach
Name:		tesseract
Version:	2.03
Release:	0.9
License:	Apache v2.0
Group:		Applications/Graphics
Source0:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	5777b70b11df16c1ac9aa155d7cfc553
Source1:	http://tesseract-ocr.googlecode.com/files/%{name}-%{lang_version}.eng.tar.gz
# Source1-md5:	b8291d6b3a63ce7879d688e845e341a9
Source2:	http://tesseract-ocr.googlecode.com/files/%{name}-%{lang_version}.fra.tar.gz
# Source2-md5:	64896b462e62572a3708bb461820126c
Source3:	http://tesseract-ocr.googlecode.com/files/%{name}-%{lang_version}.ita.tar.gz
# Source3-md5:	2759e1dae91a989a43490ff4c2253a4b
Source4:	http://tesseract-ocr.googlecode.com/files/%{name}-%{lang_version}.deu.tar.gz
# Source4-md5:	609d91b1ae3759a756b819b5d8403653
Source5:	http://tesseract-ocr.googlecode.com/files/%{name}-%{lang_version}.spa.tar.gz
# Source5-md5:	bc26a777b2384613895677cb8e61ca75
Source6:	http://tesseract-ocr.googlecode.com/files/%{name}-%{lang_version}.nld.tar.gz
# Source6-md5:	b2f6ede182cea4bbfffd3b040533ce58
Patch0:		%{name}-no-java.patch
Patch1:		%{name}-gcc43.patch
URL:		http://code.google.com/p/tesseract-ocr/
BuildRequires:	automake
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A commercial quality OCR engine originally developed at HP between
1985 and 1995. In 1995, this engine was among the top 3 evaluated by
UNLV. It was open-sourced by HP and UNLV in 2005.

%description -l pl.UTF-8
Silnik OCR o komercyjnej jakości oryginalnie stworzony przez HP w
latach 1985-1995. W 1995 roku był jednym z 3 najlepszych wg UNLV.
Źródła zostały uwolnione przez HP i UNLV w 2005 roku.

%package lang-de
Summary:	German language data for Tesseract
Summary(pl.UTF-8):	Dane języka niemieckiego dla Tesseracta
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	tesseract-deu

%description lang-de
This package contains the data files required to recognize German
language.

%description lang-de -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
niemieckiego.

%package lang-en
Summary:	English language data for Tesseract
Summary(pl.UTF-8):	Dane języka angielskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	tesseract-eng

%description lang-en
This package contains the data files required to recognize English
language.

%description lang-en -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
angielskiego.

%package lang-es
Summary:	Spanish language data for Tesseract
Summary(pl.UTF-8):	Dane języka hiszpańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	tesseract-spa

%description lang-es
This package contains the data files required to recognize Spanish
language.

%description lang-es -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
hiszpańskiego.

%package lang-fr
Summary:	French language data for Tesseract
Summary(pl.UTF-8):	Dane języka francuskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	tesseract-fra

%description lang-fr
This package contains the data files required to recognize French
language.

%description lang-fr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
francuskiego.

%package lang-it
Summary:	Italian language data for Tesseract
Summary(pl.UTF-8):	Dane języka włoskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	tesseract-ita

%description lang-it
This package contains the data files required to recognize Italian
language.

%description lang-it -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
włoskiego.

%package lang-nl
Summary:	Dutch language data for Tesseract
Summary(pl.UTF-8):	Dane języka holenderskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	tesseract-nl

%description lang-nl
This package contains the data files required to recognize Dutch
language.

%description lang-nl -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
holenderskiego.

%package devel
Summary:	Tesseract - Development header files and libraries
Summary(pl.UTF-8):	Tesseract - Pliki nagłówkowe i biblioteki dla programistów
Group:          Development/Libraries

%description devel
This package contains the development header files and libraries
necessary to develop applications using Tesseract.

%prep
%setup -q
tar xzf %{SOURCE1}
tar xzf %{SOURCE2}
tar xzf %{SOURCE3}
tar xzf %{SOURCE4}
tar xzf %{SOURCE5}
tar xzf %{SOURCE6}
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub config
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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/cntraining
%attr(755,root,root) %{_bindir}/mftraining
%attr(755,root,root) %{_bindir}/tesseract
%attr(755,root,root) %{_bindir}/unicharset_extractor
%attr(755,root,root) %{_bindir}/wordlist2dawg
%dir %{_datadir}/tessdata
%{_datadir}/tessdata/confsets
%dir %{_datadir}/tessdata/configs
%{_datadir}/tessdata/configs/*
%dir %{_datadir}/tessdata/tessconfigs
%{_datadir}/tessdata/tessconfigs/*

%files lang-de
%defattr(644,root,root,755)
%{_datadir}/tessdata/deu.*

%files lang-en
%defattr(644,root,root,755)
%{_datadir}/tessdata/eng.*

%files lang-es
%defattr(644,root,root,755)
%{_datadir}/tessdata/spa.*

%files lang-fr
%defattr(644,root,root,755)
%{_datadir}/tessdata/fra.*

%files lang-it
%defattr(644,root,root,755)
%{_datadir}/tessdata/ita.*

%files lang-nl
%defattr(644,root,root,755)
%{_datadir}/tessdata/nld.*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.a
