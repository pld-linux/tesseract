# NOTE
# - warnings at compile stage about pointer size on amd64
Summary:	Tesseract Open Source OCR Engine
Summary(pl):	Tesseract - silnik OCR o otwartych ¼ród³ach
Name:		tesseract
Version:	1.03
Release:	1
License:	Apache Software License v2
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/tesseract-ocr/%{name}-%{version}.tar.gz
# Source0-md5:	8a191bff04b6f6bc908b3838bfc7f937
URL:		http://sourceforge.net/projects/tesseract-ocr
BuildRequires:	automake
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A commercial quality OCR engine originally developed at HP between
1985 and 1995. In 1995, this engine was among the top 3 evaluated by
UNLV. It was open-sourced by HP and UNLV in 2005.

%description -l pl
Silnik OCR o komercyjnej jako¶ci oryginalnie stworzony przez HP w
latach 1985-1995. W 1995 roku by³ jednym z 3 najlepszych wg UNLV.
¬ród³a zosta³y uwolnione przez HP i UNLV w 2005 roku.

%prep
%setup -q

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
