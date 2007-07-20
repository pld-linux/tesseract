# NOTE
# - warnings at compile stage about pointer size on amd64
# - what to do with all the headers and static libs? remove?
Summary:	Tesseract Open Source OCR Engine
Summary(pl.UTF-8):	Tesseract - silnik OCR o otwartych źródłach
Name:		tesseract
Version:	2.00
Release:	0.1
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

%prep
%setup -q
#%patch0 -p1
tar zxf %{SOURCE1}
tar xzf %{SOURCE2}
tar xzf %{SOURCE3}
tar xzf %{SOURCE4}
tar xzf %{SOURCE5}
tar xzf %{SOURCE6}

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
%{_datadir}/tessdata/*

%package deu
Summary:	German language data for Tesseract
Group:		Applications/Graphics
Requires:	tesseract >= 2.0

%description deu
The %{name}-%{version}.deu package contains the data files required to
recognize German

%files deu
%defattr(644,root,root,755)
%{_datadir}/tessdata/deu.DangAmbigs
%{_datadir}/tessdata/deu.freq-dawg
%{_datadir}/tessdata/deu.inttemp
%{_datadir}/tessdata/deu.normproto
%{_datadir}/tessdata/deu.pffmtable
%{_datadir}/tessdata/deu.unicharset
%{_datadir}/tessdata/deu.user-words
%{_datadir}/tessdata/deu.word-dawg

%package eng
Summary:	English language data for Tesseract
Group:		Applications/Graphics
Requires:	tesseract >= 2.0

%description eng
The %{name}-%{version}.eng package contains the data files required to
recognize English

%files eng
%defattr(644,root,root,755)
%{_datadir}/tessdata/eng.DangAmbigs
%{_datadir}/tessdata/eng.freq-dawg
%{_datadir}/tessdata/eng.inttemp
%{_datadir}/tessdata/eng.normproto
%{_datadir}/tessdata/eng.pffmtable
%{_datadir}/tessdata/eng.unicharset
%{_datadir}/tessdata/eng.user-words
%{_datadir}/tessdata/eng.word-dawg

%package fra
Summary:	French language data for Tesseract
Group:		Applications/Graphics
Requires:	tesseract >= 2.0

%description fra
The %{name}-%{version}.fra package contains the data files required to
recognize French

%files fra
%defattr(644,root,root,755)
%{_datadir}/tessdata/fra.DangAmbigs
%{_datadir}/tessdata/fra.freq-dawg
%{_datadir}/tessdata/fra.inttemp
%{_datadir}/tessdata/fra.normproto
%{_datadir}/tessdata/fra.pffmtable
%{_datadir}/tessdata/fra.unicharset
%{_datadir}/tessdata/fra.user-words
%{_datadir}/tessdata/fra.word-dawg

%package ita
Summary:	Italian language data for Tesseract
Group:		Applications/Graphics
Requires:	tesseract >= 2.0

%description ita
The %{name}-%{version}.ita package contains the data files required to
recognize Italian

%files ita
%defattr(644,root,root,755)
%{_datadir}/tessdata/ita.DangAmbigs
%{_datadir}/tessdata/ita.freq-dawg
%{_datadir}/tessdata/ita.inttemp
%{_datadir}/tessdata/ita.normproto
%{_datadir}/tessdata/ita.pffmtable
%{_datadir}/tessdata/ita.unicharset
%{_datadir}/tessdata/ita.user-words
%{_datadir}/tessdata/ita.word-dawg

%package nld
Summary:	Dutch language data for Tesseract
Group:		Applications/Graphics
Requires:	tesseract >= 2.0

%description nld
The %{name}-%{version}.nld package contains the data files required to
recognize Dutch

%files nld
%defattr(644,root,root,755)
%{_datadir}/tessdata/nld.DangAmbigs
%{_datadir}/tessdata/nld.freq-dawg
%{_datadir}/tessdata/nld.inttemp
%{_datadir}/tessdata/nld.normproto
%{_datadir}/tessdata/nld.pffmtable
%{_datadir}/tessdata/nld.unicharset
%{_datadir}/tessdata/nld.user-words
%{_datadir}/tessdata/nld.word-dawg

%package spa
Summary:	Spanish language data for Tesseract
Group:		Applications/Graphics
Requires:	tesseract >= 2.0

%description spa
The %{name}-%{version}.spa package contains the data files required to
recognize Spanish

%files spa
%defattr(644,root,root,755)
%{_datadir}/tessdata/spa.DangAmbigs
%{_datadir}/tessdata/spa.freq-dawg
%{_datadir}/tessdata/spa.inttemp
%{_datadir}/tessdata/spa.normproto
%{_datadir}/tessdata/spa.pffmtable
%{_datadir}/tessdata/spa.unicharset
%{_datadir}/tessdata/spa.user-words
%{_datadir}/tessdata/spa.word-dawg
