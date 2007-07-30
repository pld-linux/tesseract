# TODO:
# - warnings at compile stage about pointer size on amd64 - needs check
# - build dynamic library, not the static one
Summary:	Tesseract Open Source OCR Engine
Summary(pl.UTF-8):	Tesseract - silnik OCR o otwartych źródłach
Name:		tesseract
Version:	2.00
Release:	0.9
License:	Apache Software License v2
Group:		Applications/Graphics
Source0:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	6d68d940ed15c61300cb04019c30f46c
Source1:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.eng.tar.gz
# Source1-md5:	b8291d6b3a63ce7879d688e845e341a9
Source2:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.fra.tar.gz
# Source2-md5:	64896b462e62572a3708bb461820126c
Source3:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.ita.tar.gz
# Source3-md5:	2759e1dae91a989a43490ff4c2253a4b
Source4:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.deu.tar.gz
# Source4-md5:	609d91b1ae3759a756b819b5d8403653
Source5:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.spa.tar.gz
# Source5-md5:	bc26a777b2384613895677cb8e61ca75
Source6:	http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.nld.tar.gz
# Source6-md5:	b2f6ede182cea4bbfffd3b040533ce58
Patch0:		%{name}-globals.patch
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

%package lang-deu
Summary:	German language data for Tesseract
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-deu

%description lang-deu
The Tesseract deu package contains the data files required to
recognize German language.

%package lang-eng
Summary:	English language data for Tesseract
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-eng

%description lang-eng
The Tesseract eng package contains the data files required to
recognize English language.

%package lang-fra
Summary:	French language data for Tesseract
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-fra

%description lang-fra
The Tesseract fra package contains the data files required to
recognize French language.

%package lang-ita
Summary:	Italian language data for Tesseract
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-ita

%description lang-ita
The Tesseract ita package contains the data files required to
recognize Italian language.

%package lang-nld
Summary:	Dutch language data for Tesseract
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-nld

%description lang-nld
The Tesseract nld package contains the data files required to
recognize Dutch language.

%package lang-spa
Summary:	Spanish language data for Tesseract
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-spa

%description lang-spa
The Tesseract spa package contains the data files required to
recognize Spanish language.

%package devel
Summary:	Tesseract - Development header files and libraries
Summary(pl.UTF-8):	Tesseract - Pliki nagłówkowe i biblioteki dla programistów
Group:          Development/Libraries

%description devel
This package contains the development header files and libraries
necessary to develop applications using Tesseract.

%prep
%setup -q
#%patch0 -p1
tar -zxvf %{SOURCE1}
tar -zxvf %{SOURCE2}
tar -zxvf %{SOURCE3}
tar -zxvf %{SOURCE4}
tar -zxvf %{SOURCE5}
tar -zxvf %{SOURCE6}

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

%files lang-deu
%defattr(644,root,root,755)
%{_datadir}/tessdata/deu.*

%files lang-eng
%defattr(644,root,root,755)
%{_datadir}/tessdata/eng.*

%files lang-fra
%defattr(644,root,root,755)
%{_datadir}/tessdata/fra.*

%files lang-ita
%defattr(644,root,root,755)
%{_datadir}/tessdata/ita.*

%files lang-nld
%defattr(644,root,root,755)
%{_datadir}/tessdata/nld.*

%files lang-spa
%defattr(644,root,root,755)
%{_datadir}/tessdata/spa.*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.a
